# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-30 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('philatelist', '0004_auto_20181230_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='stamp',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
    ]
