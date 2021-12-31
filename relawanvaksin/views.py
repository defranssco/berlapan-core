from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.fields import JSONField
from rest_framework.utils import json
from .forms import Form_relawan_vaksin
from .models import Model_relawan_vaksin
from django.views.generic import ListView, DetailView,TemplateView,View

import base64

from rest_framework import permissions

from django.core.files.base import ContentFile

from .serializers import relawanVaksinSerializer

from rest_framework import viewsets
from rest_framework import serializers
 # Create your views here.
 #Views form daftar relawan vaksin
def index(request) :
    submitted = False
    response ={}
    form = Form_relawan_vaksin(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Daftar_relawan/?submitted=True')
    else :
        form = Form_relawan_vaksin
        if 'submitted' in request.GET :
            submitted = True

        # return redirect('/Daftar_relawan/selesai')
    response['form']= form
    response['submitted'] = submitted
    return render(request,'Daftar_relawan_vaksin.html',response)
   

# Hanya dapat diakses setelah login
@method_decorator(login_required, name='dispatch')
class lihat_data_relawan_vaksin(ListView):
   
    model= Model_relawan_vaksin
    template_name = "data_relawan_vaksin.html"
    

@method_decorator(login_required, name='dispatch')
class detail_relawan_vaksin(DetailView):
    model = Model_relawan_vaksin
    template_name = "detail_relawan_vaksin.html"
    context_object_name = 'relawan_vaksin'

# Membuat fungsi load more di js
# Sumber :https://www.youtube.com/watch?v=P2KdFZZyruo
class MainView(TemplateView):
      template_name = "data_relawan_vaksin_singkat.html"

class PostJsonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        indeks_akhir = kwargs.get('num_posts')
        indeks_awal = indeks_akhir - 3 
        posts = list(Model_relawan_vaksin.objects.values()[indeks_awal:indeks_akhir])
        posts_size = len(Model_relawan_vaksin.objects.all())
        max_size = True if indeks_akhir >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)

class serialisasi(viewsets.ModelViewSet):
    
    queryset = Model_relawan_vaksin.objects.all()
    serializer_class = relawanVaksinSerializer

class relawanVaksin(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Model_relawan_vaksin.objects.all()
    serializer_class = relawanVaksinSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def add_to_django(request):
    if (request.method == "POST"):
        data = json.loads(request.body)
        Nama = data['Nama']
        umur = data['umur']
        nomor_hp =  data['nomor_hp']
        nomor_ktp = data['nomor_hp']
        email = data['email']

        # import base64
        print(data['foto'])
        format, imgstr = data['foto'].split(';base64,') 
        ext = format.split('/')[-1] 

        datafoto = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        # datafoto = data

        foto = datafoto

        alamat = data['alamat']
        
        Riwayat_nakes = data['Riwayat_nakes']
    
        Peran = data['Peran']

        relawanVaksin = Model_relawan_vaksin()

        relawanVaksin.Nama = Nama

        relawanVaksin.umur = umur

        relawanVaksin.nomor_hp = nomor_hp

        relawanVaksin.nomor_ktp = nomor_ktp

        relawanVaksin.email = email

        relawanVaksin.foto = foto

        relawanVaksin.alamat = alamat

        relawanVaksin.Riwayat_nakes = Riwayat_nakes

        relawanVaksin.Peran = Peran

        relawanVaksin.save()

        # relawanVaksins = Model_relawan_vaksin.objects.all()

        # data = serializers.serialize('json', relawanVaksins)
        # return HttpResponse(data, content_type="application/json")