from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from pages.models import SessionBooking
from django.core.paginator import Paginator 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')



@require_POST
def contact_form_submit(request):
    name = request.POST.get('name')
    sender_email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    try:
        email = EmailMessage(
        subject=f"TherapiWithDrMakay-{name} {subject}",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
        reply_to=[sender_email])
        email.send()
        messages.success(request, "Your message has been sent successfully. A member of our team will respond as soon as possible.")
        return HttpResponse(status=200)  # Success - nothing else returned
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

@login_required
@user_passes_test(lambda u: u.is_staff)
def custom_admin_dashboard(request):
    bookings_list = SessionBooking.objects.all().order_by('-date', '-time')
    paginator = Paginator(bookings_list, 10)  # 10 bookings per page

    page_number = request.GET.get('page')
    bookings = paginator.get_page(page_number)

    return render(request, 'custom_admin/dashboard.html', {'bookings': bookings})



def custom_login(request):
    if request.user.is_authenticated:
        return redirect('custom_admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('custom_admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an admin.')
    return render(request, 'auth/login.html')


@login_required
@user_passes_test(lambda u: u.is_staff)
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff') == 'on'

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            User.objects.create_user(username=username, email=email, password=password, is_staff=is_staff)
            messages.success(request, f'User "{username}" registered successfully.')
            return redirect('register_user')

    return render(request, 'auth/register.html')


    
