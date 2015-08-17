# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscaf', '0002_auto_20150430_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseigne',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='enseigne',
            name='professeur',
        ),
        migrations.RemoveField(
            model_name='matiere',
            name='ue',
        ),
        migrations.RemoveField(
            model_name='note',
            name='eleve',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='periode',
            name='cursus',
        ),
        migrations.RemoveField(
            model_name='professeur',
            name='matieres',
        ),
        migrations.RemoveField(
            model_name='surveillant',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='surveille',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='surveille',
            name='surveillant',
        ),
        migrations.RemoveField(
            model_name='trajet',
            name='Professeur',
        ),
        migrations.RemoveField(
            model_name='trajet',
            name='chauffeur',
        ),
        migrations.RemoveField(
            model_name='ue',
            name='periode',
        ),
        migrations.DeleteModel(
            name='Chauffeur',
        ),
        migrations.DeleteModel(
            name='Cursus',
        ),
        migrations.DeleteModel(
            name='Enseigne',
        ),
        migrations.DeleteModel(
            name='Matiere',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Periode',
        ),
        migrations.DeleteModel(
            name='Professeur',
        ),
        migrations.DeleteModel(
            name='Surveillant',
        ),
        migrations.DeleteModel(
            name='Surveille',
        ),
        migrations.DeleteModel(
            name='Trajet',
        ),
        migrations.DeleteModel(
            name='UE',
        ),
    ]
