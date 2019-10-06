# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-06 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_auto_20191006_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location'),
        ),
    ]