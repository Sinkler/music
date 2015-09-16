# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastfm_mbid', models.CharField(default=b'', max_length=255)),
                ('mbid', models.CharField(default=b'', max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mbid', models.CharField(unique=True, max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=20)),
                ('date', models.CharField(default=b'', max_length=255, blank=True)),
                ('year', models.PositiveIntegerField(default=0)),
                ('country', models.CharField(default=b'', max_length=255, blank=True)),
                ('image', models.URLField(default=b'', max_length=255, blank=True)),
                ('artist', models.ForeignKey(related_name='albums', to='common.Artist')),
            ],
        ),
    ]
