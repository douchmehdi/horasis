# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecole', '0006_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='examen',
            field=models.ForeignKey(default=b'1', to='ecole.Examen'),
        ),
    ]
