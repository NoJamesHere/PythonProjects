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
send_emails(receiver_list, sender, subject, body, password, slow = False, ignore = False)

- 'receiver_list': e.g. ("email1@email.com, email2@email.com, ...")
- 'sender': your own email address
- 'subject' of the email
- 'body' of the email; aka. the content inside the email
- 'password': your 16-digit google app password
- (optional) 'slow': if slow = True, wait for 5 seconds after every email. Otherwise wait for 1 seconds.
- (optional) 'ignore': if ignore = True, skip the confirmation for sending out empty body, else don't

Example:

### Code explanation:

```python
# importing smtplib ; for actually sending the email through gmail
import smtplib

# for accessing the gmail 16-digit passcode (more in README.md file)
import os

# importing necessary 'email.mime' modules
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# importing time ; e.g.for time.sleep()
import time

# importing the logging module for possible debugging
import logging

# some config settings for the logging module
logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        filename = "debug.log",
        filemode = "a"
    )


# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

# User input when the script is executed instead being imported into another script
def userinput_function():
    print("Make sure you have read the README.md file!\n")
    slow = False
    ignore = False
    try:
        user_input = input("Enter emails separated by commas (e.g. 'email1@gmail.com, email2@gmail.com, ...'): ")

        # strip the input for whitespace and split it into a list
        receiver_list = [email.strip() for email in user_input.split(",")]
        email_input = input("Type in your own Gmail address: ")

        # strip for whitespace and make it case insensitive
        sender = email_input.strip().lower()
    
        subject = input("\nType in your subject: ")
        body = input("\nType in the body of your message (using newline characters works fine): ")

        # encode using utf-8 so newline characters are supported
        body = body.encode('utf-8').decode('unicode escape')
        user_input_delay = input("Do you want a longer delay? y/n")
        slow = True if user_input_delay.strip().lower() == "y" else False
        if not body.strip():
          logging.warning("detected no body, do you want to ignore further warnings regarding this?")
          inputt = input("y/n: ").strip().lower()
          if(inputt in ["y", "yes"]):
            ignore = False
          else:
            ignore = True
          
        return receiver_list, sender, subject, body, slow, ignore

    # Exit clean when CTRL+C is pressed
    except KeyboardInterrupt:
        print("\n")
        logging.warning("Process interrupted! Exiting..")
        exit()

# -- Send email here: --
def send_emails(receiver_list, sender, subject, body, password, slow = False, ignore = False):
    delay = 5 if slow else 1
    logging.info(f'Using longer delay ? {slow}')
    
    # Check for non existent input
    if  all(not r.strip() for r in receiver_list):
        logging.error("Did not input recipients!! Exiting..")
        exit()
    if "@" not in sender or "." not in sender:
        logging.error("Wrong sender! Exiting..")
        exit()
    if not subject.strip():
        logging.error("No subject context was given!! Exiting..")
        exit()
    # Wait for confirmation if theres no body and *ignore* isn't active
    if not body.strip() and not ignore:
        logging.warning("No body context was given, continue? y/n")
        userinput = input().strip().lower()
        if(userinput == "y"):
            logging.info("Continuing without body..")

        else:
            logging.info("Exiting..")
            exit()

    sent_emails = 0
    failed_emails = 0
    
    # Connect to server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        try:
            server.login(sender, password)

        except smtplib.SMTPAuthenticationError:
            logging.error("Login failed!! Check your email or app password! Exiting..")
            exit()

        except Exception as e:
            logging.error(f"An unexpected error occurred during login: {e}")
            exit()
        
        # loop through the receiver list
        for i, receiver in enumerate(receiver_list):
            receiver = receiver.strip().lower()
            
            # if the string is not a valid email, skip it, also log one failed email
            if "@" not in receiver or "." not in receiver or receiver == "":
                failed_emails += 1
                logging.warning(f'Could not send Email to {receiver}. Skipping...')
                continue

            remaining = len(receiver_list) - i - 1
            
            
            try:
                # attach the details for the email
                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = receiver
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                # send
                server.sendmail(sender, receiver, msg.as_string())
                logging.info(f'Sent "{subject}" to {receiver} successfully.')
                logging.info(f'Remaining: {remaining}. Next in {delay} seconds.')
                sent_emails += 1
                time.sleep(delay)

            except Exception as e:
                # if error occurred, log it and also log one failed email
                logging.error(f'Ooops! Something went wrong.. Error: {e}')
                failed_emails += 1
                continue

            except KeyboardInterrupt:
                # again Keyboard Interrupt if user decides to press CTRL+C or whatever
                logging.warning("Process interrupted! Exiting..")
                exit()

    # Small summary at the end
    logging.info(f'Summary | Sent: {sent_emails} ; Failed: {failed_emails}')



# this will be run if the script is being ran directly:
if(__name__ == "__main__"):
    # Getting password through the os module
    password = os.environ.get("GMAIL_APP_PASSWORD")
    if password is None:
        logging.error("GMAIL_APP_PASSWORD environment variable not set!! Please visit the README.md file for setting it up. Exiting..")
        exit()
    
    # get details from the user input
    receiver_list, sender, subject, body, slow, ignore = userinput_function()
    
    # call send_emails() function with the information gotten from the userinput_function()
    try: 
        send_emails(receiver_list, sender, subject, body, password, slow, ignore)
    except Exception as e:
        logging.error(f'Oooops! Somethin went wrong.. Error: {e}')
        logging.warning("Exiting..")
        exit()
```

