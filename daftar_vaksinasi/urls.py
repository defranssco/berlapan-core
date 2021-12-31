from django.urls import path
from .views import *

#app_name = 'forms'

urlpatterns = [ path('', index, name='index'),
                path('forms/tiket_vaksinasi', summary, name='tiket_vaksinasi'),
                path('forms/', form_peserta_vaksinasi, name='forms'),

                path('alamat_json', alamat_json, name='alamat_json'),
                path('tanggal_json', tanggal_json, name='tanggal_json'),
                path('jam_json', jam_json, name='jam_json'),

                path('add_to_django', add_to_django, name='add_to_django'),

                path('peserta_vaksinasi_json', peserta_vaksinasi_json, name='peserta_vaksinasi_json'),

]