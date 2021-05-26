from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import (
    BaseSetting,
    register_setting,
)
from wagtail.core.fields import RichTextField

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

@register_setting
class SocialMediaSettings(BaseSetting):

    github = models.URLField(
        blank=True, help_text="Enter your Github URL"
    )
    twitter = models.URLField(
        blank=True, help_text="Enter your Twitter URL"
    )
    linkedin = models.URLField(
        blank=True, help_text="Enter your Linkedin URL"
    )
    medium = models.URLField(
        blank=True, help_text="Enter your Medium URL"
    )
    figma = models.URLField(
        blank=True, help_text="Enter your Figma URL"
    )

    panels = [
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("linkedin"),
        FieldPanel("medium"),
        FieldPanel("figma"),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "social_media_settings"
        )
        cache.delete(key)

        return super().save(*args, **kwargs)


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

    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "footer_contact_settings"
        )
        cache.delete(key)

        return super().save(*args, **kwargs)
