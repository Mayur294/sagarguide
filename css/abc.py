import json
import urlib.request, urlib.parse, urlib.error

url = 'http://py4e-data.dr-chuck.net/comments_42.json'
uh = urlib.request.urlopen(url)
data = uh.read().decode()
print('retrieved',len(data))

