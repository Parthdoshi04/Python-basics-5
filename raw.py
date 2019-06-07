import imapclient
from imapclient import IMAPClient
import pyzmail
import re
from info import email
from info import password
i=imapclient.IMAPClient('imap.gmail.com',ssl=True)
print(i.login(email,password))
i.select_folder('INBOX',readonly=True)
list_of_uids=i.search(['SINCE','05-May-2019'])
print("\nList of UIDs:",list_of_uids)
random_message = int(list_of_uids[12])
raw_messages=i.fetch([random_message],[b'BODY[]',b'FLAGS'])
message=pyzmail.PyzMessage.factory(raw_messages[random_message][b'BODY[]'])
print('\nSubject for Email with UID',random_message,':',message.get_subject())
print('Message received from: ', message.get_address('from'))
print('\nMessage contents\n')
content=message.html_part.get_payload().decode(message.html_part.charset)
clean = re.compile('<.*?>')
text = re.sub(clean,'',content)
print(text.strip())
i.logout()