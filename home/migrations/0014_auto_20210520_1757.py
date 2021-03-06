# Generated by Django 3.1.9 on 2021-05-20 17:57

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210519_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('about_me', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('table', streams.blocks.AnyTableBlock(help_text='Enter your details in this table'))])), ('education', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('progress_bars', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('experience', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('services', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('my_projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('testimonial', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('testimonials', wagtail.core.blocks.ListBlock(streams.blocks.TestimonialBlock))]))], blank=True, null=True),
        ),
    ]
