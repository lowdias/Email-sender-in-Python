"""
Author: Ilias Kamal
Email: ilias.kamal@gmail.com
Date: March 23, 2023

Description: This script sends an email using Python's smtplib library and Gmail's SMTP server.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up email content
sender_email = "your_email@gmail.com"
receiver_email = "her_email@gmail.com"
subject = "I love you"
body = "A love letter..."
password = "password or app password if 2FA is activated"

# Create a message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Set up SMTP server and send email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent!")
