# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-06 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(null=True,blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True,blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
            preserve_default=False,
        ),
    ]
