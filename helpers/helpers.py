import random,datetime
import string

def gen_incid_id(length=5):

    rand_int="".join(random.sample(string.digits, k=length))

    return f"RMG{str(rand_int)}{str(datetime.datetime.now().year)}"
