from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import *
from rest_framework.viewsets import ModelViewSet

class HududlarViewSet(ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [CustomPermission]

class KompaniyalarViewSet(ModelViewSet):
    queryset = Kompaniya.objects.all()
    serializer_class = KompaniyaSerializer
    permission_classes = [CustomPermission]

class BinolarViewSet(ModelViewSet):
    queryset = Bino.objects.all()
    serializer_class = BinoSerializer
    permission_classes = [CustomPermission]





