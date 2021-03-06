# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cutter', '0005_auto_20171125_0420'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('short_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cutter.ShortURL')),
            ],
        ),
        migrations.CreateModel(
            name='ClickEventManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
