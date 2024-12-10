from os import getenv

from core.email import send_email
from dotenv import load_dotenv

load_dotenv()


def send_email_verification(receiver_email: str, token: str) -> None:

    url = f"{getenv('VERIFY_EMAIL_URL')}?token={token}"
    sender_email = getenv("EMAIL_ACCOUNT")
    subject = "ToolTally Email Verification"
    html_body = f"""
<html>
  <body>
    <p>Hello,</p>
    <p>Click on this <a href="{url}">Verify Email</a> to verify your email.</p>
    <p>For more information contact: <a href="mailto:{sender_email}">{sender_email}</a></p>
    <p>Best regards,<br>
    The VSA Team</p>
  </body>
</html>
"""
    send_email(subject, html_body, receiver_email)


def send_reset_email(receiver_email: str, token: str) -> None:

    url = f"{getenv('RESET_PASSWORD_URL')}?token={token}"
    sender_email = getenv("EMAIL_ACCOUNT")
    subject = "Tooltally password reset"
    html_body = f"""
<html>
  <body>
    <p>Hello,</p>
    <p>Click on this <a href="{url}">Reset Password</a> to reset your password.</p>
    <p>For more information contact: <a href="mailto:{sender_email}">{sender_email}</a></p>
    <p>Best regards,<br>
    The Tooltally Team</p>
  </body>
</html>
"""
    send_email(subject, html_body, receiver_email)