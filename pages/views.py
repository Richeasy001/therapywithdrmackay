from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SessionBooking
from datetime import datetime
from django.core.mail import EmailMessage as DjangoEmailMessage  # Correct import

def book_session(request):
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            sender_email = request.POST.get('email')
            location = request.POST.get('location')
            date_str = request.POST.get('date')
            time_str = request.POST.get('time')
            subject = request.POST.get('subject')
            summary = request.POST.get('summary')

            # Convert date and time
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            time_obj = datetime.strptime(time_str, '%H:%M').time()

            # Save booking
            booking = SessionBooking(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=sender_email,
                location=location,
                date=date_obj,
                time=time_obj,
                subject=subject,
                summary=summary
            )
            booking.save()

            # Send confirmation email
            # try:
            #     email = DjangoEmailMessage(
            #         subject='Appointment Confirmation',
            #         body=f"Hi {booking.first_name},\n\n"
            #             f"Your appointment for '{booking.subject}' is confirmed on "
            #             f"{booking.date} at {booking.time}.\n\n"
            #             f"Location: {booking.location}\n\n"
            #             "Thank you!",
            #         from_email=settings.EMAIL_HOST_USER,
            #         to=[sender_email],
            #         reply_to=[sender_email]
            #     )
            # except Exception as e:
            #     print("EMAIL ERROR:", str(e))  # This logs the error to your terminal
            #     return render(request, 'booking.html', {'error': f'Email error: {str(e)}'})


            return redirect('booking-success')

        except ValueError:
            return render(request, 'booking.html', {'error': 'Invalid date or time format.'})
        except Exception as e:
            return render(request, 'booking.html', {'error': f'Error: {str(e)}'})

    return render(request, 'booking.html')



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
