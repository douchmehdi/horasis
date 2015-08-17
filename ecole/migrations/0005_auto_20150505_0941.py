# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecole', '0004_auto_20150504_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='note',
            name='anneeScolaire',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matiere',
        ),
    ]
