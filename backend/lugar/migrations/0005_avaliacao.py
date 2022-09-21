# Generated by Django 4.1.1 on 2022-09-21 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lugar', '0004_lugar_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.TextField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugar.lugar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
