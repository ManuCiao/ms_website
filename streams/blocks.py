from django import forms
from django.db.models.fields import CharField, URLField
from django.template.loader import render_to_string
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.core.blocks.list_block import ListBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

from wagtailfontawesome.blocks import IconBlock
from wagtailmarkdown.blocks import MarkdownBlock

NEW_TABLE_OPTIONS = {
    "minSpareRows": 0,
    "startRows": 4,
    "startCols": 4,
    "colHeaders": False,
    "rowHeaders": False,
    "contextMenu": [
        "row_above",
        "row_below",
        "---------",
        "col_left",
        "col_right",
        "---------",
        "remove_row",
        "remove_col",
        "---------",
        "undo",
        "redo",
        "---------",
        "copy",
        "cut" "---------",
        "alignment",
    ],
    "editor": "text",
    "stretchH": "all",
    "renderer": "html",
    "autoColumnSize": False,
}


class AnyMarkDownBlock(blocks.StreamBlock):
    markdown = MarkdownBlock(
        icon="code", help_text="Enter your details in markdown", required=False
    )


class AnyIconBlock(blocks.StreamBlock):
    icon = IconBlock(help_text="Enter your icon from fontawesome",)


class TitleBlock(blocks.StructBlock):

    sub_heading = blocks.CharBlock(required=True, help_text="Enter sub-heading")
    heading = blocks.CharBlock(required=True, help_text="Enter heading")

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display"


class LinkValue(blocks.StructValue):
    """Additional logic for our links"""

    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")
        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link
        return ""


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(max_length=50, default="More details")
    internal_page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkValue


class AnyRichTextBlock(blocks.StructBlock):
    context = blocks.RichTextBlock(
        help_text="Enter your richtext here",
        features=[
            "h1",
            "h2",
            "h2",
            "h4",
            "h5",
            "h6",
            "bold",
            "italic",
            "ol",
            "ul",
            "hr",
            "link",
            "document-link",
            "image",
            "embed",
            "code",
            "subscript",
            "strikethrough",
            "blockquote",
        ]
    )


class Card(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, help_text="Bold title text 100 max lenght")
    text = blocks.TextBlock(
        max_length=255, help_text="Optional text of 255 characters", required=False
    )
    image = ImageChooserBlock(help_text="image cropped")
    link = Link(help_text="Enter an external link or select an internal page")


class CardsBlock(blocks.StructBlock):

    cards = blocks.ListBlock(Card())

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Cards"
        help_text = "Centered text to display"


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(choices=self.field.widget.choices)


class ImageAndTestBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    image_alignment = RadioSelectBlock(
        choices=(("left", "image to the left"), ("right", "image to the right")),
        default="left",
        help_text="image with text",
    )
    title = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    text = blocks.CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"


class AnyTableBlock(TableBlock):
    table = TableBlock(
        table_options=NEW_TABLE_OPTIONS, help_text="Enter your details in this table"
    )


class AboutMeBlock(blocks.StructBlock):
    image_table = ImageChooserBlock(
        help_text="Enter the image for the left table", label="Image Table"
    )
    title_table = TitleBlock(
        help_text="Enter heading and subheading of the table", label="Left Title Table"
    )
    table = AnyTableBlock()
    # markdown = AnyMarkDownBlock()
    title = TitleBlock(
        help_text="Enter heading and subheading", label="Right Title RichText"
    )
    ricktext = AnyRichTextBlock()
    link_cv_document = DocumentChooserBlock()
    btn_download_text = TitleBlock(
        help_text="Enter 2 texts for btn", label="First Button Text"
    )
    hire_url = Link(help_text="Write the url to link to", label="Hire Button URL")
    btn_hire_text = TitleBlock(
        help_text="Enter 2 texts for btn", label="Second Button Text"
    )

    class Meta:
        template = "streams/about_me.html"


class InfoBlock(blocks.StructBlock):
    block_alignment = RadioSelectBlock(
        choices=(("left", "block to the left"), ("right", "block to the right")),
        default="left",
        help_text="Block Alignment",
    )
    block_color = RadioSelectBlock(
        choices=(
            ("pink", "pink background"),
            ("yellow", "yellow background"),
            ("orange", "orange background"),
            ("cyan", "cyan background"),
        ),
        default="pink",
        help_text="Block Color",
    )


class EducationBlock(blocks.StructBlock):
    info_block = InfoBlock(help_text="Enter block alignement and color")
    number_block = blocks.CharBlock(max_length=60, help_text="Enter first, second, third or fourth")
    edu_mainyear = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    state_title = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    number_title = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    education_place_span = blocks.CharBlock(
        max_length=60, help_text="Max length 60 characters"
    )
    education_place_h3 = blocks.CharBlock(
        max_length=60, help_text="Max length 60 characters"
    )
    education_place_richtext = AnyRichTextBlock()


class EducationsBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")
    education_block = blocks.ListBlock(EducationBlock)

    class Meta:
        template = "streams/education.html"
        icon = "grip"
        label = "Education"


class ProgressBarBlock(blocks.StructBlock):
    progress_bar = blocks.ListBlock(TitleBlock(help_text="Enter percentage and title"))

    class Meta:
        template = "streams/progress_bars.html"
        icon = "spinner"
        label = "Progress Bars"


class ExperienceBlock(blocks.StructBlock):
    info_block = InfoBlock(help_text="Enter block alignement and color")
    ex_leftside_h1_up = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    ex_leftside_h4 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    ex_leftside_h1_down = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    ex_rightside_h4 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    ex_rightside_span = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    company_span = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    ex_details_p = blocks.CharBlock(max_length=255, help_text="Max length 60 characters")
    more_content_p = blocks.CharBlock(max_length=255, help_text="Max length 60 characters")


class ExperiencesBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")
    experience_block = blocks.ListBlock(ExperienceBlock)

    class Meta:
        template = "streams/experience.html"
        icon = "list-ul"
        label = "Experience"


class ServiceBlock(blocks.StructBlock):
    image_service = ImageChooserBlock(
        help_text="Enter the image for the service", label="Image Service"
    )
    service_title = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    service_richtext = AnyRichTextBlock()


class ServicesBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")
    services = blocks.ListBlock(ServiceBlock)

    class Meta:
        template = "streams/services.html"
        icon = "cog"
        label = "Services"


class MyProjectBlock(blocks.StructBlock):
    data_filter_classname_01 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    data_filter_classname_02 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters", required=False)
    image = ImageChooserBlock()
    grid_content_h3 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters")
    

class MyProjectsBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")
    data_filter_01 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters", required=False)
    data_filter_02 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters", required=False)
    data_filter_03 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters", required=False)
    data_filter_04 = blocks.CharBlock(max_length=60, help_text="Max length 60 characters", required=False)
    my_project_block = blocks.ListBlock(MyProjectBlock)

    class Meta:
        template = "streams/my_projects.html"
        icon = "image"
        label = "My Projects"


class TestimonialBlock(blocks.StructBlock):
    testimonial_snippet = SnippetChooserBlock(target_model="testimonials.Testimonial")


class TestimonialsBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")
    testimonials = blocks.ListBlock(TestimonialBlock)

    class Meta:
        template = "streams/testimonial_block.html"


## get in touch block
# port_sub_heading text
# port_heading text
# port_head_wrapper text

### create forms app for the contact form ###
