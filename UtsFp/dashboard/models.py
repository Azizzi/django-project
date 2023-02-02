from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class komik(models.Model):
    kodekomik = models.CharField(max_length=8)
    namakomik = models.CharField(max_length=120)
    penerbit = models.CharField(max_length=50)
    stockkomik = models.IntegerField()
    hargakomik = models.BigIntegerField()
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.namakomik

class daftarkomik(models.Model):
    kodekomik = models.CharField(max_length=8)
    namakomik = models.CharField(max_length=120)
    penerbit = models.CharField(max_length=50)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}".format(self.kodekomik,self.namakomik)