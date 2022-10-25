from django.conf import settings
from django.core.mail import EmailMessage


class GenerateMail(object):
    ERROR = 'error'
    INFO = 'info'
    NOTIFICATION = 'notification'

    @classmethod
    def send_mail(cls, title, content, mail_type=ERROR, to=None):
        if not to and mail_type == cls.ERROR:
            to = settings.ERROR_HANDLER_ADMINS
        elif not to and mail_type == cls.NOTIFICATION:
            to = settings.NOTIFICATION_HANDLER_ADMINS

        if isinstance(content, list):
            content = ''.join(content)
        if isinstance(content, object):
            content = f'{content}'

        assert to, 'Indicate receivers mail properly'
        if isinstance(to, list):
            email = EmailMessage(title, content, to=to)
        else:
            email = EmailMessage(title, content, to=[to])

        email.send()
        return True
