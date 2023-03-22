from background_task import background
from django.core.mail import send_mail


@background
def send_email():
    """Задача Отправка email"""
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False)