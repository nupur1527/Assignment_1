import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from email import encoders

def Send_mail(emailbody,RECEIVER_EMAIL):
  
  SENDER_EMAIL = 'nupur.0815@gmail.com'
  SENDER_PASSWORD = 'fskyuycwvrxvlghi'
  SERVER = 'smtp.gmail.com:587'
  SUBJECT = 'Expected Run Modification'

  message = MIMEMultipart("alternative", None, [MIMEText(emailbody, 'html')])
  message['Subject'] = SUBJECT
  message['From'] = SENDER_EMAIL
  message['To'] = RECEIVER_EMAIL

  server = smtplib.SMTP(SERVER)
  server.ehlo()
  server.starttls()
  server.login(SENDER_EMAIL, SENDER_PASSWORD)
  server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL.split(','), message.as_string())
  server.quit()

