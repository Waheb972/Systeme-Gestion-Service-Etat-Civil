# Generated by Django 4.1.5 on 2023-01-27 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActeCivil',
            fields=[
                ('Matricule', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=255)),
                ('Prenom', models.CharField(max_length=255)),
                ('Sexe', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], max_length=6)),
                ('Profession', models.CharField(max_length=255)),
                ('Domicile', models.CharField(max_length=255)),
                ('DateN', models.DateTimeField(blank=True, null=True, verbose_name='Date de Naissance')),
                ('LieuN', models.CharField(blank=True, max_length=255, null=True, verbose_name='Lieu de Naissance')),
                ('VilleN', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ville de Naissance')),
                ('PaysN', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pays de Naissance')),
            ],
        ),
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('NumC', models.IntegerField(primary_key=True, serialize=False)),
                ('NomC', models.CharField(max_length=255)),
                ('NomD', models.CharField(max_length=255)),
                ('NomW', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Registre',
            fields=[
                ('NumR', models.IntegerField(primary_key=True, serialize=False)),
                ('AnneeR', models.IntegerField()),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registre_bureau', to='Gestion.bureau')),
            ],
        ),
        migrations.CreateModel(
            name='Officier',
            fields=[
                ('Matricule', models.IntegerField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=255)),
                ('Prenom', models.CharField(max_length=255)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Actif', models.BooleanField(default=True)),
                ('Role', models.CharField(choices=[('Maire', 'Maire'), ('Titulaire', 'Titulaire'), ('Officier', 'Officier')], max_length=10)),
                ('Password', models.CharField(max_length=255)),
                ('Bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officier_bureau', to='Gestion.bureau')),
            ],
        ),
        migrations.CreateModel(
            name='ActeMariage',
            fields=[
                ('Matricule', models.IntegerField(primary_key=True, serialize=False)),
                ('DateM', models.DateField(verbose_name='Date du mariage')),
                ('LieuM', models.CharField(max_length=255, verbose_name='Lieu du mariage')),
                ('Officier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteMariage_officier', to='Gestion.officier', verbose_name='Officier Déclarant')),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteMariage_bureau', to='Gestion.bureau', verbose_name="Bureau d'état civil")),
                ('femme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_femme', to='Gestion.actecivil', verbose_name='Acte Civile de la femme')),
                ('filiation_mere_femme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_mere_femme', to='Gestion.actecivil', verbose_name='Filitation, Mère de la femme')),
                ('filiation_mere_marie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_mere_marie', to='Gestion.actecivil', verbose_name='Filitation, Mère du marie')),
                ('filiation_pere_femme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_pere_femme', to='Gestion.actecivil', verbose_name='Filitation, Père de la femme')),
                ('filiation_pere_marie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_pere_marie', to='Gestion.actecivil', verbose_name='Filitation, Père du marie')),
                ('marie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteCivil_marie', to='Gestion.actecivil', verbose_name='Acte Civile du marie')),
                ('temoin1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_temoin1', to='Gestion.actecivil', verbose_name='Acte Civile du Temoin 1')),
                ('temoin2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_temoin2', to='Gestion.actecivil', verbose_name='Acte Civil du Temoin 2')),
            ],
        ),
        migrations.CreateModel(
            name='ActeDeces',
            fields=[
                ('Matricule', models.IntegerField(primary_key=True, serialize=False)),
                ('DateD', models.DateField(verbose_name='Date du décès')),
                ('LieuD', models.CharField(max_length=255, verbose_name='Lieu du décès')),
                ('Concerne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_decede', to='Gestion.actecivil')),
                ('Officier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteDeces_officier', to='Gestion.officier', verbose_name='Officier Déclarant')),
                ('Temoin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_temoin', to='Gestion.actecivil', verbose_name='Temoin du décès')),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteDeces_bureau', to='Gestion.bureau', verbose_name="Bureau d'état civil")),
            ],
        ),
        migrations.AddField(
            model_name='actecivil',
            name='Officier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteCivil_officier', to='Gestion.officier', verbose_name='Officier Déclarant'),
        ),
        migrations.AddField(
            model_name='actecivil',
            name='bureau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteCivil_bureau', to='Gestion.bureau', verbose_name="Bureau d'état civil"),
        ),
        migrations.AddField(
            model_name='actecivil',
            name='declarant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actCivil_declarant', to='Gestion.actecivil', verbose_name='Acte Civil du déclarant'),
        ),
        migrations.AddField(
            model_name='actecivil',
            name='mere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acteCivil_mere', to='Gestion.actecivil', verbose_name='Acte Civil de la mère'),
        ),
        migrations.AddField(
            model_name='actecivil',
            name='pere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acteCivil_pere', to='Gestion.actecivil', verbose_name='Acte Civil du père'),
        ),
    ]
