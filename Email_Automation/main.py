import smtplib #talks to email server
from email.message import EmailMessage #helps create email
from config import email_address, email_password


def creating_email(recipient, subject, body):
    msg=EmailMessage() #creating an email
    msg["Subject"]=subject
    msg["From"]= email_address
    msg["To"]= recipient
    msg.set_content(body)
    return msg


def send_email(msg):
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.starttls()
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

def main():
    recipients=[]
    number_of_recipients=int(input("How many people are you sending this email to: "))
    for i in range(number_of_recipients):
        rec=input("Who do you want to email? ")
        recipients.append(rec) 
    subject_of_email=input("Subject: ")
    body_of_email=input("Body: ")



    print(f"You are about to send this email to {len(recipients)} people.")
    print(f"Subject: {subject_of_email}")
    print(f"Body: {body_of_email}")

    confirm = input("Send emails? yes/no: ")
    if confirm.lower()=="yes":
        for rec in recipients:
            message=creating_email(rec,subject_of_email,body_of_email)
            send_email(message)
            print(f"Email has been sent to {rec}")   
    else:
        print("Emails Canceled")
main()
