# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0012_defectsperunit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]