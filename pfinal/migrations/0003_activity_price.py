# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0002_auto_20150520_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='price',
            field=models.FloatField(max_length=100.0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
