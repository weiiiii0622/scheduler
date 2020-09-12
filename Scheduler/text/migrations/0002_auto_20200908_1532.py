# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='subject',
        ),
        migrations.AddField(
            model_name='link',
            name='scope',
            field=models.CharField(max_length=100, default=0),
        ),
        migrations.AddField(
            model_name='link',
            name='test',
            field=models.CharField(max_length=100, default=0),
        ),
    ]
