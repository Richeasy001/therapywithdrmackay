from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SessionBooking
from .forms import SessionBookingForm
from datetime import datetime


def book_session(request):
    form = SessionBookingForm()
    if request.method == 'POST':
        form = SessionBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking-success')
    return render(request, 'booking.html', {'form': form})


def get_booked_slots(request):
    date_str = request.GET.get('date')
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        bookings = SessionBooking.objects.filter(date=date_obj)
        booked_slots = [booking.time.strftime('%H:%M') for booking in bookings]
        return JsonResponse({'booked_slots': booked_slots})
    except Exception:
        return JsonResponse({'booked_slots': []})


def booking_success(request):
    return render(request, 'booking_success.html')