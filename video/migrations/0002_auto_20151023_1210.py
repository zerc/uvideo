# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 12, 9, 51, 26031, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 12, 10, 1, 706393, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
