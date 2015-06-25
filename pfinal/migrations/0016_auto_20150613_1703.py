# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0015_auto_20150613_1027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='myacc',
        ),
    ]
