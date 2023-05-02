
from rest_framework import serializers
from core.models import Incidents

class IncidSerl(serializers.ModelSerializer):
    reporter=serializers.StringRelatedField()
    class Meta:
        model=Incidents
        fields='__all__'

class UpdatIncidSerl(serializers.ModelSerializer):
    
    class Meta:
        model=Incidents
        fields=['status','priority','details']

