# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150915_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='lastfm_playcount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
