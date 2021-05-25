from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.utils.html import TRAILING_PUNCTUATION_CHARS
from modelcluster.models import ClusterableModel
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey


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

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    page = ParentalKey("Menu", related_name="menu_items")


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
