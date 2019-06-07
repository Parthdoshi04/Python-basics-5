from bs4 import BeautifulSoup
s=BeautifulSoup(open("form.html"),('html.parser'))
print("Printing with object\n")
print("\n",s)
print("Printing using html\n")
print("\n",s.html)
print("Printing contents within body\n")
print("\n",s.body)
print("prettify htnl file\n")
print("\n",s.prettify())
for tag in s.find_all(True):
	print("\n",tag.name)