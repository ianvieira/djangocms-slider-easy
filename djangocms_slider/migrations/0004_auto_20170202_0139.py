# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-02 03:39
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_slider', '0003_auto_20160728_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Image', verbose_name='image'),
        ),
    ]
