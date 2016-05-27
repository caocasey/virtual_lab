# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital', '0005_auto_20160121_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='base_image',
            name='memory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='base_image',
            name='reimage_file',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='base_image',
            name='backing_file',
            field=models.CharField(max_length=500),
        ),
    ]
