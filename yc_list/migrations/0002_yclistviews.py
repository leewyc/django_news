# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yc_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YcListViews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gcontext', models.TextField()),
                ('gpic', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'yc_list_views',
                'managed': False,
            },
        ),
    ]
