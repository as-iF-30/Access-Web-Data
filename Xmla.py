import xml.etree.ElementTree as et
import ssl
import urllib.request
l = input("Enter location:")
print('Retrieving',l)
link = urllib.request.urlopen(l).read()
print('Retrieved:'+str(len(link))+" characters")
tree = et.fromstring(link)
c = tree.findall('.//count')
print("Count:"+str(len(c)))
j = 0
for i in c:
    j += int(i.text)
print("Sum:" + str(j))
# http://py4e-data.dr-chuck.net/comments_354418.xml
# http://py4e-data.dr-chuck.net/comments_42.xml
