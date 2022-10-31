from django.conf import settings
from email.mime.image import MIMEImage

# email sending
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# celery
from celery.utils.log import get_task_logger
from core.celery import app

logger = get_task_logger(__name__)


@app.task(name='send_email_async')
def send_email_async(template, to, cc=None, subject='New Email', email_data=None, **kwargs):
    if not email_data:
        email_data = {}
    email_data['server'] = settings.FRONT_URL
    msg_html = render_to_string(
        template,
        email_data
    )

    msg = EmailMessage(
        subject=subject,
        body=msg_html,
        from_email=settings.SUBSCRIPTION_EMAIL_SENDING,
        to=to,
        cc=cc
    )
    for el in kwargs.get('images', []):
        filename = el.split('/')[-1]
        with open(el, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<{name}>'.format(name=filename))
            img.add_header('Content-Disposition', 'inline', filename=filename)
        msg.attach(img)
    msg.content_subtype = "html"
    msg.send()
