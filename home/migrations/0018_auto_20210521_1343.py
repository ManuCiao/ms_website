# Generated by Django 3.1.9 on 2021-05-21 13:43

from django.db import migrations
import streams.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210521_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('about_me', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Enter your details in this table', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo', '---------', 'copy', 'cut---------', 'alignment'], 'editor': 'text', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'})), ('markdown_table', wagtail.core.blocks.StreamBlock([('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code'))], help_text='Enter your details in markdown', required=False))])), ('education', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('progress_bars', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('experience', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('services', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('my_projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading'))])), ('testimonial', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.StructBlock([('sub_heading', wagtail.core.blocks.CharBlock(help_text='Enter sub-heading', required=True)), ('heading', wagtail.core.blocks.CharBlock(help_text='Enter heading', required=True))], help_text='Enter heading and subheading')), ('testimonials', wagtail.core.blocks.ListBlock(streams.blocks.TestimonialBlock))]))], blank=True, null=True),
        ),
    ]
