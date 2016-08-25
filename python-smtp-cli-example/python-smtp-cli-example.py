import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get username and password from environment variables
username = os.environ['DOPPLERRELAY_USERNAME']
password = os.environ['DOPPLERRELAY_PASSWORD']

# Relay SMTP service configuration
host = 'smtp.dopplerrelay.com'
port = 587

# Custom data
mailfrom = "you@yourdomain.com"
mailto = "recipient1@example.com"
subject = "Hello from Doppler Relay, Python style!"
text = "Doppler Relay speaks plaintext"
html = "Doppler Relay speaks <b>HTML</b>"

# Send message using smtplib
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = mailfrom
msg['To'] = mailto
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)
s = smtplib.SMTP(host, port)
s.login(username, password)
s.sendmail(mailfrom, mailto, msg.as_string())

s.quit()