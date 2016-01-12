# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 20:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_artist_max_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-year']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['-lastfm_playcount']},
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ['-year']},
        ),
        migrations.AddField(
            model_name='artist',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 20, 45, 47, 465494, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
