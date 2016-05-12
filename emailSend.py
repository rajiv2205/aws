#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Zabbix SMTP Alert script for gmail.
"""

import sys
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
import logging

# Mail Account
MAIL_ACCOUNT = 'AWS.Alert@blackboxip.com'
MAIL_PASSWORD = 'VbNm1@34'

# Sender Name
SENDER_NAME = u'Zabbix Monitoring System <AWS.Alert@blackboxip.com>'

# Mail Server
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587
# TLS
SMTP_TLS = True

def send_mail(recipient, subject, body, encoding='utf-8'):
    session = None
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = Header(SENDER_NAME, encoding)
    msg['To'] = recipient
    msg['Date'] = formatdate()
    try:
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        if SMTP_TLS:
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(MAIL_ACCOUNT, MAIL_PASSWORD)
        session.sendmail(MAIL_ACCOUNT, recipient, msg.as_string())
    except Exception as e:
        raise e
    finally:
        # close session
        if session:
            session.quit()

if __name__ == '__main__':
    
    if len(sys.argv) == 4:
        recipient=sys.argv[1]
        subject=sys.argv[2]
        body=sys.argv[3]
   
        logmessage="sending email to: "+recipient+" with subject: "+subject+" "
        logging.basicConfig(level=logging.DEBUG, filename="/var/log/zabbix/zabbix_mail.log", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
        logging.info(logmessage)

        send_mail(
            recipient,
            subject,
            body)
    else:
        print u"""requires 3 parameters (recipient, subject, body)
\t$ zabbix-gmail.sh recipient subject body
"""
