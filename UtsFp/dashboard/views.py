from django.shortcuts import render
# from dashboard.form import Fromkomik
# from dashboard.form import Fromdaftarkomik
from dashboard.models import komik
from dashboard.models import daftarkomik

# Create your views here.

def Komik_View(request):
    komiks=komik.objects.all()

    konteks={
        'komiks':komiks,
    }
    return render(request,'Tampil_komik.html',konteks)

def Daftarkomik_View(request):
    daftarkomiks=daftarkomik.objects.all()

    konteks={
        'daftarkomiks':daftarkomiks,
    }
    return render(request,'Tampil_daftarkomik.html',konteks)