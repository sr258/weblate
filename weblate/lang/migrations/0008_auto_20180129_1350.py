# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0007_migrate_plurals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plural',
            options={'ordering': ['source'], 'verbose_name': 'Plural form', 'verbose_name_plural': 'Plural forms'},
        ),
        migrations.AlterField(
            model_name='plural',
            name='equation',
            field=models.CharField(default='n != 1', max_length=400, verbose_name='Plural equation'),
        ),
    ]
