from helpers import helpers
from rest_framework import serializers
from core.models import Incidents, gen_incid_id

class IncidSerl(serializers.ModelSerializer):
    reporter=serializers.StringRelatedField()
    class Meta:
        model=Incidents
        fields='__all__'

class UpdatIncidSerl(serializers.ModelSerializer):
    
    class Meta:
        model=Incidents
        fields=['status','priority','details']
    
    # def create(self, validated_data):
    #     inst=Incidents.objects.create(id=helpers.gen_incid_id(length=5),**validated_data)

    #     return inst


