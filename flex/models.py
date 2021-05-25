from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import RichTextBlock
from streams import blocks

from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage"]
    body = StreamField(
        [
            ("about_me", blocks.AboutMeBlock()),
            ("education", blocks.EducationsBlock()),
            ("progress_bars", blocks.ProgressBarBlock()),
            ("experience", blocks.ExperiencesBlock()),
            ("services", blocks.ServicesBlock()),
            ("my_projects", blocks.MyProjectsBlock()),
            ("testimonial", blocks.TestimonialsBlock()),
            (
                "richtext",
                RichTextBlock(
                    template="streams/richtext_block.html"
                ),
            )
            # ("testimonial", SnippetChooserBlock(
            # target_model='testimonials.Testimonial',
            # template='streams/testimonial_block.html'
            # ))
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"


    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "flex_page_streams",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args, **kwargs)
