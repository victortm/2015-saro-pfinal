# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0021_activitie_infourl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitie',
            old_name='infourl',
            new_name='moreinfo',
        ),
    ]
