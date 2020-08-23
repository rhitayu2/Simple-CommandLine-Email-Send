#!/usr/bin/env python3

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import getpass
import optparse
import sys
# from tkinter import *
from tkinter import filedialog


gmail_host = 'smtp.gmail.com'
gmail_port = 465
email = 'test@gmail.com'

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/home/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    return filename

def password_input():
    print("[!] Enter Sender's Password")
    try:
        password = getpass.getpass()

    except KeyboardInterrupt:
        print("[-] Exiting...")
        sys.exit(1)
    return password

def attach_file():
    filename = browseFiles()
    # filename = input("[!] Enter the name of the file in the directory: ")
    attachment = open(filename, 'rb')
    
    p = MIMEBase('application','octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename = {filename}')
    return p


def main():
    parser = optparse.OptionParser('usage %prog -M <mail_body_file> -T <receipient\'s email> -N <sender_name> -S <mail_subject>')
    parser.add_option('-M', dest='mail_body', type='string', help='specify the mail body')
    parser.add_option('-T', '--to',dest='to_email', type='string', help='The to email')
    parser.add_option('-N', dest='sender_name', type='string', help='specify the sender name')
    parser.add_option('-S', dest='mail_subject', type='string', help='specify the subject of the mail body')

    # Parameters
    (options, args) = parser.parse_args()

    mail_body = options.mail_body
    sender_name = options.sender_name
    mail_subject = options.mail_subject
    to_email = options.to_email

    if to_email is None:
        parser.print_help()
        sys.exit(0)

    if options.mail_body is None:
        print("[*] Sending Default Mail Body")
        mail_body = '/home/norman/Desktop/Projects/automate_mailing/message.txt'

    password = password_input()

    server = smtplib.SMTP_SSL(gmail_host,gmail_port)
    server.login(email,password)


    msg = MIMEMultipart()
    msg['From'] = sender_name
    msg['Subject'] = mail_subject

    with open(mail_body,'r') as f:
        message = f.read()

    msg.attach(MIMEText(message, 'plain'))

    at = input("[!] Attachment (Y/n): ")

    if at == str('Y') or at == str('y'):
        pay_load = attach_file()
        msg.attach(pay_load)

    try:
        mail_text = msg.as_string()
        server.sendmail(email, to_email, mail_text)
    except:
        print("[-] Couldn't Send Email")
        sys.exit(0)

    server.quit()
    print("[+] Email sent")

if __name__ == '__main__':
    main()
