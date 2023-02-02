from django.shortcuts import render, redirect
from dashboard.form import Formkomik, Formdaftarkomik
from dashboard.models import komik, daftarkomik
from django.contrib import messages

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

def tambah_komik(request):
    if request.POST:
        form=Formkomik(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = Formkomik()
            konteks={
                'form':form,
            }
            return render(request,'tambah_komik.html',konteks)
    else:
        form=Formkomik()
        konteks = {
            'form':form,
        }
        return render(request,'tambah_komik.html',konteks)

def ubah_Komik(request,id_komik):
    komiks=komik.objects.get(id=id_komik)
    if request.POST:
        form=Formkomik(request.POST,instance=komiks)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_komik',id_komik=id_komik)
    else:
        form=Formkomik(instance=komiks)
        konteks = {
            'form':form,
            'komiks':komiks
        }
        return render(request,'ubah_komik.html',konteks)

def hapuskomik(request,id_komik):
    komiks=komik.objects.filter(id=id_komik)
    komiks.delete()
    messages.success(request,'Data Terhapus')
    return redirect('/tabelkomik')

def tambah_daftarkomik(request):
    if request.POST:
        form=Formdaftarkomik(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = Formdaftarkomik()
            konteks={
                'form':form,
            }
            return render(request,'tambah_daftarkomik.html',konteks)
    else:
        form=Formdaftarkomik()
        konteks = {
            'form':form,
        }
        return render(request,'tambah_daftarkomik.html',konteks)

def ubahdaftarkomik(request,id_daftarkomik):
    daftarkomiks=daftarkomik.objects.get(id=id_daftarkomik)
    if request.POST:
        form=Formdaftarkomik(request.POST,instance=daftarkomiks)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubahdaftarkomik',id_daftarkomik=id_daftarkomik)
    else:
        form=Formdaftarkomik(instance=daftarkomiks)
        konteks = {
            'form':form,
            'daftarkomiks':daftarkomiks
        }
        return render(request,'ubah_daftarkomik.html',konteks)

def hapusdaftarbarang(request,id_daftarkomik):
    daftarkomiks=daftarkomik.objects.filter(id=id_daftarkomik)
    daftarkomiks.delete()
    messages.success(request,'Data Terhapus')
    return redirect('/daftarkomik')