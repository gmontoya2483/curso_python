import requests


class Mailgun:
    MAILGUN_API_URL = 'https://api.mailgun.net/v3/YOURDOMAIN/messages'
    MAILGUN_API_KEY = 'XXXXXXXXXXXXXXXXX'

    FROM_NAME = 'Gabriel Hernan'
    FROM_EMAIL = 'you@yourdomain'

    @classmethod
    def send_email(cls, to_emails, subject, content):
        requests.post(
            cls.MAILGUN_API_URL,
            auth=('api', cls.MAILGUN_API_KEY),  # This is basic AUTH
            data={
                'from': f'{cls.FROM_NAME} <{cls.FROM_EMAIL}>',
                'to': to_emails,
                'subject': subject,
                'text': content
            })
