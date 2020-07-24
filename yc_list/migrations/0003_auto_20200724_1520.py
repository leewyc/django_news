# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('yc_list', '0002_yclistviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='views',
            name='gcontext',
            field=tinymce.models.HTMLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='views',
            name='gtitle',
            field=models.CharField(max_length=200),
        ),
    ]
