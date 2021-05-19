# Generated by Django 3.1.9 on 2021-05-19 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='socialmediasettings',
            name='youtube',
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='figma',
            field=models.URLField(blank=True, help_text='Enter your Figma URL'),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='github',
            field=models.URLField(blank=True, help_text='Enter your Github URL'),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='linkedin',
            field=models.URLField(blank=True, help_text='Enter your Linkedin URL'),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='medium',
            field=models.URLField(blank=True, help_text='Enter your Medium URL'),
        ),
    ]
