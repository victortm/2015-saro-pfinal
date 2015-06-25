# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
