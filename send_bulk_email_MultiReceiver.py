import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import os

USE_GMAIL = False  # Set True for Gmail, False for Outlook

# Gmail config
GMAIL_EMAIL = "wdgt.wadhwanifoundation@gmail.com"
GMAIL_PASSWORD = "hezs doiy httv ualc"

# Outlook config
OUTLOOK_EMAIL = "wgdt@wadhwanifoundation.org"
OUTLOOK_PASSWORD = "Som37222"

# HTML body of the email
subject = "WGDT Test Email"
html_content = """
<html>
  <body>
    <h2 style="color:green;">Hello from WGDT!</h2>
    <p>This is a <b>bulk email test</b> using <i>for Idea validation APP</i>.</p>
  </body>
</html>
"""

# Read receivers from file
def load_receivers(filename="receivers_email.txt"):
    if not os.path.exists(filename):
        print(f"Receiver file {filename} not found.")
        return []

    with open(filename, "r") as file:
        content = file.read()

    # Remove unwanted characters and split by comma/newline
    emails = [email.strip() for line in content.splitlines() for email in line.split(",")]
    return list(filter(None, emails))  # Remove empty entries


def send_email(server, sender_email, receiver_email, subject, html_body, index):
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = f"{subject} #{index+1}"

    part = MIMEText(html_body, "html")
    msg.attach(part)

    try:
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"[{index+1}] Email sent to {receiver_email}")
    except Exception as e:
        print(f"[{index+1}] Failed to send email to {receiver_email}: {e}")


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

    receivers = load_receivers()
    if not receivers:
        print("No valid receivers found. Exiting.")
        return

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        print("Logged in successfully.")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    for index, receiver_email in enumerate(receivers):
        send_email(server, sender_email, receiver_email, subject, html_content, index)
        time.sleep(1)  # optional delay to avoid rate-limiting

    server.quit()
    print("All emails sent successfully.")


if __name__ == "__main__":
    main()
