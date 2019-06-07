import imapclient
import pyzmail
import re
from info import email,password
i=imapclient.IMAPClient('imap.gmail.com',ssl=True)
print(i.login(email,password))