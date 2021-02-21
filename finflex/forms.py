from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime



class booking_form(forms.Form):
    ROOM_TYPES=(('AC','AC'),('NON-AC','NON-AC'))
    type=forms.ChoiceField(choices=ROOM_TYPES,required=True
    )
    check_in=forms.DateTimeField(required=True)
    check_out=forms.DateTimeField(required=True)

class user_registerform(UserCreationForm):
    email=forms.EmailField(required=True)
    class meta:
        model=User
        fields=['username','email','password1','password2']