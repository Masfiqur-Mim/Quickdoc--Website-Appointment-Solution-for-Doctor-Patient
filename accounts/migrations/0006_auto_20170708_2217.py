# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170708_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contact_no',
            field=models.CharField(default='012', max_length=20, null=True),
        ),
    ]
