from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from main import models
from .serializers import DonorSerializer

class ListDonor(generics.ListCreateAPIView):
    queryset = models.DonorForm.objects.all()
    serializer_class = DonorSerializer

class DetailDonor(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DonorForm.objects.all()
    serializer_class = DonorSerializer