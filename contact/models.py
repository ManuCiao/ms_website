from django.db import models
from modelcluster.models import ParentalKey
from streams import blocks
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    parent_page_types = ["home.HomePage"]
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = (
        "contact/contact_page_landing.html"
    )
    subpage_types = []
    max_count = 1

    intro = RichTextField(
        blank=True, features=["bold", "link", "ol", "ul"]
    )
    thank_you_text = RichTextField(
        blank=True, features=["bold", "link", "ol", "ul"]
    )
    map_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text="Image cropped",
        related_name="+",
    )
    map_url = models.URLField(
        blank=True,
        help_text="Optional. Provide a link to make the map image to become a link",
    )

    body = StreamField(
        [("title", blocks.TitleBlock())],
        null=True,
        blank=True,
    )

    content_panels = AbstractEmailForm.content_panels + [
        StreamFieldPanel("body"),
        FieldPanel("intro"),
        ImageChooserPanel("map_image"),
        FieldPanel("map_url"),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address", classname="col6"),
                FieldPanel("to_address", classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
