# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecole', '0005_auto_20150505_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isDone', models.BooleanField(default=False)),
                ('anneeScolaire', models.ForeignKey(default=b'1', to='ecole.AnneeScolaire')),
                ('matiere', models.ForeignKey(to='ecole.Matiere')),
                ('session', models.ForeignKey(to='ecole.Session')),
            ],
        ),
    ]
