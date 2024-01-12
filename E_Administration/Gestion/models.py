from django.db import models
from datetime import date

class Bureau(models.Model):
    NumC = models.IntegerField(primary_key=True)
    NomC = models.CharField(max_length=255)
    NomD = models.CharField(max_length=255)
    NomW = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.NumC}'

    objects = models.Manager()

class Officier(models.Model):
    class role(models.TextChoices):
        Maire = 'Maire'
        Titulaire = 'Titulaire'
        Officier = 'Officier'

    Matricule = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255)
    Date = models.DateField(default=date.today)
    Actif = models.BooleanField(default=True)
    Role = models.CharField(choices=role.choices, max_length=10)
    Bureau = models.ForeignKey(Bureau, related_name='officier_bureau', on_delete=models.CASCADE)
    Password = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.Matricule}'

class Registre(models.Model):
    NumR = models.IntegerField(primary_key=True)
    AnneeR = models.IntegerField()
    bureau = models.ForeignKey(Bureau, related_name='registre_bureau', on_delete=models.CASCADE)

class ActeCivil(models.Model):
    class sexe(models.TextChoices):
        Homme = 'H'
        Femme = 'F'
    Matricule = models.IntegerField(primary_key=True)
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255)
    Sexe = models.CharField(choices=sexe.choices, max_length=6)
    Profession = models.CharField(max_length=255)
    Domicile = models.CharField(max_length=255)
    bureau = models.ForeignKey(Bureau, related_name='acteCivil_bureau', on_delete=models.CASCADE, verbose_name="Bureau d'état civil")
    Officier = models.ForeignKey(Officier, related_name='acteCivil_officier', on_delete=models.CASCADE, verbose_name='Officier Déclarant')
    DateN = models.DateTimeField(verbose_name='Date de Naissance',null=True, blank=True)
    LieuN = models.CharField(max_length=255, verbose_name='Lieu de Naissance',null=True, blank=True)
    VilleN = models.CharField(max_length=255, verbose_name='Ville de Naissance',null=True, blank=True)
    PaysN = models.CharField(max_length=255, verbose_name='Pays de Naissance',null=True, blank=True)
    pere = models.ForeignKey('self', related_name='acteCivil_pere', on_delete=models.CASCADE, verbose_name='Acte Civil du père',null=True, blank=True)
    mere = models.ForeignKey('self', related_name='acteCivil_mere', on_delete=models.CASCADE, verbose_name='Acte Civil de la mère',null=True, blank=True)
    declarant = models.ForeignKey('self', related_name='actCivil_declarant', on_delete=models.CASCADE, verbose_name='Acte Civil du déclarant',null=True, blank=True)
    def __str__(self):
        return f'{self.Matricule}'

class ActeDeces(models.Model):
    Matricule = models.IntegerField(primary_key=True)
    Concerne = models.ForeignKey(ActeCivil, related_name='actCivil_decede', on_delete=models.CASCADE)
    DateD = models.DateField(verbose_name='Date du décès')
    LieuD = models.CharField(max_length=255, verbose_name='Lieu du décès')
    Temoin = models.ForeignKey(ActeCivil, related_name='actCivil_temoin', on_delete=models.CASCADE, verbose_name='Temoin du décès')
    bureau = models.ForeignKey(Bureau, related_name='acteDeces_bureau', on_delete=models.CASCADE,verbose_name="Bureau d'état civil")
    Officier = models.ForeignKey(Officier, related_name='acteDeces_officier', on_delete=models.CASCADE,verbose_name='Officier Déclarant')
    def __str__(self):
        return f'{self.Matricule}'

class ActeMariage(models.Model):
    Matricule = models.IntegerField(primary_key=True)
    DateM = models.DateField(verbose_name='Date du mariage')
    LieuM = models.CharField(max_length=255, verbose_name='Lieu du mariage')
    marie = models.ForeignKey(ActeCivil, related_name='acteCivil_marie', on_delete=models.CASCADE, verbose_name='Acte Civile du marie')
    femme = models.ForeignKey(ActeCivil, related_name='actCivil_femme', on_delete=models.CASCADE, verbose_name='Acte Civile de la femme')
    temoin1 = models.ForeignKey(ActeCivil, related_name='actCivil_temoin1', on_delete=models.CASCADE, verbose_name='Acte Civile du Temoin 1')
    temoin2 = models.ForeignKey(ActeCivil, related_name='actCivil_temoin2', on_delete=models.CASCADE, verbose_name='Acte Civil du Temoin 2')
    filiation_pere_marie = models.ForeignKey(ActeCivil, related_name='actCivil_pere_marie', on_delete=models.CASCADE, verbose_name = 'Filitation, Père du marie')
    filiation_mere_marie = models.ForeignKey(ActeCivil, related_name='actCivil_mere_marie', on_delete=models.CASCADE, verbose_name = 'Filitation, Mère du marie')
    filiation_pere_femme = models.ForeignKey(ActeCivil, related_name='actCivil_pere_femme', on_delete=models.CASCADE, verbose_name = 'Filitation, Père de la femme')
    filiation_mere_femme = models.ForeignKey(ActeCivil, related_name='actCivil_mere_femme', on_delete=models.CASCADE, verbose_name = 'Filitation, Mère de la femme')
    bureau = models.ForeignKey(Bureau, related_name='acteMariage_bureau', on_delete=models.CASCADE,verbose_name="Bureau d'état civil")
    Officier = models.ForeignKey(Officier, related_name='acteMariage_officier', on_delete=models.CASCADE,verbose_name='Officier Déclarant')
    def __str__(self):
        return f'{self.Matricule}'

