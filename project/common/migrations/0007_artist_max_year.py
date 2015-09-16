# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_album_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='max_year',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
