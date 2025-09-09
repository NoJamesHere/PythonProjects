Hello! For this to work, you need to set up something for your GMAIL Account for this to actually work
- Activate 2FA
- In the 2FA window, you should see an option for app passwords (if it doesn't appear, wait a few minutes after activating 2FA)
- create an app password, name it whatever you want, and use the 16-digit code as the password in the python script. (without spaces)

---

#### Now we have to set a variable

### In Windows:
Open Start → Environment Variables.

Under User variables, click New….

Variable name: 'GMAIL_APP_PASSWORD'
Variable value: your 16-digit App Password

Click OK and restart any open terminal.

### In Linux:
export GMAIL_APP_PASSWORD="your16digitapp"

# Now run the python script. Happy sending!


---

#### if you wanna use the script as a module, use this function:
send_emails(receiver_list, sender, subject, body, password, slow = False)

- 'receiver_list': e.g. ("email1@email.com, email2@email.com, ...")
- 'sender': your own email address
- 'subject' of the email
- 'body' of the email; aka. the content inside the email
- 'password': your 16-digit google app password
- (optional) 'slow': if slow = True, wait for 5 seconds after every email. Otherwise wait for 1 seconds.
### Code explanation:
Hello! For this to work, you need to set up something for your GMAIL Account for this to actually work
- Activate 2FA
- In the 2FA window, you should see an option for app passwords (if it doesn't appear, wait a few minutes after activating 2FA)
- create an app password, name it whatever you want, and use the 16-digit code as the password in the python script. (without spaces)

---

#### Now we have to set a variable

### In Windows:
Open Start → Environment Variables.

Under User variables, click New….

Variable name: 'GMAIL_APP_PASSWORD'
Variable value: your 16-digit App Password

Click OK and restart any open terminal.

### In Linux:
export GMAIL_APP_PASSWORD="your16digitapp"

# Now run the python script. Happy sending!


---

#### if you wanna use the script as a module, use this function:
send_emails(receiver_list, sender, subject, body, password, slow = False)

- 'receiver_list': e.g. ("email1@email.com, email2@email.com, ...")
- 'sender': your own email address
- 'subject' of the email
- 'body' of the email; aka. the content inside the email
- 'password': your 16-digit google app password
- (optional) 'slow': if slow = True, wait for 5 seconds after every email. Otherwise wait for 1 seconds.
### Code explanation:
´´´python
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
print("Message(s) sent successfully!")´´´
