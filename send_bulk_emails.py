import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# ========== CONFIG ==========

USE_GMAIL = False  # Set to False if using Outlook

# Gmail config
GMAIL_EMAIL = "wdgt.wadhwanifoundation@gmail.com"
GMAIL_PASSWORD = "hezs doiy httv ualc"

# Outlook config
OUTLOOK_EMAIL = "wgdt@wadhwanifoundation.org"
OUTLOOK_PASSWORD = "Som37222"

# Email content
subject = "Test Email"
body = """
<html>
  <body>
    <h2 style="color:blue;">This is a test email</h2>
    <p>This email is sent from a <b>Python Script</b> with <i>HTML formatting</i>.</p>
  </body>
</html>
"""

# Receiver email (can be same or different)
receiver_email = "wdgt.wadhwanifoundation@gmail.com"

# =============================


def send_email(server, sender_email, password, receiver_email, subject, body, index):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = f"{subject} #{index+1}"
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"[{index+1}] Email sent to {receiver_email}")
    except Exception as e:
        print(f"[{index+1}] Failed to send email: {e}")


def main():
    if USE_GMAIL:
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = GMAIL_EMAIL
        password = GMAIL_PASSWORD
    else:
        smtp_server = "smtp.office365.com"
        port = 587
        sender_email = OUTLOOK_EMAIL
        password = OUTLOOK_PASSWORD

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        print("Logged in successfully.")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    for i in range(10):  # Send 10 emails, upgrade this number as much mail you want to send
        send_email(server, sender_email, password, receiver_email, subject, body, i)
        time.sleep(1)  # Optional: avoid triggering spam filters

    server.quit()
    print("All emails sent and connection closed.")


if __name__ == "__main__":
    main()
