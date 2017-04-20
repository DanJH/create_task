#Libraries
import poplib
from email import parser
import smtplib
from time import sleep
import sys
    
#Definitions
def read():
    try:
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user(user)
        pop_conn.pass_(pwd)
        messages = [pop_conn.retr(i) for i in range(1, 11)]
        messages = ["\n".join(mssg[1]) for mssg in messages]
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            print message['subject']
            #print message.get_payload()
        pop_conn.quit()
    except:
        print("Failed to recieve mail! Check connection, password, and username!")
        
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
        print("Failed to send mail! Check connection, password, and username!")
        
        
#Main Start
user = str(raw_input("G-mail username (make sure to use @gmail.com): "))
pwd = str(raw_input("G-mail password: "))
print "Connecting",
for i in range(10):
    sleep(.1)
    print ". ",
print("")    
gmail_user = user
gmail_pwd = pwd
print("/help for help")
while True:
    command = raw_input() #Basic constant command input
    if command == "/email":
        email() #If /email typed then it will activate email send script
    elif command == "/help":
        print("/email for email, /read for reading last 10 emails, and /exit to exit") #If /help typed it shows list
    elif command == "/read":
        read()
    elif command == "/exit":
        sys.exit()
    else:
        print("Please enter a valid command") #In case of something written wrong it returns and gives error code

