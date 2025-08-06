from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
import json
import ssl

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Validate required fields
        if not all([name, email, subject, message]):
            context = {
                'error': True,
                'message': 'Please fill in all required fields.'
            }
            return render(request, 'portfolio/contact.html', context)
        
        # Prepare email content
        email_subject = f"Portfolio Contact: {subject}"
        email_message = f"""
New contact form submission from your portfolio:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio contact form.
        """
        
        try:
            # Send email using smtplib with custom SSL context for macOS
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            import ssl
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = settings.CONTACT_EMAIL
            msg['Subject'] = email_subject
            msg.attach(MIMEText(email_message, 'plain'))
            
            # Create SSL context that works with macOS
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            # Connect and send email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls(context=context)
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                text = msg.as_string()
                server.sendmail(settings.EMAIL_HOST_USER, settings.CONTACT_EMAIL, text)
            
            # Success response
            context = {
                'success': True,
                'message': 'Thank you for your message! I\'ll get back to you soon.'
            }
            
        except BadHeaderError as e:
            context = {
                'error': True,
                'message': 'Invalid header found. Please try again.'
            }
        except Exception as e:
            context = {
                'error': True,
                'message': 'Sorry, there was an error sending your message. Please try again later or contact me directly.'
            }
        
        return render(request, 'portfolio/contact.html', context)
    
    return render(request, 'portfolio/contact.html')