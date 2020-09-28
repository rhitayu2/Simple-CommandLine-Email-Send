# Simple-CommandLine-Email-Send
A Python3 script to automate the process of sending emails via the SMTP client.
The script can be scaled further to automate the sending of a mail to multiple receipients

## Libraries Required
* smtplib
* email
* getpass
* tkinter

## Usage
* Store the mail body in a `.txt` file
* Use the following arguments in the CLI as per use:
  * -M:   To specify the location of the mail body.
  * -T:   To specify the receipient of the mail.
  * -N:   To specify the sender name.
  * -S:   Specify the subject of the email.
* Additionally, prompt on Terminal would specify if user wants to add attachment or not.

## Additional
Additional configuration required for sending through Gmail.
For accounts on Gmail with 2 step authentication, generate app password.
