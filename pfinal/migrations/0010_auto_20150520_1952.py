# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0009_auto_20150520_1928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='event',
            new_name='activitie',
        ),
    ]
