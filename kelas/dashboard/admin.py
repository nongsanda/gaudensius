from django.contrib import admin
from .models import Barang , Jenis , Detailtrans , Transaksi , Sandal

# Register your models here.
admin.site.register(Barang)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)
admin.site.register(Jenis)
admin.site.register(Sandal)

