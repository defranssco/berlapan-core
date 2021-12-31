from django.shortcuts import render, HttpResponse
from .models import *
from .forms import DaftarVaksinasiForm
from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json

# Create your views here.
def index(request):
    return render(request, 'index_daftar_vaksinasi.html')


def summary(request):
    list_of_peserta = PesertaVaksinasi.objects.all()

    result = PesertaVaksinasi
    for peserta in list_of_peserta:
        if peserta.nama == "Greg":
            result = peserta

    response = {'result':result}
    return render(request, 'tiket_vaksinasi.html', response)


def form_peserta_vaksinasi(request):
    peserta_vaksinasi_form = DaftarVaksinasiForm(request.POST or None)
    if peserta_vaksinasi_form.is_valid():
        peserta_vaksinasi_form.save()
        
    response = {'peserta_vaksinasi_form' : peserta_vaksinasi_form}
    return render(request, 'forms.html', response)



def create(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        tanggal_lahir = request.POST['tanggalLahir']
        nik = request.POST['nik']
        alamat_sentra_vaksinasi = request.POST['alamatSentraVaksinasi']
        tanggal_vaksinasi = request.POST['tanggalVaksinasi']
        jam_vaksinasi = request.POST['jamVaksinasi']
        vaksinasi_ke = request.POST['vaksinasiKe']

        new_peserta_vaksinasi = PesertaVaksinasi(nama=nama, tanggal_lahir=tanggal_lahir, nik=nik, alamat_sentra_vaksinasi=alamat_sentra_vaksinasi, tanggal_vaksinasi=tanggal_vaksinasi, jam_vaksinasi=jam_vaksinasi, vaksinasi_ke=vaksinasi_ke)
        new_peserta_vaksinasi.save()

        success = nama + " telah terdaftar sebagai peserta vaksinasi di " + alamat_sentra_vaksinasi
        return HttpResponse(success)

@csrf_exempt
def alamat_json(request):
    alamats = SentraVaksinasi.objects.all()
    data = serializers.serialize('json', alamats)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def tanggal_json(request):
    tanggals = TanggalTersedia.objects.all()
    data = serializers.serialize('json', tanggals)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def jam_json(request):
    jams = JamTersedia.objects.all()
    data = serializers.serialize('json', jams)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_to_django(request):
    if (request.method == "POST"):
        data = json.loads(request.body)
        nama = data['nama']
        nik = data['nik']
        tanggal_lahir = data['tanggal_lahir']
        sentra = data['sentra']
        tanggal_vaksinasi = data['tanggal_vaksinasi']
        jam = data['jam']
        vaksinasi_ke = data['vaksinasi_ke']

        peserta_baru = PesertaVaksinasi()

        peserta_baru.nama = nama
        peserta_baru.nik = nik
        peserta_baru.tanggal_lahir = tanggal_lahir

        for pilihan in SentraVaksinasi.objects.all():
            if pilihan.alamat_sentra_vaksinasi == sentra:
                peserta_baru.alamat_sentra_vaksinasi = pilihan
                break
        
        for pilihan in TanggalTersedia.objects.all():
            if pilihan.tanggal == tanggal_vaksinasi:
                peserta_baru.tanggal_vaksinasi = pilihan
                break
        
        for pilihan in JamTersedia.objects.all():
            if pilihan.jam == jam:
                peserta_baru.jam_vaksinasi = pilihan
                break
                
        peserta_baru.vaksinasi_ke = vaksinasi_ke
        peserta_baru.save()

        pesertas = PesertaVaksinasi.objects.all()
        data = serializers.serialize('json', pesertas)
        return HttpResponse(data, content_type="application/json")


@csrf_exempt
def peserta_vaksinasi_json(request):
    pesertas = PesertaVaksinasi.objects.all()
    data = serializers.serialize('json', pesertas)
    return HttpResponse(data, content_type="application/json")