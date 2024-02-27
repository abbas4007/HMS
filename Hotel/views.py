from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from Hotel.booking_functions.availability import check_availability
from .forms import AvailabilityForm
from .models import *
# Create your views here.
class RoomListView(View):
    def get(self,request):
        rooms = Room.objects.all()
        return render(request,'Hotel/room_list_view.html',{'rooms':rooms})

class BookingView(View):
    def get(self,request):
        booking = Booking.objects.all()
        return render(request,'booking_list_view.html',{'booking':booking})


class RoomDetailView(View):
    def get(self,request,category):
        room = Room.objects.get(category=category)
        return render(request,'Hotel/room_detail_view.html',{'room':room})

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]

            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')
