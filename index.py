import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def check_website(url):
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            return True
        else:
            return False
    except:
        return False
    
def send_email(sender_email, password, receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except:
        print("Failed to send the email")


url = "https://kafka.apache.org/"

if not check_website(url):
    sender_email = os.getenv("SENDER_EMAIL")
    subject = "Website is not working"
    body = "The application is on terminated state."
    receiver_email = os.getenv("RECEIVER_EMAIL")
    password = os.getenv("APP_PASSWORD")
    send_email(sender_email, password, receiver_email, subject, body)
else:
    print("Website is up and running")