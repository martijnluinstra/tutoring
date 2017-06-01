# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-08 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverAccounts', '0014_auto_20170508_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covermember',
            name='appears_anonymous',
            field=models.BooleanField(default=False, help_text='Checking this means that your name and profile picture will not appear anywhere on this page. However your tutoring offers and requests can still be seen, including what you wrote in their descriptions.', verbose_name='Hide name'),
        ),
        migrations.AlterField(
            model_name='covermember',
            name='receives_mail_notification',
            field=models.BooleanField(default=True, help_text='If checked, you will be receiving email notifications whenever someone writes you a message.', verbose_name='Enable mail notification'),
        ),
    ]
