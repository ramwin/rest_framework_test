# Generated by Django 2.1.5 on 2019-08-19 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0030_datetimeorder'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basicmodel',
            options={'ordering': ('-id',)},
        ),
    ]
