# Generated by Django 2.0.1 on 2018-01-18 17:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vota', '0002_auto_20180118_1703'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Encuestas',
            new_name='Encuesta',
        ),
    ]
