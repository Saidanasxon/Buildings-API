from rest_framework import serializers
from .models import *

class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'

class KompaniyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kompaniya
        fields = '__all__'

class BinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bino
        fields = '__all__'
