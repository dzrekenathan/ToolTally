import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logging import getLogger
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def send_email(subject: str, body: str, receiver_email: str):
    """
    Sends an email to a receiver

    Args:
        subject: the email subject
        body: the email body
        receiver_email: the email address of the receiver
    """
    logger = getLogger(__name__)
    sender_email = getenv("EMAIL_ACCOUNT")
    sender_password = getenv("EMAIL_PASSWORD")
    mail_server = getenv("SMTP_HOST")
    port = int(getenv("SMTP_PORT"))

    try:
        logger.info("Started email send")

        # Create the email object
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        # Attach the email body
        html_part = MIMEText(body, "html")
        msg.attach(html_part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(mail_server, port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        logger.info("Ended email send")
    except smtplib.SMTPException as smtp_ex:
        logger.error(f"SMTP error: {smtp_ex}")
        raise smtp_ex
    except Exception as ex:
        logger.error(f"Error occurred: {ex}")
        raise ex


# import smtplib
# import ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from logging import getLogger
# from os import getenv

# import mail1
# from dotenv import load_dotenv

# load_dotenv()



# def send_email(subject: str, body: str, receiver_email: str):
#     """
#     Sends an email to a receiver

#     Args:
#         subject: the email subject
#         body: the email body
#     """
#     logger = getLogger(__name__)
#     sender_email = getenv("EMAIL_ACCOUNT")
#     sender_password = getenv("EMAIL_PASSWORD")
#     mail_server = getenv("SMTP_HOST")
#     port = int(getenv("SMTP_PORT"))
#     try:
#         logger.info("Started email send")
#         server = smtplib.SMTP_SSL(mail_server, port)
#         server.login(sender_email, sender_password)

#         server.send_message(
#             subject=subject,
#             text=body,
#             text_html=body,
#             recipients=receiver_email,
#             smtp_host=mail_server,
#             smtp_port=port,
#             sender=sender_email,
#             username=sender_email,
#             password=sender_password,
#         )
#         # mail1.send(
#         #     subject=subject,
#         #     text=body,
#         #     text_html=body,
#         #     recipients=receiver_email,
#         #     smtp_host=mail_server,
#         #     smtp_port=port,
#         #     sender=sender_email,
#         #     username=sender_email,
#         #     password=sender_password,
#         # )
#         logger.info("Ended email send")
#     except Exception as ex:
#         logger.error(ex)
#         raise ex