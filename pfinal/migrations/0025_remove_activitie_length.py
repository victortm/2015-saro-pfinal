# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0024_auto_20150624_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitie',
            name='length',
        ),
    ]
