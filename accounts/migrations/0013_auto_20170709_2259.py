# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20170709_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='degree',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(max_length=100),
        ),
    ]