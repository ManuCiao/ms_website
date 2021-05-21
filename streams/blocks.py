from django import forms
from django.template.loader import render_to_string
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtailfontawesome.blocks import IconBlock
from wagtailmarkdown.blocks import MarkdownBlock


NEW_TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo',
        '---------',
        'copy',
        'cut'
        '---------',
        'alignment',
    ],
    'editor': 'text',
    'stretchH': 'all',
    'renderer': 'html',
    'autoColumnSize': False,
}

class MarkDownBlock(blocks.StreamBlock):
    markdown = MarkdownBlock(icon="code")


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
        choices=(("left", "imange to the left"), ("right", "image to the right")),
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
    table = TableBlock(table_options=NEW_TABLE_OPTIONS, help_text="Enter your details in this table")

class AboutMeBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")
    title_table = TitleBlock(help_text="Enter heading and subheading of the table")
    table = TableBlock(table_options=NEW_TABLE_OPTIONS, help_text="Enter your details in this table")
    markdown_table = MarkDownBlock(help_text="Enter your details in markdown", required=False)

    class Meta:
        template = "streams/about_me.html"
        icon = "doc-full-inverse"
        label = "About me"

## about me block
# image 445x490
# ps_name text
# ps_designation text
# age value text
# address value text
# email value url
# residence value text
# phone value text
# freelance value text
# github url
# linkedin url
# medium url
# twitter url
# figma url

# port_sub_heading text
# about_tophead text
# signature name h2 text
# signature name p text
# button document
# button 1 text 1
# button 1 txt 2
# button url
# button 2 text 1
# button 2 text 2


class EducationBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")

    class Meta:
        template = "streams/education.html"
        icon = "grip"
        label = "Education"


## education block
# port_sub_heading text
# port_heading text

#### repeat block ####
# left_title text
# right_title text
# education_place text h3
# education_place richtext p


class ProgressBarBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")

    class Meta:
        template = "streams/progress_bars.html"
        icon = "spinner"
        label = "Progress Bars"


## progress bar block
#### repeat block ####
# data-percent text
# circle span text


class ExperienceBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")

    class Meta:
        template = "streams/experience.html"
        icon = "list-ul"
        label = "Experience"


## experience block
# port_sub_heading text
# port_heading text

#### repeat block ####
# color text
# ex_leftside h1 up text
# ex_leftside h4 text
# ex_leftside h1 down text
# ex_rightside h4 text
# ex_rightside span text
# ex_details p text
# more_content p text


class ServicesBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")

    class Meta:
        template = "streams/services.html"
        icon = "cog"
        label = "Services"


## my services block
# port_sub_heading text
# port_heading text

#### repeat block ####
# image icon
# project_heading text
# project_pera text


class MyProjectsBlock(blocks.StructBlock):
    title = TitleBlock(help_text="Enter heading and subheading")

    class Meta:
        template = "streams/my_projects.html"
        icon = "image"
        label = "My Projects"


## my projects block
# port_sub_heading text
# port_heading text

#### repeat block ####
# data-filter text
# image
# grid-content h3 text
# grid-content span text


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


