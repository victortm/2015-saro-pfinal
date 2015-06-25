# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0012_activitie_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='length',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
