# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('params', models.CharField(default=b'{}', max_length=10000)),
                ('results', models.CharField(default=b'{}', max_length=10000)),
                ('experiment', models.CharField(default=b'{}', max_length=10000)),
                ('researcher', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('wid', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
            ],
        ),
    ]
