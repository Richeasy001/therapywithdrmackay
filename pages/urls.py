from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_session, name='book-session'),
    path('api/booked-timeslots/', views.get_booked_slots, name='booked-timeslots'),
    path('booking-success/', views.booking_success, name='booking-success'),
]