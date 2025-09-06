# importing smtplib ; for actually sending the email through gmail
import smtplib

# for accessing the gmail 16-digit passcode (more in README.md file)
import os

# importing necessary 'email.mime' modules
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# importing time ; e.g.for time.sleep()
import time


print("Make sure you have read the README.md file!\n")


# List of receivers, receiving the same email
user_input = input("Enter emails separated by commas (e.g. 'email1@gmail.com, email2@gmail.com, ...'): ")
receiverList = [email.strip() for email in user_input.split(",")]

# Your Gmail address :                             

email_input = input("Type in your own Gmail address: ")
sender = email_input.strip().lower()

# Getting password through the os module (more about that included in the README.md file)

password = os.environ.get("GMAIL_APP_PASSWORD")
if password is None:

    # throw error when the variable wasn't set
    raise ValueError("GMAIL_APP_PASSWORD environment variable not set! Exiting..")


# The Subject of the emails
subject = "Hello world :D!"

# Body of the emails
body = "This is the body lol"




# -- Send email here: --

# Loop through the list of receivers
for receiver in receiverList:
    
    ''' 
            Setting new msg variable each time,
            so that it doesn't append the next 
            email address. ------v
    '''

    msg = MIMEMultipart() # <-- here
    

    # Setting subject etc for the Emails
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    
    # Attaching the body
    msg.attach(MIMEText(body, "plain"))
    


    # Sending the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    


    # Wait 5 second before sending next email
    time.sleep(5.0)



# This message gets printed if no errors were thrown:
print("Message(s) sent successfully!")
