from django.urls import path,include
from .views import *
app_name='hotel'
urlpatterns = [
    # path('',include('Hotel.urls')),
    path('rooms/',RoomListView.as_view(),name='roomlist_view'),
    path('bookings/',BookingListView.as_view(),name='booking_view'),
    path('detail/<str:category>',RoomDetailView.as_view(),name='room_detail'),
]