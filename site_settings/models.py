from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField


@register_setting
class SocialMediaSettings(BaseSetting):

    github = models.URLField(blank=True, help_text="Enter your Github URL")
    twitter = models.URLField(blank=True, help_text="Enter your Twitter URL")
    linkedin = models.URLField(blank=True, help_text="Enter your Linkedin URL")
    medium = models.URLField(blank=True, help_text="Enter your Medium URL")
    figma = models.URLField(blank=True, help_text="Enter your Figma URL")

    panels = [
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("linkedin"),
        FieldPanel("medium"),
        FieldPanel("figma"),
    ]


@register_setting
class ContactSettings(BaseSetting):

    location = RichTextField(
        blank=True,
        null=True,
        features=["link"],
    )

    phone = RichTextField(
        blank=True,
        null=True,
        features=["link"],
    )

    email = RichTextField(
        blank=True,
        null=True,
        features=["link"],
    )

    panels = [
        FieldPanel("location"),
        FieldPanel("phone"),
        FieldPanel("email"),
    ]


## footer settings
# footer_heading location p
# footer_heading contact p
# footer_heading contact url
# footer_heading email p
# footer_heading email url
