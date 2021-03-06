# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-12-05 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0009_filefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='default_submissions_limit',
            field=models.IntegerField(blank=True, default=10, help_text='Use 0 for unlimited submissions.', verbose_name='default submissions limit'),
        ),
        migrations.AlterField(
            model_name='probleminstance',
            name='submissions_limit',
            field=models.IntegerField(default=10, help_text='Use 0 for unlimited submissions.', verbose_name='submissions limit'),
        ),
    ]
