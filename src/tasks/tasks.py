import smtplib

from email.message import EmailMessage

from celery import Celery

from src.config import SMTP_USER, SMTP_PASS

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_tamplate_greetings(username: str):
    email = EmailMessage()
    email['Subject'] = 'Thanks for your feedback'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(f'<h1>Thank, {username}!</h1>', subtype='html')

    return email


@celery.task
def send_email_greetings(username: str):
    email = get_email_tamplate_greetings(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
