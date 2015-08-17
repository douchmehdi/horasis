# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iscaf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseigne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Cours dispens\xc3\xa9s')),
                ('tarifHoraire', models.DecimalField(verbose_name=b'tarif horaire en euros', max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.DecimalField(max_digits=5, decimal_places=2)),
                ('eleve', models.ForeignKey(to='iscaf.Eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Surveille',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b"date de l'examen")),
                ('duree', models.DecimalField(verbose_name=b'dur\xc3\xa9e de la surveillance', max_digits=5, decimal_places=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'date du trajet')),
                ('sens', models.DateTimeField(verbose_name=b'Sens AI ou IA')),
                ('Professeur', models.ForeignKey(to='iscaf.Professeur')),
                ('chauffeur', models.ForeignKey(to='iscaf.Chauffeur')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='ue',
            field=models.ForeignKey(default=0, to='iscaf.UE'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periode',
            name='cursus',
            field=models.ForeignKey(default=datetime.datetime(2015, 4, 30, 16, 3, 51, 276074, tzinfo=utc), to='iscaf.Cursus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ue',
            name='periode',
            field=models.ForeignKey(default=datetime.datetime(2015, 4, 30, 16, 5, 8, 969129, tzinfo=utc), to='iscaf.Periode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveille',
            name='matiere',
            field=models.ForeignKey(to='iscaf.Matiere'),
        ),
        migrations.AddField(
            model_name='surveille',
            name='surveillant',
            field=models.ForeignKey(to='iscaf.Surveillant'),
        ),
        migrations.AddField(
            model_name='note',
            name='matiere',
            field=models.ForeignKey(to='iscaf.Matiere'),
        ),
        migrations.AddField(
            model_name='enseigne',
            name='matiere',
            field=models.ForeignKey(to='iscaf.Matiere'),
        ),
        migrations.AddField(
            model_name='enseigne',
            name='professeur',
            field=models.ForeignKey(to='iscaf.Professeur'),
        ),
        migrations.AddField(
            model_name='professeur',
            name='matieres',
            field=models.ManyToManyField(to='iscaf.Matiere', through='iscaf.Enseigne'),
        ),
        migrations.AddField(
            model_name='surveillant',
            name='matiere',
            field=models.ManyToManyField(to='iscaf.Matiere', through='iscaf.Surveille'),
        ),
    ]
