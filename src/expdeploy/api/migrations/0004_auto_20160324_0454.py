# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160324_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workertask',
            name='results',
            field=models.TextField(default=b'{"data":[], "metadata":[]}'),
        ),
    ]
