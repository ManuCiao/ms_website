# Generated by Django 3.1.9 on 2021-05-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0003_auto_20210518_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='button',
            new_name='button_01',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='button_text',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_personal_image',
            field=models.ForeignKey(help_text='Banner personal image 968x945', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_02',
            field=models.ForeignKey(blank=True, help_text='Select an optional page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_03',
            field=models.ForeignKey(blank=True, help_text='Select an optional page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text_01',
            field=models.CharField(default='Read More', help_text='Button text 01', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text_02',
            field=models.CharField(default='Read More', help_text='Button text 02', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text_03',
            field=models.CharField(default='Read More', help_text='Button text 03', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sub_text_down',
            field=models.CharField(blank=True, help_text='Subheading text under the banner title', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sub_text_up',
            field=models.CharField(blank=True, help_text='Subheading text under the banner title', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner_background_image',
            field=models.ForeignKey(help_text='Banner background image 1902x952', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Heading text under the banner title', max_length=255),
        ),
    ]
