# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_artist_lastfm_playcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=20)),
                ('year', models.PositiveIntegerField(default=0)),
                ('artist', models.ForeignKey(related_name='albums', to='common.Artist')),
            ],
        ),
        migrations.AddField(
            model_name='release',
            name='is_get_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='release',
            name='is_to_album',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='release',
            name='artist',
            field=models.ForeignKey(related_name='releases', to='common.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='releases',
            field=models.ManyToManyField(related_name='albums', to='common.Release', blank=True),
        ),
    ]
