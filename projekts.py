

import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email():

    sender_email = 'pythonproject78@gmail.com'
    sender_password = 'jdxj sdoc ehxy uzdp' 
    recipient_email = input("Ievadiet e-mailu uz kuru gribiet atsutit : ")


    message = MIMEText(input("Ievadiet tekstu, ko gribiet atsutit"))
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = input("Ievadiet temu ")

  
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        
send_email() 