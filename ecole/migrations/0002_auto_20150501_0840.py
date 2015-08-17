# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecole', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='telephone',
            field=models.IntegerField(default=138),
        ),
        migrations.AlterField(
            model_name='periode',
            name='periode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nombreMatieres',
            field=models.IntegerField(default=8),
        ),
    ]
