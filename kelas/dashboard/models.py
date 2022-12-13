from django.db import models
# Create your models here.
class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.nama
class Barang(models.Model):
    kodebrg = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150, blank=True)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nama

class Sandal(models.Model):
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    waktu_beli = models.DateTimeField(auto_now_add=True)
    komen = models.CharField(max_length=150)
    def __str__(self):
        return self.nama

class Transaksi(models.Model):
    kodetranss = models.CharField(max_length=10)
    total = models.BigIntegerField()
    tgltrans = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kodetranss

class Detailtrans(models.Model):
    kodetrans = models.CharField(max_length=10)
    kodebrg = models.CharField(max_length=8)
    qty = models.BigIntegerField()

    def __str__(self):
        return self.kodebrg
