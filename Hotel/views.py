from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.
class RoomView(View):
    def get(self,request):
        rooms = Room.objects.all()
        return render(request,'index.html',{'rooms':rooms})

class BookinView(View):
    def get(self,request):
        booking = Booking.objects.all()
        return render(request,'index.html',{'booking':booking})

