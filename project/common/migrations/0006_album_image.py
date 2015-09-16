# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20150915_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.URLField(default=b'', max_length=255, blank=True),
        ),
    ]
