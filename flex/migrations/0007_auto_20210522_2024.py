# Generated by Django 3.1.9 on 2021-05-22 20:24

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_auto_20210522_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('about_me', wagtail.core.blocks.StructBlock([('image_table', wagtail.images.blocks.ImageChooserBlock(help_text='Enter the image for the left table', label='Image Table')), ('title_table', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading of the table', label='Left Title Table')), ('table', streams.blocks.AnyTableBlock()), ('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading', label='Right Title RichText')), ('ricktext', wagtail.core.blocks.StructBlock([('context', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h2', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'subscript', 'strikethrough', 'blockquote'], help_text='Enter your richtext here'))])), ('link_cv_document', wagtail.documents.blocks.DocumentChooserBlock()), ('btn_download_text', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter 2 texts for btn', label='First Button Text')), ('hire_url', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Write the url to link to', label='Hire Button URL')), ('btn_hire_text', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter 2 texts for btn', label='Second Button Text'))])), ('education', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('education_block', wagtail.core.blocks.ListBlock(streams.blocks.EducationBlock))])), ('progress_bars', wagtail.core.blocks.StructBlock([('progress_bar', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter percentage and title')))])), ('experience', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('services', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('services', wagtail.core.blocks.ListBlock(streams.blocks.ServiceBlock))])), ('my_projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('testimonial', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('testimonials', wagtail.core.blocks.ListBlock(streams.blocks.TestimonialBlock))])), ('richtext', wagtail.core.blocks.RichTextBlock(template='streams/richtext_block.html'))], blank=True, null=True),
        ),
    ]
