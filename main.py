from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

GMAIL_SMTP_SERVER = os.getenv("GMAIL_SMTP_SERVER")
GMAIL_SMTP_PORT = os.getenv("GMAIL_SMTP_PORT")
GMAIL_SMTP_SENDER = os.getenv("GMAIL_SMTP_SENDER")
GMAIL_SMTP_PASSWORD = os.getenv("GMAIL_SMTP_PASSWORD")


def main():
    message = MIMEMultipart()
    message['From'] = "Ichika Nagano"
    message['To'] = "oleksandr.savchuk@lasoft.org"
    message['Subject'] = "subject"
    message.attach(MIMEText('Hello from python test app', 'plain'))

    server = smtplib.SMTP(GMAIL_SMTP_SERVER, int(GMAIL_SMTP_PORT))
    server.starttls()
    server.login(GMAIL_SMTP_SENDER, GMAIL_SMTP_PASSWORD)
    response = server.sendmail(GMAIL_SMTP_SENDER, "oleksandr.savchuk@lasoft.org", message.as_string())

    server.quit()
    print(response)


if __name__ == "__main__":
    main()
