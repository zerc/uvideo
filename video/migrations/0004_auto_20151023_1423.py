# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20151023_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('order', '-created', '-id')},
        ),
        migrations.AddField(
            model_name='video',
            name='order',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
