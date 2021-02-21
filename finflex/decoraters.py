from. import views
from django.shortcuts import redirect,render
from django.http import HttpResponse
from . models import booking

def dec_admin(func):
    def wrapper(request,*args,**kwargs):
         if request.user.is_staff:
                booking_lists=booking.objects.all()
                return render(request,"finflex/booking_admin.html",{'booking_lists':booking_lists})
         else:
            return func(request,*args,**kwargs)
   
        
    return wrapper