# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-04 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_reports', '0002_auto_20170804_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temperature',
            field=models.CharField(max_length=20, verbose_name='temperature'),
        ),
    ]