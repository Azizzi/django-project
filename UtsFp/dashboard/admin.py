from django.contrib import admin

# Register your models here.
from .models import komik

admin.site.register(komik)

from .models import daftarkomik

admin.site.register(daftarkomik)