import imaplib
import datetime
from datetime import date
d = date.fromordinal(730920)
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('daniel.j.heidorn@gmail.com', 'Heidorn00')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.
date = (d.strftime("(%d-1)-%b-%Y"))
result, data = mail.uid('search', None, '(SENTSINCE )'.format(date=date))

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
rawemail = data[0][1]
# here's the body, which is raw text of the whole email
# including headers and alternate payloads
print rawemail