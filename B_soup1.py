from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')
count = int(input('Enter count:'))
position = int(input('Enter position:')) - 1
html = urlopen(url,context = ctx).read()
s = BeautifulSoup(html,"html.parser")

tags = s('a') #tag you want to search
for i in range(count):
    link = tags[position].get('href',None)
    print(tags[position].contents[0])
    html = urlopen(link).read
    s = BeautifulSoup(html,"html.parser")
    href = soup('a')
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Nadia.html
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# url = input('Enter Url: ')
# count = int(input("Enter count: "))
# position = int(input("Enter position:"))
# for i in range(count):
#     html = urlopen(url).read()
#     soup = BeautifulSoup(html)
#
#     tags = soup('a')
#     s = []
#     t = []
#     for tag in tags:
#         x = tag.get('href', None)
#         s.append(x)
#         y = tag.text
#         t.append(y)
#
#     print(s[position-1])
#     print(t[position-1])
#     url = s[position-1]
