# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0016_auto_20150613_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitie',
            name='price',
        ),
    ]
