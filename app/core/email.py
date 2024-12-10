import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logging import getLogger
from os import getenv

import mail1
from dotenv import load_dotenv

load_dotenv()



def send_email(subject: str, body: str, receiver_email: str):
    """
    Sends an email to a receiver

    Args:
        subject: the email subject
        body: the email body
    """
    logger = getLogger(__name__)
    sender_email = getenv("EMAIL_ACCOUNT")
    sender_password = getenv("EMAIL_PASSWORD")
    mail_server = getenv("SMTP_HOST")
    port = int(getenv("SMTP_PORT"))
    try:
        logger.info("Started email send")
        mail1.send(
            subject=subject,
            text=body,
            text_html=body,
            recipients=receiver_email,
            smtp_host=mail_server,
            smtp_port=port,
            sender=sender_email,
            username=sender_email,
            password=sender_password,
        )
        logger.info("Ended email send")
    except Exception as ex:
        logger.error(ex)
        raise ex