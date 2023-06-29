import smtplib
from email.message import EmailMessage
def email_alerts(subject,body,to):
    message = EmailMessage()
    message.set_content(body)
    message["subject"] = subject
    message["to"] = to
    
    
    user = "alicemoraaongongo@gmail.com"
    message["from"] = user
    password = "pnwllqfqnbxpreut"
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(message)
    
    server.quit()
if __name__ == "__main__":
    email_alerts("Application for an internship","I hereby write this for my application for an internship.",
                 "moraaalice527@gmail.com") 