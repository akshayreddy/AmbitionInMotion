# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170804_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'ordering': ('-created',)},
        ),
    ]
