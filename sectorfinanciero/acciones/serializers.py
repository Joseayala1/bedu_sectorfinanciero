from rest_framework import serializers
from .models import Sector

class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sector
        fields = ('nombre','ticker')
