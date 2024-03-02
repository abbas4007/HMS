from django.urls import path,include
from .views import *
app_name='hotel'
urlpatterns = [
    # path('',include('Hotel.urls')),
    path('rooms/',RoomListView.as_view(),name='roomlist_view'),
    path('bookings/',BookingListView.as_view(),name='booking_view'),
    path('booking/cancel/<int:id>',CancelBookingView.as_view(),name = 'CancelBookingView'),    path('detail/<str:category>',RoomDetailView.as_view(),name='room_detail'),
    path('success/',RoomSuccessView.as_view(),name='room_success'),
]