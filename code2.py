from bs4 import BeautifulSoup
s=BeautifulSoup(open("form.html"),('html.parser'))
x=s.find('div',class_="First")
print(x)
print(x.p)
print(x.p.a)
for link in s.find_all('a',limit=3):
	print(link.text)
	print(link.get("href"))