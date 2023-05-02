from functools import reduce
import operator

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q,F


from rest_framework import status
from rest_framework.permissions import IsAuthenticated
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

import random

@api_view(['post'])
def signup(request):  
    data=request.data 
    email=data.get('email','').strip()
    password=data.get('password','').strip()

    if email and password and not User.objects.filter(email=email).exists():
        uname=email.split('@')[0]+str(random.randint(37,999999))
        inst=User.objects.create_user(email=email,username=uname)
        inst.set_password(password)
        inst.save()
    
    else:       
        return Response({
            'error':{
                "errorMessage":'Not possible'
            },
            'response':None

        }, status=status.HTTP_200_OK)






    return Response({
        'error':None,
        'response':{
            'data':None,
            'message':{
                'successMessage':"Success."
            }
        }

    }, status=status.HTTP_200_OK)



@api_view(['get','post'])

def login(request):

    data=request.data 

    email=data.get('email','').strip()
    password=data.get('password','').strip()

    respData=None

    if email and password and User.objects.filter(email=email.strip()).exists():
        
        inst=User.objects.get(email=email)
        if inst.check_password(password):
            dat=helpers.getToken(inst)
            respData=dat
        
    else:       
        return Response({
            'error':{
                "errorMessage":'Could not login'
            },
            'response':None

        }, status=status.HTTP_200_OK)






    return Response({
        'error':None,
        'response':{
            'data':respData,
            'message':{
                'successMessage':"Success."
            }
        }

    }, status=status.HTTP_200_OK)

@api_view(['get','post'])
def search(request,term):

    data=[]

    items=term.split(',')


    qs=Incidents.objects.filter(reduce(operator.or_,(Q(id__contains=x.strip()) for x in items)))
    

    if qs.exists():
        resp=api_serializers.IncidSerl(qs,many=True)
        data=resp.data


    
    return Response({
        'error':None,
        'response':{
            'items':items,
            'data':data
            
        }

    }, status=status.HTTP_200_OK)


@api_view(['get'])
@permission_classes([IsAuthenticated])
def create(request):

    data=request.data
    

    return Response({
        'error':None,
        'response':{
            'auth':request.user.is_authenticated
            
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




