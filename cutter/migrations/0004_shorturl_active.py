# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0003_auto_20171122_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
