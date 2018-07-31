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




