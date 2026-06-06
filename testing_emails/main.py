import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_mail():
    recipients=["jnadagani@gmail.com"]
    sender = os.getenv("EMAIL_ADDRESS", "")
    password = os.getenv("EMAIL_PASSWORD", "")
    
    msg = EmailMessage()
    msg['Subject'] = "Your Daily Update"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg.set_content("This is your automated daily email.")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


if __name__ == "__main__":
    send_mail()
    
    