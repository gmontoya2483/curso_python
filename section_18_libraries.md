# Section 18: libraries

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)
* [Libraries overview](#libraries-overview)
* [Using pylint](#using-pylint)
* [Using yapf](#using-yapf)
* [Sending emails with smtplib](#sending-emails-with-smtplib)  
* [Sending emails with Mailgun](#sending-emails-with-mailgun)


## Introduction to this section

[Video: Introduction to this section](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/10057986?start=0)


## libraries overview

[Video: libraries overview](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/10057966?start=0)


## Using pylint

[Video: using pylint](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/10057968?start=0)


## Using yapf

[Video: Using yapf](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/10057970?start=0)


## sending emails with smtplib

```python
"""
If you gt an SMTPAuthenticationError even when yor password is correct,
it is possible that you have 2-factor authentication enabled.
You'll need to use an App Password to log in instead of you normal password

If you don¡t have 2-fa anabled, you will have to allow access by less secure apps in your Gmail security
preferences-thought remember to deactivate it once you've finished learning about sendinge-mails with python
"""

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['Subject'] = 'Test email'
email['From'] = 'from@gmail.com'
email['To'] = 'to@gmail.com'


content = '''Dear Sir/ Madam,

I am sending you an  e-mail with python.

Br,

Me

'''
email.set_content(content)

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('from@gmail.com', 'PASSWORD')

smtp_connector.send_message(email)
smtp_connector.quit()
```

[Video: sending emails with smtplib](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/10057972?start=0)  
[Tutorial: Python - Sending Email using SMTP](https://www.tutorialspoint.com/python/python_sending_email.htm)


## Sending emails with Mailgun

```python
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

```

[Mailgun.com](https://www.mailgun.com)   
[Video: Sending emails with Mailgun](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/10057976?start=0)  
[Mailgun: send message documentation](https://documentation.mailgun.com/en/latest/user_manual.html#sending-messages)  