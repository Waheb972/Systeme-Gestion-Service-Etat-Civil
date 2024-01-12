from django.shortcuts import render, redirect

from Gestion.models import Bureau as BureauModel
from Gestion.models import Officier
from Gestion.models import ActeCivil
from Gestion.models import ActeMariage
from Gestion.models import ActeDeces

from Gestion.forms import BureauForm
from Gestion.forms import OfficierForm
from Gestion.forms import ActeForm
from Gestion.forms import ActeCivilForm
from Gestion.forms import ActeNaissanceForm
from Gestion.forms import ActeMariageForm
from Gestion.forms import ActeDecesForm

def homePage(request):
    return render(request,'home.html')

def basepage(request):
    return render(request,'Gestion/base.html')

def OfficierSimple(request):
    return render(request, 'OfficierSimple.html')

def tit(request):
    return render(request,'titulaire.html')

def login(request):
    if request.method == 'POST':
        matricule = request.POST['matricule']
        password = request.POST['password']
        try:
            officier = Officier.objects.get(Matricule=matricule)
            if officier.Password == password:
                if officier.Role == 'Maire':
                    return render(request, 'Home.html')
                elif officier.Role == 'Titulaire':
                    return render(request,'titulaire.html')
                elif officier.Role == 'Officier':
                    return render(request, 'OfficierSimple.html')
            else:
                return render(request, 'login.html', {'error_message': 'Invalid login'})
        except Officier.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def officier_tit(request):
    dataOfficier = Officier.objects.all()
    return render(request, 'Gestion/Officier/OfficierTitulaire.html', {'dataOfficier':dataOfficier})

def officier_Add_Tit(request):
    dataOfficier = Officier.objects.all()
    if request.method == 'POST':
        form = OfficierForm(request.POST)
        if form.is_valid():
            office = form.save()
            return render(request, 'Gestion/Officier/OfficierTitulaire.html', {'dataOfficier':dataOfficier})
        else:
            return render(request,'Gestion/Officier/addOffTit.html',{'form': form, 'dataOfficier':dataOfficier})
    else:
        form = OfficierForm()
        return render(request,'Gestion/Officier/addOffTit.html', {'form': form, 'dataOfficier':dataOfficier})





def officier_Base(request):
    dataOfficier = Officier.objects.all()
    return render(request, 'Gestion/Officier/Officier.html', {'dataOfficier':dataOfficier})

def officier_Add(request):
    dataOfficier = Officier.objects.all()
    if request.method == 'POST':
        form = OfficierForm(request.POST)
        if form.is_valid():
            office = form.save()
            return render(request, 'Gestion/Officier/Officier.html', {'dataOfficier':dataOfficier})
        else:
            return render(request,'Gestion/Officier/addOff.html',{'form': form, 'dataOfficier':dataOfficier})
    else:
        form = OfficierForm()
        return render(request,'Gestion/Officier/addOff.html', {'form': form, 'dataOfficier':dataOfficier})

def officier_Update(request, id):
    off = Officier.objects.get(Matricule=id)
    if request.method == "POST":
        form = OfficierForm(request.POST, instance=off)
        if form.is_valid():
            form.save()
            return redirect('/Officier/')
    else:
        form = OfficierForm(instance=off)
        return render(request, "Gestion/Officier/updOff.html", {'form': form, 'dataOfficier':Officier.objects.all})

def officier_Delete(request, id):
    form = Officier.objects.get(Matricule=id)
    if request.method == "POST":
        form.delete()
        return redirect('/Officier/')
    else:
        return render(request, "Gestion/Officier/delOff.html", {'off': form, 'dataOfficier':Officier.objects.all})



def Acte_Base(request):
    return render(request, 'Gestion/Acte/Acte.html', {'data':ActeCivil.objects.all})

def Acte_Add(request):
    if request.method == 'POST':
        form = ActeCivilForm(request.POST)
        if form.is_valid():
            acte = form.save()
            return redirect('/Acte/')
        else:
            return render(request,'Gestion/Acte/addActe.html',{'form': form, 'data':ActeCivil.objects.all})
    else:
        form = ActeCivilForm()
        return render(request,'Gestion/Acte/addActe.html', {'form': form, 'data':ActeCivil.objects.all})

def Acte_AddN(request):
    if request.method == 'POST':
        form = ActeNaissanceForm(request.POST)
        if form.is_valid():
            acte = form.save()
            return redirect('/Acte/')
        else:
            return render(request,'Gestion/Acte/addActe.html',{'form': form, 'data':ActeCivil.objects.all})
    else:
        form = ActeNaissanceForm()
        return render(request,'Gestion/Acte/addActe.html', {'form': form, 'data':ActeCivil.objects.all})


def Acte_Delete(request, id):
    form = ActeCivil.objects.get(Matricule=id)
    if request.method == "POST":
        form.delete()
        return redirect('/Acte/')
    else:
        return render(request, "Gestion/Acte/delActe.html", {'form': form, 'data':ActeCivil.objects.all})

def Acte_Update(request, id):
    off = ActeCivil.objects.get(Matricule=id)
    if request.method == "POST":
        form = ActeForm(request.POST, instance=off)
        if form.is_valid():
            form.save()
            return redirect('/Acte/')
    else:
        form = ActeForm(instance=off)
        return render(request, "Gestion/Acte/updActe.html", {'form': form, 'data':ActeCivil.objects.all})



def ActeMariage_Base(request):
    return render(request, 'Gestion/ActeMariage/Acte.html', {'data':ActeMariage.objects.all})

def ActeMariage_Add(request):
    if request.method == 'POST':
        form = ActeMariageForm(request.POST)
        if form.is_valid():
            acte = form.save()
            return redirect('/ActeMariage/')
        else:
            return render(request,'Gestion/ActeMariage/addActe.html',{'form': form, 'data':ActeMariage.objects.all})
    else:
        form = ActeMariageForm()
        return render(request,'Gestion/ActeMariage/addActe.html', {'form': form, 'data':ActeMariage.objects.all})

def ActeMariage_Delete(request, id):
    form = ActeMariage.objects.get(Matricule=id)
    if request.method == "POST":
        form.delete()
        return redirect('/ActeMariage/')
    else:
        return render(request, "Gestion/ActeMariage/delActe.html", {'form': form, 'data':ActeMariage.objects.all})

def ActeMariage_Update(request, id):
    off = ActeMariage.objects.get(Matricule=id)
    if request.method == "POST":
        form = ActeMariageForm(request.POST, instance=off)
        if form.is_valid():
            form.save()
            return redirect('/ActeMariage/')
    else:
        form = ActeMariageForm(instance=off)
        return render(request, "Gestion/ActeMariage/updActe.html", {'form': form, 'data':ActeMariage.objects.all})

def ActeDeces_Base(request):
    return render(request, 'Gestion/ActeDeces/Acte.html', {'data':ActeDeces.objects.all})

def ActeDeces_Add(request):
    if request.method == 'POST':
        form = ActeDecesForm(request.POST)
        if form.is_valid():
            acte = form.save()
            return redirect('/ActeDeces/')
        else:
            return render(request,'Gestion/ActeDeces/addActe.html',{'form': form, 'data':ActeDeces.objects.all})
    else:
        form = ActeDecesForm()
        return render(request,'Gestion/ActeDeces/addActe.html', {'form': form, 'data':ActeDeces.objects.all})

def ActeDeces_Delete(request, id):
    form = ActeDeces.objects.get(Matricule=id)
    if request.method == "POST":
        form.delete()
        return redirect('/ActeDeces/')
    else:
        return render(request, "Gestion/ActeDeces/delActe.html", {'form': form, 'data':ActeDeces.objects.all})

def ActeDeces_Update(request, id):
    off = ActeDeces.objects.get(Matricule=id)
    if request.method == "POST":
        form = ActeDecesForm(request.POST, instance=off)
        if form.is_valid():
            form.save()
            return redirect('/ActeDeces/')
    else:
        form = ActeDecesForm(instance=off)
        return render(request, "Gestion/ActeDeces/updActe.html", {'form': form, 'data':ActeDeces.objects.all})


