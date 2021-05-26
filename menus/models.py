from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.utils.html import TRAILING_PUNCTUATION_CHARS, urlize
from modelcluster.models import ClusterableModel
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.documents.edit_handlers import DocumentChooserPanel 
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


class MenuItem(Orderable):
    link_title = models.CharField(
        blank=True, max_length=100
    )
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(
        default=False, blank=True
    )
    svg = models.ForeignKey(
        'wagtaildocs.Document',
        blank=True,
        null=True, 
        related_name='+',
        on_delete=models.SET_NULL, # Only works with null=True
    )


    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
        DocumentChooserPanel("svg"),
    ]

    page = ParentalKey("Menu", related_name="menu_items")

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'

class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("menu_items", label="Menu Item")
    ]

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        key = make_template_fragment_key(
            "sidebar_menu"
        )
        cache.delete(key)

        return super().save(**kwargs)