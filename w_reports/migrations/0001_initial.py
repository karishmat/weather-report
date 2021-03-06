# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-04 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('temperature', models.CharField(max_length=10, verbose_name='temperature')),
                ('year', models.IntegerField(max_length=10, verbose_name='year')),
                ('month', models.CharField(max_length=10, verbose_name='month')),
                ('season', models.CharField(max_length=15, verbose_name='season')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='w_reports.Country')),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
    ]
