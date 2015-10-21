# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cover', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('cover', pyuploadcare.dj.models.ImageField(blank=True)),
                ('video_file', pyuploadcare.dj.models.FileField()),
                ('collection', models.ForeignKey(to='video.Collection')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
