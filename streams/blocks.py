from wagtail.core import blocks


class TitleBlock(blocks.StructBlock):

    text = blocks.CharBlock(
        required=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display"

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


## education block
# port_sub_heading text
# port_heading text

#### repeat block ####
# left_title text
# right_title text
# education_place text h3
# education_place richtext p 


## progress bar block
#### repeat block ####
# data-percent text
# circle span text

## experience block


## my services block


## my projects block


## testimonials could be a block or admin??


## get in touch block
