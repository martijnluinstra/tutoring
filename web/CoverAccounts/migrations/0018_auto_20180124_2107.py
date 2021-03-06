# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverAccounts', '0017_covermember_is_alpha_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covermember',
            name='is_alpha_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='covermember',
            name='receives_mail_notification',
            field=models.BooleanField(default=True, help_text='If checked, you will be receiving weekly email updates on what you missed.', verbose_name='Enable mail digests'),
        ),
    ]
