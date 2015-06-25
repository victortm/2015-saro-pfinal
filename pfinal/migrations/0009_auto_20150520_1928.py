# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0008_auto_20150520_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.FloatField(max_length=200.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
