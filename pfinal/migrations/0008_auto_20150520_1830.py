# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0007_auto_20150520_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='kind',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.FloatField(max_length=100.0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
