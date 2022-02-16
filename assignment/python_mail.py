import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from email import encoders
import assgn

SENDER_EMAIL = 'nupur.0815@gmail.com'
SENDER_PASSWORD = 'fskyuycwvrxvlghi'
SERVER = 'smtp.gmail.com:587'
RECEIVER_EMAIL = 'tomar.nupur01@gmail.com'

SUBJECT = 'Expected Run Modification'

def Send_mail():
  message = generate_msg()
  server = smtplib.SMTP(SERVER)
  server.ehlo()
  server.starttls()
  server.login(SENDER_EMAIL, SENDER_PASSWORD)
  server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
  server.quit()

def generate_msg() -> MIMEMultipart:
    message = MIMEMultipart("alternative", None, [MIMEText(assgn.construct_emailbody(), 'html')])
    message['Subject'] = SUBJECT
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    return message


if __name__ == '__main__':
  Send_mail()