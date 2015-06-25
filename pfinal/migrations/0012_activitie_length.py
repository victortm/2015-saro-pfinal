# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0011_activitie_longlength'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitie',
            name='length',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
