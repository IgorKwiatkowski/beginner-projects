import json
import urllib.request
import urllib.parse

# x = urllib.request.urlopen('http://www.reddit.com/user/clockwork8.json')
#
# print(x.read())

url = 'https://www.pythonprogramming.net/search'

values = {'q': 'basic', }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)