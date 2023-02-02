"""UtsFp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
#from dashboard.views import Komik_View, Daftarkomik_View, tambah_komik, tambah_daftarkomik
from dashboard.views import *

def Home(request):
    titlenya="Home"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Home.html',konteks)
def Daftar(request):
    titlenya="Daftar"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Daftar.html',konteks)
def Populer(request):
    titlenya="Populer"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Populer.html',konteks)
def Bookmark(request):
    titlenya="Bookmark"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Bookmark.html',konteks)
def Contactus(request):
    titlenya="Contact Us"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Contact us.html',konteks)
def Project(request):
    titlenya="Project"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Project.html',konteks)
def Signin(request):
    titlenya="Sign In"
    konteks = {
        'title':titlenya,
    }
    return render(request,'Sign in.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home),
    path('Daftar/',Daftar),
    path('Populer/',Populer),
    path('Bookmark/',Bookmark),
    path('Contactus/',Contactus),
    path('Project/',Project),
    path('Signin/',Signin),
    path('tabelkomik/',Komik_View),
    path('daftarkomik/',Daftarkomik_View),
    path('tambahkomik/',tambah_komik),
    path('tambahdaftarkomik/',tambah_daftarkomik),
    path('ubahkomik/<int:id_komik>',ubah_Komik,name='ubah_komik'),
    path('ubahdaftarkomik/<int:id_daftarkomik>',ubahdaftarkomik,name='ubahdaftarkomik'),
    path('hapusdaftarkomik/<int:id_daftarkomik>',hapusdaftarbarang,name='hapusdaftarkomik'),
    path('hapuskomik/<int:id_komik>',hapuskomik,name='hapuskomik'),
]
