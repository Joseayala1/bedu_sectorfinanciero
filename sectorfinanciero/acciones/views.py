from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SectorSerializer
from .models import Sector
# Create your views here.

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
