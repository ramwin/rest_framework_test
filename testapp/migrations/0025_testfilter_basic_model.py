# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-11 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0024_testfilter'),
    ]

    operations = [
        migrations.AddField(
            model_name='testfilter',
            name='basic_model',
            field=models.ManyToManyField(to='testapp.BasicModel'),
        ),
    ]