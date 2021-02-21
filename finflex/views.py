from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,FormView,DeleteView
from.forms import booking_form
from finflex.booking_function.availability import check_avail
from . models import room,booking
from django.contrib.auth.forms  import UserCreationForm
from django.urls import reverse
from .forms import user_registerform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . decoraters import dec_admin
import datetime
# Create your views here.

class home(LoginRequiredMixin,View):
    login_url="login"
   
    
    def get(self,request):
        form=booking_form()
        return render(request,"finflex/index.html",{"form":form})
    
    
    def post(self,request):
        
        form=booking_form(request.POST)              
        if form.is_valid():            
            data=form.cleaned_data
            room_lists=room.objects.filter(Type=data['type'])
            avail_rooms=[]
            for room_list in room_lists:
                if data['check_out']<data['check_in']:
                    messages.info(request,"Kindly Select valid Input")
                    return render(request,"finflex/index.html")
                if check_avail(room_list,data['check_in'],data['check_out']):
                    avail_rooms.append(room_list)
                    if len(avail_rooms)>0:
                        Room=avail_rooms[0]
                        Booking=booking.objects.create(
                        user=self.request.user,
                        Room=Room,
                        Check_in=data['check_in'],
                        Check_out=data['check_out']
                        )
                        Booking.save()
                        messages.info(request,"Room Booked")
                        return redirect("booking")
                else:
                    messages.info(request,"Room not available for selected room type")
                    return render(request,"finflex/index.html")
        return render(request,"finflex/index.html",{'form':form})
            
            
            
        
        

def user_registeration(request):
    form=user_registerform()
    if request.method=="POST":
        form=user_registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"account was created successfully")
            return redirect("login")
        
    return render(request,"finflex/register.html",{"form":form})

def user_login(request):
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.warning(request,"Username or Password Incorrect")
    
    return render(request,"finflex/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")
@dec_admin
def my_booking(request):
    
    booking_lists=booking.objects.filter(user=request.user)
    return render(request,"finflex/booking.html",{'booking_lists':booking_lists})



def delete_booking (request,pk):
    if request.method=="POST":
        Book=booking.objects.get(id=pk)
        Book.delete()
        return redirect("booking")
    return render(request,"finflex/booking_confirm_delete.html")    

def profile(request):
    today=datetime.datetime.now()
    return render(request,"finflex/profile.html",{'today':today})
class form(FormView):
    form_class=booking_form
    template_name="finflex/form.html"

   