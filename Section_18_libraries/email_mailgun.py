import requests


MAILGUN_API_URL = 'https://api.mailgun.net/v3/YOURDOMAIN/messages'
MAILGUN_API_KEY = 'XXXXXXXXXXXXXXXXX'

FROM_NAME = 'Gabriel Hernan'
FROM_EMAIL = 'you@yourdomain'

TO_EMAILS = ['mail_1', 'mail_2']
SUBJECT = 'Test e-mail mailgun'


CONTENT = "testing some mailgun!!!"

requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),  # This is basic AUTH
    data={
        'from': f'{FROM_NAME} <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    })
