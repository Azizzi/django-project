from django.forms import ModelForm
from dashboard.models import komik, daftarkomik
from django import forms


class Formkomik(ModelForm):
    class Meta :
         model=komik
         fields='__all__'

         widgets = {
            'kodekomik': forms.TextInput({'class':'form-control'}),
            'namakomik': forms.TextInput({'class':'form-control'}), 
            'penerbit': forms.TextInput({'class':'form-control'}),
            'stockkomik': forms.NumberInput({'class':'form-control'}), 
            'hargakomik': forms.NumberInput({'class':'form-control'}), 
            'jenis_id': forms.Select({'class':'form-control'}), 
         }

class Formdaftarkomik(ModelForm):
     class Meta :
         model=daftarkomik
         fields='__all__'

         witgets = {
            'kodekomik': forms.TextInput({'class':'form-control'}),
            'namakomik': forms.TextInput({'class':'form-control'}),
            'penerbit': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
         }