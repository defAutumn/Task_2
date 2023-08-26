from django.core.mail import send_mail
from celery import shared_task
import random
from django.conf import settings

from . import services
from .models import CustomUser
import time
from rest_framework import views, response, exceptions


@shared_task
def send_otp_email(email):
    subject = 'Your account verification email'
    otp = random.randint(100000, 999999)
    message = f'Your OTP is {otp}'
    email_from = 'chromweechannelusa@gmail.com'
    send_mail(subject, message, email_from, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
    return