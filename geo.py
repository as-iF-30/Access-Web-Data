import urllib.request, urllib.parse, urllib.error
import json
url = "http://py4e-data.dr-chuck.net/json?"
address = input("Enter location:")
address_parm = urllib.parse.urlencode({'sensor': 'false','address':address})
link = url + address_parm
print('Retrieving',link)
data = urllib.request.urlopen(url).read()
print('Reterieved', len(data), 'characters')
info = json.loads(data)

# place_id = info["results"][0]["place_id"]
# print("Place ID: ",place_id)
# UW Madison
# South Federal University
