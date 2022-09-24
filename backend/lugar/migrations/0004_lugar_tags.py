# Generated by Django 4.1.1 on 2022-09-16 23:22

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('lugar', '0003_rename_author_lugar_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]