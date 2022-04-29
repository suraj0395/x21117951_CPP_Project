import email
from email.mime.text import MIMEText
import smtplib

def send_email(email):
    from_email="teamhelpinghands123@gmail.com"
    from_password="Sur@j0395"
    to_email=email

    subject="Helping Hands"
    message="Greetings!, Thank you for contributing to the helping hands community, We appreciate your intrest towards the cause!."

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
    
