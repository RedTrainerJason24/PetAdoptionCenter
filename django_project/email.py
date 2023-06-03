from django.core.mail import send_mail
from django.conf import settings
import os

def sendMail(user_data):
  send_mail(
     subject='Inquiry from ' +user_data['fname']+' ' +user_data['lname']+' ('+user_data['email']+')'+' '+user_data['phone'],
     message=user_data['message'],
     from_email=settings.EMAIL_HOST_USER,
     recipient_list=[settings.EMAIL_HOST_USER, user_data['email']],
     fail_silently=True) 
     # auth_user=os.environ['EMAIL_HOST_USER'], 
     # auth_password=os.environ['EMAIL_HOST_PASSWORD'])
  print(user_data)