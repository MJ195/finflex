from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# Room details
class room(models.Model):
    ROOM_TYPES=(('AC','AC'),('NON-AC','NON-AC'))
    No=models.IntegerField()
    Type=models.CharField(max_length=10,choices=ROOM_TYPES)
    Bed=models.IntegerField()

    def __str__(self):
        return "Room No:{} and Room Type is {}".format(self.No,self.Type)
# Bookings details
class booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Room=models.ForeignKey(room,on_delete=models.CASCADE)
    Time=models.DateTimeField(auto_now_add=True,null=True)
    Check_in=models.DateTimeField()
    Check_out=models.DateTimeField()

class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField()
    email=models.EmailField()
    contact_no=models.IntegerField()
    



