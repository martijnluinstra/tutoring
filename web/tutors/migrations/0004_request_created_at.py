# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tutors', '0003_request_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]