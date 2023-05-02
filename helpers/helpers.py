import random,datetime
import string

from core.models import Incidents

from rest_framework_simplejwt.tokens import AccessToken,Token,RefreshToken

def getToken(user=None):
    
    token=RefreshToken.for_user(user)

    toks={}
    toks['accessToken']=str(token.access_token)#str(token)
    toks['refreshToken']=str(token)
    return toks

def gen_incid_id(length=5):

    while True:
        rand_int="".join(random.sample(string.digits, k=length))
        obj=f"RMG{str(rand_int)}{str(datetime.datetime.now().year)}"
        idd=Incidents.objects.filter(id=obj).first()
        if not idd:
            break

    return obj
