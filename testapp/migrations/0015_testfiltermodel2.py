# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0014_auto_20180607_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFilterModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_bool', models.NullBooleanField()),
                ('_int', models.IntegerField()),
            ],
        ),
    ]
