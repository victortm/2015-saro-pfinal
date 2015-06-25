# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0020_auto_20150619_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitie',
            name='infourl',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
