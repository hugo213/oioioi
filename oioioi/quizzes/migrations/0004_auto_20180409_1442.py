# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-09 14:42
from __future__ import unicode_literals

from django.db import migrations
import oioioi.base.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_questionreport_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionreport',
            name='status',
            field=oioioi.base.fields.EnumField(default=b'WA', max_length=64, verbose_name='status'),
        ),
    ]
