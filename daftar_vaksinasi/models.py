from django.db import models
from django.db.models.deletion import  CASCADE
from django.db.models.fields import DateField


class JamTersedia(models.Model):
    jam = models.TimeField()

    def __str__(self):
        return self.jam

class TanggalTersedia(models.Model):
    tanggal = models.DateField()

    def __str__(self):
        return str(self.tanggal)

class Provinsi(models.Model):
    provinsi = models.CharField(max_length=100)

    def __str__(self):
        return self.provinsi

class KabupatenKota(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=CASCADE, null=True)
    kabupaten_kota = models.CharField(max_length=100)

    def __str__(self):
        return self.kabupaten_kota


class SentraVaksinasi(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=CASCADE, null=True)
    kabupaten_kota = models.ForeignKey(KabupatenKota, on_delete=CASCADE, null=True)
    alamat_sentra_vaksinasi = models.TextField()

    def __str__(self):
        return self.alamat_sentra_vaksinasi + ", " + str(self.kabupaten_kota) + ", " + str(self.provinsi)

class PesertaVaksinasi(models.Model):
    nama = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    nik = models.CharField(max_length=50)

    alamat_sentra_vaksinasi = models.ForeignKey(SentraVaksinasi, on_delete=CASCADE, null=True)

    tanggal_vaksinasi = models.ForeignKey(TanggalTersedia, on_delete=CASCADE, null=True)
    jam_vaksinasi = models.ForeignKey(JamTersedia, on_delete=CASCADE, null=True)

    PILIHAN_VAKSINASI_KE = (('1','1'), ('2','2'))
    vaksinasi_ke = models.CharField(max_length=1, choices=PILIHAN_VAKSINASI_KE, null=True)

    def __str__(self):
        return self.nama
