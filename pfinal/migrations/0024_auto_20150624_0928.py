# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0023_remove_activitie_picked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='moreinfo',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
    ]
