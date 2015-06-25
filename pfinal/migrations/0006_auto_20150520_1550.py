# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0005_auto_20150520_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(default=None, max_length=250),
            preserve_default=True,
        ),
    ]
