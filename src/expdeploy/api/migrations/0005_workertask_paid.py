# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160324_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='workertask',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
