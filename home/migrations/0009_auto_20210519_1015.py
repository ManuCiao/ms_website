# Generated by Django 3.1.9 on 2021-05-19 10:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text 100 max lenght', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text of 255 characters', max_length=255, required=False))])))]))], blank=True, null=True),
        ),
    ]
