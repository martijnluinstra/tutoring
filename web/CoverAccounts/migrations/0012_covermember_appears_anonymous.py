# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-01 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverAccounts', '0011_auto_20170307_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='covermember',
            name='appears_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]