# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20150915_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='is_get_image',
        ),
        migrations.AddField(
            model_name='album',
            name='is_get_image',
            field=models.BooleanField(default=False),
        ),
    ]
