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
