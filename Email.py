f = True
import smtplib
#Definitions
def email():
    recipient = str(raw_input("To: "))
    subject = str(raw_input("Subject: "))
    body = str(raw_input("Body: "))
    FROM = user
    
        #Shout out to David Akwii on stackexchange for code on line  - 
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    
        # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    print message
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("Mail sent!")
    except:
        print("Failed to send mail!")
        
        
#Main Start
user = str(raw_input("G-mail username: "))
pwd = str(raw_input("G-mail password: "))
gmail_user = user
gmail_pwd = pwd
print("/email to send email")
while True:
    command = raw_input()
    if command == "/email":
        email()
    else:
        print("Please enter a valid command")
