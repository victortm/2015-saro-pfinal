# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0004_activity_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='kind',
            field=models.CharField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='price',
            field=models.FloatField(default=None, max_length=100.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.TimeField(default=None),
            preserve_default=True,
        ),
    ]
