"""E_Administration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestion import views

urlpatterns = [
    path('base/', views.basepage),
    path('admin/', admin.site.urls),

    path('OfficierSimple',views.OfficierSimple,name='OfficierSimple'),
    path('Officier/', views.officier_Base,name='Officier_Base'),
    path('OfficierTitulaire',views.officier_tit,name='Officier_tit'),
    path('Officier/add/', views.officier_Add,name='addOff'),
    path('OfficierTit/add/', views.officier_Add_Tit,name='addOffTit'),
    path('Officier/update/<int:id>',views.officier_Update,name='updOff'),
    path('Officier/delete/<int:id>',views.officier_Delete,name='delOff'),
    path('',views.login,name='login'),


    path('Acte/', views.Acte_Base, name='Acte'),
    path('Acte/add/', views.Acte_Add, name='addActe'),
    path('Acte/add_Naissance/', views.Acte_AddN, name='addActeN'),
    path('Acte/delete/<int:id>', views.Acte_Delete, name='delActe'),
    path('Acte/update/<int:id>', views.Acte_Update, name='updActe'),

    path('ActeMariage/', views.ActeMariage_Base, name='ActeM'),
    path('ActeMariage/add/', views.ActeMariage_Add, name='addActeM'),
    path('ActeMariage/delete/<int:id>', views.ActeMariage_Delete, name='delActeM'),
    path('ActeMariage/update/<int:id>', views.ActeMariage_Update, name='updActeM'),

    path('ActeDeces/', views.ActeDeces_Base, name='ActeD'),
    path('ActeDeces/add/', views.ActeDeces_Add, name='addActeD'),
    path('ActeDeces/delete/<int:id>', views.ActeDeces_Delete, name='delActeD'),
    path('ActeDeces/update/<int:id>', views.ActeDeces_Update, name='updActeD'),
]
