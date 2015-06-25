# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0022_auto_20150619_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitie',
            name='picked',
        ),
    ]
