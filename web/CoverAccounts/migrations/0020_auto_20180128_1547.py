# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-28 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoverAccounts', '0019_auto_20180128_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covermember',
            name='receives_mail_notification',
        ),
        migrations.AddField(
            model_name='covermember',
            name='receives_daily_mails',
            field=models.BooleanField(default=True, help_text='If checked, you will be receiving daily email updates on new messages, but of course only if there are unread ones.', verbose_name='Enable daily mail digests'),
        ),
        migrations.AddField(
            model_name='covermember',
            name='receives_weekly_mails',
            field=models.BooleanField(default=False, help_text='If checked, you will be receiving weekly email updates on new messages, but of course only if there are unread ones.', verbose_name='Enable weekly mail digests'),
        ),
        migrations.AlterField(
            model_name='covermember',
            name='telegram_bot_token',
            field=models.CharField(default=None, help_text='You can setup the "CACTuS Messenger" bot in Telegram. The bot will ask you for this code.', max_length=160, verbose_name='Telegram Bot Token'),
        ),
    ]