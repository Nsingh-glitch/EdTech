from django.core.mail import send_mail
from django.conf import settings


def send_account_activation_email(email,email_token):
    subject='Your account needs to be verified'
    email_from=settings.EMAIL_HOST_USER
    message=f'Hi,Click on the link to activate the account http://127.0.0.1:8000/users/activate/{email_token}'
    
    send_mail(subject, message , email_from, [email])
