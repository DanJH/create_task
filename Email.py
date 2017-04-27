#ALL WORK IS OWN UNLESS MENTIONED
#Referenced documentation throughout however

#-----------Libraries to import---------------
import feedparser, sys, poplib,smtplib, urllib2, getpass
from time import sleep 
#Hey

#---------------Global Variables---------------------
newmail="" #sets empty value for whether there is mail
head="https://" #sets prefix for whether to connect to https or http
where="mail.google.com" #server to connect to
end="/gmail/feed/atom" #path of server to login


#--------Definitions---------------

'''Loading Bar'''
def loading(z):  #Defines function
    print "Connecting", #prints connecting to show progress
    for i in range(z): #Given variable outputs how many periods
        sleep(.1) #Waits .1 second in between . print
        print ". ", #Prints . with no end
        
        
'''Check for new emails'''        
def mailcheck(checker): #Defines function
    ''' 
    Help and reference provided by:
    https://null-byte.wonderhowto.com/how-to/make-gmail-notifier-python-0132845/
    '''
    try: #Tries to if error it won't quit but rather show code
        loading(5)
        mail = int(feedparser.parse(
            head + usr + ":" + pwd + "@" + where + end
        )["feed"]["fullcount"]) 
        #Connects using "https://" + username + ":" + password + "@" + "mail.google.com" + "/gmail/feed/atom" then checks feed and sees if any new mail
        if mail > 0: #If emails that are new are not there, then don't mail
            newmail = 1
        else: #Otherwise it will say no new mail
            newmail = 0
        #If email is new then output message
        if newmail == 1:
            print "\nYou have new mail!" 
    except: #If won't work, will throw code
        print "Cannot connect to email! Check connection, password, and name!"
        
        
'''Reads emails using atom feed'''            
def read():
    mail = int(feedparser.parse(
        head + usr + ":" + pwd + "@" + where + end #This connects to the atom server them returns an integer of the amount of emails
    )["feed"]["fullcount"])
    print mail, " new emails" #Outputs how many emails read
    print(feedparser.parse( #Reads the XML on gmail atom and prints it
        head + usr + ":" + pwd + "@" + where + end
    ))
         
           
'''Sending e-mail to others'''                
def email():
    recip = str(raw_input("To: ")) #Gets the recipient
    sub = str(raw_input("Subject: "))  #Gets the subject
    body = str(raw_input("Body: ")) #Gets the body text
    FROM = user #Uses the user previously asked for to be sent from
    """
    Refernce from David Akwii on stackexchange 
    for code on line 65-79 for help formating email
    """
    
    TO = recip if type(recip) is list else [recip] #If more than one recipient, then it is sent to multiple
    SUBJECT = sub #Variable sub -> SUBJECT
    TEXT = body #Variable body -> TEXT
    
    '''Format for sending'''
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s  
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT) #Formatting message for server to parse
    print message #Shows the message in all before sending
    try:  #Tries to send email, if failed it exits and prints error code
        loading(5) #UI output to show action
        pop_server = smtplib.SMTP("smtp.gmail.com", 587) #Defines where to connect including port
        pop_server.ehlo() #Starts connection to POP server
        pop_server.starttls() #Securely connects to POP
        pop_server.login(user, pwd) #Logs in to POP
        pop_server.sendmail(FROM, TO, message) #Tries to send email with proper format
        pop_server.close() #Closes connection as to save bandwidth
        print "Mail sent!"
    except: #Error exception
        print "Failed to send mail! Check connection, password, and name!" #UI output to try and aid user
          



#-----------------------------Main start------------------------------------

usr = str(raw_input("G-mail username (MUST BE GMAIL ACCOUNT): ")) #Gathers user's username for login
if "@gmail.com" not in usr: #Checks if "@gmail.com" is at end
    user = usr+"@gmail.com" #Adds "@gmail.com" in order to send emails using POP
pwd = str(getpass.getpass("G-mail password: ")) #Gathers user's password for login
print ""   #Line for beauty purposes
mailcheck(1) #Goes to function checking for new mail
print ""  #Line for beauty purposes
print "/help for help" #Outputs help for the user
while True: #Constantly gathers input
    command = raw_input() #Basic constant command input
    if command == "/email":
        email() #If /email typed then it will activate email
    elif command == "/help":
        print "/email for email, /read for reading last 10 emails, /check to check for mail, and /exit to exit"
        #If /help typed it shows list
    elif command == "/read":
        read() #If /read typed it will activate read
    elif command == "/check":
        mailcheck(1) #If /check typed it will activate mail checker
    elif command == "/exit":
        sys.exit() #If /exit typed it quits the program
    else:
        print "Please enter a valid command"
        #In case of something written wrong it returns and gives error code