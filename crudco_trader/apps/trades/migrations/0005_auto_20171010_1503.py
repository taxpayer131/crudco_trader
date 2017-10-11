# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0004_auto_20171010_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='users.User'),
        ),
    ]
