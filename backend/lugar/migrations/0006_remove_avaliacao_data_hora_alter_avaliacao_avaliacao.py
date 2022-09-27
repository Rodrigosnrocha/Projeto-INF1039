# Generated by Django 4.1.1 on 2022-09-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugar', '0005_avaliacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='data_hora',
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliacao',
            field=models.IntegerField(choices=[(1, 'Upvote'), (0, 'Neutral'), (-1, 'Downvote')]),
        ),
    ]
