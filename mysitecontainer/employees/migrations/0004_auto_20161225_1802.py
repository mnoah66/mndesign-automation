# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-25 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20161223_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]