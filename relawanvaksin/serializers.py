from .models import Model_relawan_vaksin
from rest_framework import serializers

class relawanVaksinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model_relawan_vaksin
        fields = ['Nama','umur','nomor_ktp','nomor_hp','email','alamat','Peran','Riwayat_nakes', 'foto']  #'foto'