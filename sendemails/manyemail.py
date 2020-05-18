import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Siddhant Agarwal'
email['to']='siddhant235@gmail.com'
email['subject']='Python Developer'
email.set_content(html.substitute({'name':'tintin'}),'html')
with smtplib.SMTP(host='smtp.gamail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttlss()
    smtp.login('siddhant235@gmail.com','9935446659')
    smtp.send_message(email)
print("done")