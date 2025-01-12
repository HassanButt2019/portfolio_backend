import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")  # e.g., "smtp.gmail.com"
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Default to 587
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(subject: str, body: str , sender_email:str):
    """Send an email notification."""
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = subject
        # Attach the message body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_RECEIVER, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
