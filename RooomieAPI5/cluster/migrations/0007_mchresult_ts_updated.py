# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-31 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0006_auto_20180601_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='mchresult',
            name='TS_UPDATED',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
