import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import logging

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

def userinput_function():
    print("Make sure you have read the README.md file!\n")
    slow = False
    try:
        user_input = input("Enter emails separated by commas (e.g. 'email1@gmail.com, email2@gmail.com, ...'): ")
        receiver_list = [email.strip() for email in user_input.split(",")]
        email_input = input("Type in your own Gmail address: ")
        sender = email_input.strip().lower()
    
        subject = input("\nType in your subject: ")
        body = input("\nType in the body of your message (using newline characters works fine): ")
        body = body.encode('utf-8').decode('unicode escape')
        user_input_delay = input("Do you want a longer delay? y/n")
        slow = True if user_input_delay.strip().lower() == "y" else False
    
        return receiver_list, sender, subject, body, slow
    except KeyboardInterrupt:
        print("\n")
        logging.warning("Process interrupted! Exiting..")
        exit()

# -- Send email here: --
def send_emails(receiver_list, sender, subject, body, password, slow = False):
    delay = 5 if slow else 1
    logging.info(f'Using longer delay ? {slow}')

    if  all(not r.strip() for r in receiver_list):
        logging.error("Did not input recipients!! Exiting..")
        exit()
    if "@" not in sender or "." not in sender:
        logging.error("Wrong sender! Exiting..")
        exit()
    if not subject.strip():
        logging.error("No subject context was given!! Exiting..")
        exit()
    
    if not body.strip():
        logging.warning("No body context was given, continue? y/n")
        userinput = input().strip().lower()
        if(userinput == "y"):
            logging.info("Continuing without body..")
        else:
            logging.info("Exiting..")
            exit()
    sent_emails = 0
    failed_emails = 0

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        try:
            server.login(sender, password)
        except smtplib.SMTPAuthenticationError:
            logging.error("Login failed!! Check your email or app password! Exiting..")
            exit()
        except Exception as e:
            logging.error(f"An unexpected error occurred during login: {e}")
            exit()
        for i, receiver in enumerate(receiver_list):
            receiver = receiver.strip().lower()
            if "@" not in receiver or "." not in receiver or receiver == "":
                failed_emails += 1
                logging.warning(f'Could not send Email to {receiver}. Skipping...')
                continue
            remaining = len(receiver_list) - i - 1       
            try:
                sent_atleast_once = True
                msg = MIMEMultipart()
                msg["From"] = sender
                msg["To"] = receiver
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                server.sendmail(sender, receiver, msg.as_string())
                logging.info(f'Sent "{subject}" to {receiver} successfully.')
                logging.info(f'Remaining: {remaining}. Next in {delay} seconds.')
                sent_emails += 1
                time.sleep(delay)
            except Exception as e:
                logging.error(f'Ooops! Something went wrong.. Error: {e}')
                failed_emails += 1
                continue
            except KeyboardInterrupt:
                logging.warning("Process interrupted! Exiting..")
                exit()
     
    logging.info(f'Summary | Sent: {sent_emails} ; Failed: {failed_emails}')




if(__name__ == "__main__"):
    # Getting password through the os module (more about that included in the README.md file)
    password = os.environ.get("GMAIL_APP_PASSWORD")
    if password is None:
        logging.error("GMAIL_APP_PASSWORD environment variable not set!! Please visit the README.md file for setting it up. Exiting..")
        exit()

    receiver_list, sender, subject, body, slow = userinput_function()
    
    
    try: 
        send_emails(receiver_list, sender, subject, body, password, slow)
    except Exception as e:
        logging.error(f'Oooops! Somethin went wrong.. Error: {e}')
        logging.warning("Exiting..")
        exit()

