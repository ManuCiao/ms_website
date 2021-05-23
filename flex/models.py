from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import RichTextBlock
from streams import blocks

class FlexPage(Page):

    body = StreamField([
        ("about_me", blocks.AboutMeBlock()),
        ("education", blocks.EducationsBlock()),
        ("progress_bars", blocks.ProgressBarBlock()),
        ("experience", blocks.ExperiencesBlock()),
        ("services", blocks.ServicesBlock()),
        ("my_projects", blocks.MyProjectsBlock()),
        ("testimonial", blocks.TestimonialsBlock()),
        ("richtext", RichTextBlock(
            template="streams/richtext_block.html"
        ))
        # ("testimonial", SnippetChooserBlock(
        # target_model='testimonials.Testimonial', 
        # template='streams/testimonial_block.html'
        # ))
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]
    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"
