from functools import reduce
import operator
import random

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q,F
from django.core import paginator


from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,    
)

from rest_framework.response import Response


from core.models import Incidents
from .import api_serializers
from helpers import helpers

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
                'successMessage':"Login Success."
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
            'data':data,

             'message':{
                    'successCode':status.HTTP_200_OK,
                    'successMessage':'Query completed successfully.',                    
            }    

            
        }

    }, status=status.HTTP_200_OK)


@api_view(['post'])
@permission_classes([IsAuthenticated])
def create(request):

    data=request.data

    serl=api_serializers.UpdatIncidSerl(data=data)
    if serl.is_valid(raise_exception=True):
        serl.save(id=helpers.gen_incid_id(length=5),reporter=request.user,status='open')          

        return Response({
            'error':None,
            'response':{
                'data':serl.data,
                'message':{
                    'successCode':status.HTTP_200_OK,
                    'successMessage':'Created successfully',                    
                }                
            }
        }, status=status.HTTP_200_OK)



    return Response({
        'error':{
            
             'message':{
                'errorCode':status.HTTP_200_OK,
                'errorMessage':'Could not create incident.'
             }
        },
        'response':None

    }, status=status.HTTP_200_OK)


@api_view(['get','post'])
@permission_classes([IsAuthenticated])
def view(request):

    qs=request.user.incidents.all()
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

    inst=request.user.incidents.filter(id=pdata['id'])

    

    if inst.exists():
        if inst[0].status=='closed':

            return Response({
            'error':{            
                'message':{
                    'errorCode':status.HTTP_200_OK,
                'errorMessage':'Closed incident can not be updated.'
             }
            },
            'response':None

        }, status=status.HTTP_200_OK)


        serl=api_serializers.UpdatIncidSerl(data=pdata,instance=inst[0])
        if serl.is_valid():
            serl.save()
            print('done......')   

            return Response({
                'error':None,
                'response':{
                    'data':serl.data,
                    'message':{
                        'successCode':status.HTTP_200_OK,
                        'successMessage':'Incident updated successfully.',
                        
                    }
                }
            }, status=status.HTTP_200_OK)

    return Response({
        'error':{            
             'message':{
                'errorCode':status.HTTP_200_OK,
                'errorMessage':'Could not update incident.'
             }
        },
        'response':None

    }, status=status.HTTP_200_OK)





@api_view(['get','post'])
def land(request):


    return Response({
        'error':None,
        'response':{
            'data':"Incident management api interface",
             'message':{
                'successCode':status.HTTP_200_OK,
                'successMessage':'Query completed successfully.'
             }
        }
    }, status=status.HTTP_200_OK)

