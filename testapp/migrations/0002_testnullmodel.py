# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-30 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestNullModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_null_blank', models.TextField(blank=True, null=True)),
                ('can_null', models.TextField(null=True)),
                ('can_blank', models.TextField(blank=True)),
                ('can_default', models.TextField(default='')),
                ('can', models.TextField()),
            ],
        ),
    ]
