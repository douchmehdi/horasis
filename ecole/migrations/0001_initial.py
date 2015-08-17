# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('dateDeNaissance', models.DateTimeField(verbose_name=b'date de naissance')),
                ('adresse', models.CharField(max_length=300)),
                ('dateInscription', models.DateTimeField(verbose_name=b"date d'inscription")),
            ],
        ),
        migrations.CreateModel(
            name='Enseigne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Cours dispens\xc3\xa9s')),
                ('tarifHoraire', models.DecimalField(verbose_name=b'tarif horaire en euros', max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.DecimalField(max_digits=5, decimal_places=2)),
                ('eleve', models.ForeignKey(to='ecole.Eleve')),
                ('matiere', models.ForeignKey(to='ecole.Matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periode', models.IntegerField(default=0, max_length=2)),
                ('cursus', models.ForeignKey(to='ecole.Cursus')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('matieres', models.ManyToManyField(to='ecole.Matiere', through='ecole.Enseigne')),
            ],
        ),
        migrations.CreateModel(
            name='Surveillant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Surveille',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b"date de l'examen")),
                ('duree', models.DecimalField(verbose_name=b'dur\xc3\xa9e de la surveillance', max_digits=5, decimal_places=1)),
                ('matiere', models.ForeignKey(to='ecole.Matiere')),
                ('surveillant', models.ForeignKey(to='ecole.Surveillant')),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'date du trajet')),
                ('sens', models.DateTimeField(verbose_name=b'Sens AI ou IA')),
                ('Professeur', models.ForeignKey(to='ecole.Professeur')),
                ('chauffeur', models.ForeignKey(to='ecole.Chauffeur')),
            ],
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('nombreMatieres', models.IntegerField(default=8, max_length=10)),
                ('periode', models.ForeignKey(to='ecole.Periode')),
            ],
        ),
        migrations.AddField(
            model_name='surveillant',
            name='matiere',
            field=models.ManyToManyField(to='ecole.Matiere', through='ecole.Surveille'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='ue',
            field=models.ForeignKey(to='ecole.UE'),
        ),
        migrations.AddField(
            model_name='enseigne',
            name='matiere',
            field=models.ForeignKey(to='ecole.Matiere'),
        ),
        migrations.AddField(
            model_name='enseigne',
            name='professeur',
            field=models.ForeignKey(to='ecole.Professeur'),
        ),
    ]
