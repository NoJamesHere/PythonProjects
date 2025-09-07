import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


print("Make sure you have read the README.md file!\n")


user_input = input("Enter emails separated by commas (e.g. 'email1@gmail.com, email2@gmail.com, ...'): ")
receiver_list = [email.strip() for email in user_input.split(",")]
email_input = input("Type in your own Gmail address: ")
sender = email_input.strip().lower()

# Getting password through the os module (more about that included in the README.md file)
password = os.environ.get("GMAIL_APP_PASSWORD")
if password is None:
    raise ValueError("GMAIL_APP_PASSWORD environment variable not set! Exiting..")


subject = input("\nType in your subject: ")
body = input("\nType in the body of your message (using newline characters works fine): ")
body = body.encode('utf-8').decode('unicode_escape')

# -- Send email here: --
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    for receiver in receiver_list:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        server.sendmail(sender, receiver, msg.as_string())
        print(f'Sent "{subject}" to {receiver} successfully.')
        time.sleep(5.0)

print("Message(s) sent successfully!")
