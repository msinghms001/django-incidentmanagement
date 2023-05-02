from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework import status
from rest_framework.decorators import (
    api_view,
    APIView,
    permission_classes,
    authentication_classes,    
)

from rest_framework.response import Response


from core.models import Incidents
from .import api_serializers
from helpers import helpers

@api_view(['get','post'])
def land(request):

    while True:
        obj=helpers.gen_incid_id(length=5)
        idd=Incidents.objects.filter(id=obj).first()
        if not idd:
            break
        

    Incidents.objects.create(
        id=obj,
        reporter_id=2,
        status='open',
        priority='high',
    )

    data={
        'hi':'ok'
    }

    return Response({
        'error':None,
        'response':data
    }, status=status.HTTP_200_OK)



@api_view(['get','post'])
def signup(request):
    
    
    return Response({
        'error':None,
        'response':{
            'searching':''
            
        }

    }, status=status.HTTP_200_OK)


@api_view(['get','post'])
def search(request,term):

    data=[]
    qs=Incidents.objects.filter(id=term)

    if qs.exists():
        resp=api_serializers.IncidSerl(qs,many=True)
        data=resp.data


    
    return Response({
        'error':None,
        'response':{
            'data':data
            
        }

    }, status=status.HTTP_200_OK)



@api_view(['get','post'])
def view(request):

    qs=Incidents.objects.all()
    resp=api_serializers.IncidSerl(qs,many=True)
    


    return Response({
        'error':None,
        'response':{
            'data':resp.data,
            'message':{
                'successCode':status.HTTP_200_OK,
                'successMessage':'List fetched successfully.',
                
            }
        },
    }, status=status.HTTP_200_OK)


@api_view(['post'])
def update(request):

    pdata=request.data

    '''
    [{"id": "RMG705132023","status": "open", "priority": "high", "details": "helo"}]
    '''
    
    serl=api_serializers.UpdatIncidSerl(data=pdata,many=True)
    if serl.is_valid():
        serl.save(user=User.objects.get(id=2))
        print('done......')
    
    print(serl.errors)

    return Response({
        'error':None,
        'response':{
            'data':None,
            'message':{
                'successCode':status.HTTP_200_OK,
                'successMessage':'List updated successfully.',
                
            }
        }
    }, status=status.HTTP_200_OK)




