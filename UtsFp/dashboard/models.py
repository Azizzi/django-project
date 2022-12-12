from django.db import models

# Create your models here.
class komik(models.Model):
    kodekomik = models.CharField(max_length=8)
    namakomik = models.CharField(max_length=120)
    penerbit = models.CharField(max_length=50)
    stockkomik = models.IntegerField()
    hargakomik = models.BigIntegerField()

    def __str__(self):
        return self.namakomik

class daftarkomik(models.Model):
    kodekomik = models.CharField(max_length=8)
    namakomik = models.CharField(max_length=120)
    penerbit = models.CharField(max_length=50)

    def __str__(self):
        return "{}. {}".format(self.kodekomik,self.namakomik)