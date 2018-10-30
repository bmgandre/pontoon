# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-12 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0134_google_translate_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='configuration_file',
            field=models.CharField(blank=True, help_text='\n        A path to the optional project configuration file, relative to the\n        source string repository.\n        ', max_length=2000, null=True),
        ),
    ]