from bs4 import BeautifulSoup
import requests
count=0
url = input("Enter a website to extract the URL's form: ")
r=requests.get("https://"+url)
data=r.text
soup = BeautifulSoup(data,'html.parser')
print(soup)
for link in soup.find_all(['h1','h2','h3']):
	print(link)
	count=count+1
print("Total number of headers:",count)