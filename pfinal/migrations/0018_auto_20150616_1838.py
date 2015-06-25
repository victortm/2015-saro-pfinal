# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0017_remove_activitie_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitie',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
