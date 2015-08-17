from django import forms
from models import Eleve, Professeur

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ('nom','prenom','dateDeNaissance','dateInscription','telephone','adresse',)

class ProfesseurForm(forms.ModelForm):
	class Meta:
		model=Professeur
		fields=('nom','prenom',)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)