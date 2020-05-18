import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']='Siddhant Agarwal'
email['to']='siddhant235@gmail.com'
email['subject']='I am a Genius!'
email.set_content('I am a Python Master')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("siddhant235@gmail.com","9935846659")
    smtp.send_message(email)
print("DONE")