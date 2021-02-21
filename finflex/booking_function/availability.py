import datetime
from finflex.models import room,booking
from datetime import tzinfo
import pytz
from pytz import tzinfo
from django.utils import timezone

def check_avail(room,Check_in,Check_out):
    booking_lists=booking.objects.filter(Room=room)
    room_list=[]
    

    
    if booking_lists:
        
            for booking_list in booking_lists:
                if Check_out>Check_in :
                    if (Check_out<booking_list.Check_in and Check_in<booking_list.Check_in) or (booking_list.Check_out<Check_in and booking_list.Check_out<Check_out) :
                        room_list.append(True)
                    else:
                        room_list.append(False)
                
        
            
                
    else:
        room_list.append(True)
    return all(room_list)

