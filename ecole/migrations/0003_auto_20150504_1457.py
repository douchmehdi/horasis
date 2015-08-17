# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecole', '0002_auto_20150501_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeScolaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anneeDeDebut', models.IntegerField()),
                ('anneeDeFin', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='periode',
            name='periode',
            field=models.CharField(max_length=5, verbose_name=b'Semestre'),
        ),
        migrations.AlterField(
            model_name='ue',
            name='nom',
            field=models.CharField(max_length=100),
        ),
    ]
