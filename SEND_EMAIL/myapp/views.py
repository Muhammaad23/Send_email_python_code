from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']

        # Format the message or subject if needed
        subject = f"Contact Form Submission from {name}"

        # Send email to the user
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],  # Use the user's email here
            fail_silently=False
        )

        return HttpResponse("Email sent successfully!")  # Add feedback for the user

    return render(request, 'index.html')
