# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecole', '0003_auto_20150504_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='InscriptionCursus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='enseigne',
            name='anneeScolaire',
            field=models.ForeignKey(default=b'1', to='ecole.AnneeScolaire'),
        ),
        migrations.AddField(
            model_name='note',
            name='anneeScolaire',
            field=models.ForeignKey(default=b'1', to='ecole.AnneeScolaire'),
        ),
        migrations.AddField(
            model_name='surveille',
            name='anneeScolaire',
            field=models.ForeignKey(default=b'1', to='ecole.AnneeScolaire'),
        ),
        migrations.AddField(
            model_name='trajet',
            name='anneeScolaire',
            field=models.ForeignKey(default=b'1', to='ecole.AnneeScolaire'),
        ),
        migrations.AlterField(
            model_name='anneescolaire',
            name='anneeDeDebut',
            field=models.IntegerField(verbose_name=b'ann\xc3\xa9e de d\xc3\xa9but'),
        ),
        migrations.AlterField(
            model_name='anneescolaire',
            name='anneeDeFin',
            field=models.IntegerField(verbose_name=b'ann\xc3\xa9e de fin'),
        ),
        migrations.AddField(
            model_name='inscriptioncursus',
            name='anneeScolaire',
            field=models.ForeignKey(to='ecole.AnneeScolaire'),
        ),
        migrations.AddField(
            model_name='inscriptioncursus',
            name='cursus',
            field=models.ForeignKey(to='ecole.Cursus'),
        ),
        migrations.AddField(
            model_name='inscriptioncursus',
            name='eleve',
            field=models.ForeignKey(to='ecole.Eleve'),
        ),
    ]
