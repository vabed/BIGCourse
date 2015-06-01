# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150531_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(default=1, to='blog.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 13, 34, 21, 444000)),
        ),
    ]
