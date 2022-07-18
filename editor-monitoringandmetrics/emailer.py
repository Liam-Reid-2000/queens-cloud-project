import smtplib
from email.message import EmailMessage

def email_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = "lreid295@gmail.com"
        
    user = "emailercloud@gmail.com"
    msg['from'] = "emailercloud295@gmail.com"
    password = "EmailerCloud123"
        
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
        
    server.quit()

    # https://stackoverflow.com/questions/67951635/how-to-send-email-alert-through-python-if-a-string-is-found-in-a-csv-file
