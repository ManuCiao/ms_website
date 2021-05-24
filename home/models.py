from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.documents.edit_handlers import (
    DocumentChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

from wagtailstreamforms.blocks import WagtailFormBlock
from wagtailstreamforms.models.abstract import (
    AbstractFormSetting,
)


class AdvancedFormSetting(AbstractFormSetting):
    to_address = models.EmailField()


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["flex.FlexPage"]
    max_count = 1
    lead_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Heading text under the banner title",
    )
    sub_text_up = models.CharField(
        max_length=255,
        blank=True,
        help_text="Subheading text above the heading title",
    )
    sub_text_down_01 = models.CharField(
        max_length=255,
        blank=True,
        help_text="Subheading text below the heading title 1",
    )
    sub_text_down_02 = models.CharField(
        max_length=255,
        blank=True,
        help_text="Subheading text below the heading title 2",
    )
    sub_text_down_03 = models.CharField(
        max_length=255,
        blank=True,
        help_text="Subheading text below the heading title 3",
    )
    button_01 = models.ForeignKey(
        "wagtaildocs.Document",
        blank=True,
        null=True,
        related_name="+",
        help_text="Select an optional page to link to",
        on_delete=models.SET_NULL,
    )
    button_text_01_1 = models.CharField(
        max_length=50,
        default="Download CV",
        blank=False,
        help_text="Button text 01 1",
    )
    button_text_01_2 = models.CharField(
        max_length=50,
        default="Download",
        blank=False,
        help_text="Button text 01 2",
    )
    button_02 = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Write the url to link to",
    )
    button_text_02_1 = models.CharField(
        max_length=50,
        default="Send Message",
        blank=False,
        help_text="Button text 02 1",
    )
    button_text_02_2 = models.CharField(
        max_length=50,
        default="SEND",
        blank=False,
        help_text="Button text 02 2",
    )
    button_03 = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Write the url to link to",
    )
    button_text_03_1 = models.CharField(
        max_length=50,
        default="Hire Me",
        blank=False,
        help_text="Button text 03 1",
    )
    button_text_03_2 = models.CharField(
        max_length=50,
        default="HIRE",
        blank=False,
        help_text="Button text 03 2",
    )
    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="Banner background image 1902x952",
        on_delete=models.SET_NULL,
    )
    banner_personal_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="Banner personal image 968x945",
        on_delete=models.SET_NULL,
    )

    body = StreamField(
        [
            ("about_me", blocks.AboutMeBlock()),
            ("education", blocks.EducationsBlock()),
            ("progress_bars", blocks.ProgressBarBlock()),
            ("experience", blocks.ExperiencesBlock()),
            ("services", blocks.ServicesBlock()),
            ("my_projects", blocks.MyProjectsBlock()),
            ("testimonial", blocks.TestimonialsBlock()),
            ("form", WagtailFormBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        FieldPanel("sub_text_up"),
        FieldPanel("sub_text_down_01"),
        FieldPanel("sub_text_down_02"),
        FieldPanel("sub_text_down_03"),
        DocumentChooserPanel("button_01"),
        FieldPanel("button_text_01_1"),
        FieldPanel("button_text_01_2"),
        FieldPanel("button_02"),
        FieldPanel("button_text_02_1"),
        FieldPanel("button_text_02_2"),
        FieldPanel("button_03"),
        FieldPanel("button_text_03_1"),
        FieldPanel("button_text_03_2"),
        ImageChooserPanel("banner_background_image"),
        ImageChooserPanel("banner_personal_image"),
        StreamFieldPanel("body"),
    ]
