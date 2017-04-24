#Libraries
import poplib
from email import parser
import smtplib
from time import sleep
import sys
import urllib2 #To connect to the website
import feedparser #To disect the xml
from textwrap import wrap #Advanced formatting
#Global Variables
atomfeed = "https://mail.google.com/gmail/feed/atom"

#Definitions

#Loading Bar
def loading(z):
    print "Connecting",
    for i in range(z):
        sleep(.1)
        print ". ",
        
def read():
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user=usr,
        passwd=pwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen(atomfeed)
    return feed.read()
#Sending e-mail to others                

def email():
    recipient = str(raw_input("To: "))
    subject = str(raw_input("Subject: "))
    body = str(raw_input("Body: "))
    FROM = usr
    
    """Shout out to David Akwii on stackexchange 
    for code on line  49-51 for help formating"""
     
    
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    
    #Format for sending
    
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    print message
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(usr, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("Mail sent!")
    except:
        print("Failed to send mail! Check connection, password, and username!")
          
#Main Start
usr = str(raw_input("G-mail username (MUST BE GMAIL ACCOUNT): "))
if "@gmail.com" not in usr:
    usr = usr+"@gmail.com"
pwd = str(raw_input("G-mail password: "))
loading(5)
print("")    
print("/help for help")
while True:
    command = raw_input() #Basic constant command input
    if command == "/email":
        email() #If /email typed then it will activate email send script
    elif command == "/help":
        print("/email for email, /read for reading last 10 emails, and /exit to exit") 
        #If /help typed it shows list
    elif command == "/read":
        read()
    elif command == "/exit":
        sys.exit()
    else:
        print("Please enter a valid command") 
        #In case of something written wrong it returns and gives error code

