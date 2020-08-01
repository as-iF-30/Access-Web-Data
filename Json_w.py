import json
import urllib.request
url = input("Enter location:")
print('Retrieving',url)
data = urllib.request.urlopen(url).read()
print('Reterieved', len(data), 'characters')
info = json.loads(data)
print('Count:',len(info))
t = 0
for i in info['comments']:
    t += int(i['count'])
print('Sum:',t)
# http://py4e-data.dr-chuck.net/comments_354419.json
# http://py4e-data.dr-chuck.net/comments_42.json
