from django import forms
from Gestion.models import Bureau
from Gestion.models import Officier
from Gestion.models import ActeCivil
from Gestion.models import ActeMariage
from Gestion.models import ActeDeces



class BureauForm(forms.ModelForm):
   class Meta:
     model = Bureau
     fields = '__all__'


class OfficierForm(forms.ModelForm):
   class Meta:
     model = Officier
     fields = '__all__'

class ActeForm(forms.ModelForm):
   class Meta:
     model = ActeCivil
     fields = '__all__'


class ActeNaissanceForm(forms.ModelForm):
   class Meta:
     model = ActeCivil
     fields = ('Matricule','Nom','Prenom','Sexe','DateN', 'LieuN', 'VilleN', 'PaysN', 'pere', 'mere', 'declarant','bureau','Officier')

class ActeMariageForm(forms.ModelForm):
   class Meta:
     model = ActeMariage
     fields = '__all__'

class ActeDecesForm(forms.ModelForm):
   class Meta:
     model = ActeDeces
     fields = '__all__'

class ActeCivilForm(forms.ModelForm):
   class Meta:
     model = ActeCivil
     fields = ('Matricule', 'Nom', 'Prenom', 'Sexe', 'Profession', 'Domicile', 'bureau', 'Officier')