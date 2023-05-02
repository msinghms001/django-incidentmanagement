from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
import uuid
import random
import datetime


def gen_incid_id():

    return f""

class Incidents(models.Model):

    status_opts=(
        ('open','Open'),
        ('in_progress','In progress'),
        ('closed','Closed'),
    )

    priority_opts=(
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    )

    id=models.CharField(
        max_length=9999,
        unique=True,
          primary_key=True,
       
        
    )

    reporter=models.ForeignKey(User,related_name='incidents' ,on_delete=models.CASCADE)

    status=models.CharField(

        choices=status_opts,
        max_length=9999,
        default='open'
        
    )

    priority=models.CharField(
        choices=priority_opts,
        max_length=9999,
        default='low'
    )

    details=models.TextField(
        default='',

    )

    reportedOn=models.DateTimeField(
        auto_now_add=True
    )

    updatedOn=models.DateTimeField(
        auto_now=True
    )


    