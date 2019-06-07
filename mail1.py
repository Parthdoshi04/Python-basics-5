import smtplib
import info
from info import email,password
s = smtplib.SMTP('smtp.gmail.com',587)
print(s.ehlo())
print(s.starttls())
print(s.login(email,password))
print(s.sendmail('parthdoshi244@gmail.com','parthdoshi244@gmail.com','Subject:Whats up!Bhaiyo,this is a test mail written using smtp protocol'))
print(s.quit())
