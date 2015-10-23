# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def migrate_users(apps, *args, **kwargs):
    Collection = apps.get_model('video', 'Collection')
    User = apps.get_model('auth', 'User')

    user = User.objects.first()

    for col in Collection.objects.filter(user=0):
        col.user_id = user.pk
        col.save()


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20151023_1210'),
    ]

    operations = [
        migrations.RunPython(migrate_users, lambda *args, **kwargs: True),
    ]
