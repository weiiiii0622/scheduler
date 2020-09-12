# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_auto_20200908_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='subject',
            field=models.IntegerField(default=0),
        ),
    ]
