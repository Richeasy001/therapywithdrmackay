from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

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

    
