from django.shortcuts import render
from dashboard.models import Barang ,Transaksi ,Sandal

def utama(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'data.html')

def produk(request):
    titelnya= "produk"
    konteks= {
        'titel' : titelnya,
    }
    return render(request,'produk.html',konteks)
# Create your views here.

def tampilBrg(request):
    barang = Barang.objects.all()
    konteks = {
        'barang': barang ,
    }
    return render(request, 'tampil_brg.html', konteks)

def tampilSandal(request):
    sandal = Sandal.objects.all()
    konteks = {
        'sandal': sandal ,
    }
    return render (request, 'tampil_sandal.html', konteks)
