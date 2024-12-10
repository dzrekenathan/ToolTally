import smtplib
from email.mime.text import MIMEText

def test_smtp_connection():
    smtp_host = "smtp.gmail.com"
    smtp_port = 465  # SSL
    sender_email = "dzrekenathan2002@gmail.com"
    sender_password = "uwfjwrtycjmijqqr"  # Replace with your App Password
    receiver_email = "dzrekepokunathan@gmail.com"

    subject = "SMTP Test Email"
    body = "This is a test email sent via SMTP."

    try:
        # Establish SSL connection
        server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        server.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEText(body, "html")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

test_smtp_connection()
