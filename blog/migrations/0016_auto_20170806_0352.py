# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_forum_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='question',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
