# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fill_order(apps, *args, **kwargs):
    Video = apps.get_model('video', 'Video')

    for i, video in enumerate(Video.objects.all().order_by('order')):
        video.order = i
        video.save()


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20151023_1423'),
    ]

    operations = [
        migrations.RunPython(fill_order, lambda *args, **kwargs: True),
    ]
