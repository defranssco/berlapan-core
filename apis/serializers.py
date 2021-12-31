from django.db.models import fields
from rest_framework import serializers
from main import models

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=models.DonorForm