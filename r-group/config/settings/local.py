from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='86mv^0+am3*@p=e%d1rp3q(@1nnm*8s@aee$vr*izd+&kxvp$&')
DEBUG = env.bool('DJANGO_DEBUG', True)