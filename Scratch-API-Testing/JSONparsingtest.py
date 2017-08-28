"""
https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python#645318
https://scratch.mit.edu/discuss/topic/177546/
"""

import requests
import sys
import json

print(sys.executable)


def GET(url):
    r = requests.get(url)
    return r


## GET Project Details
url = "https://api.scratch.mit.edu/users/djsanosa/projects/169189283"
r = GET(url)
#print(r.headers)
#print(r.content)

j = json.loads(r.content);

h = r.headers;
c= r.content;
print(c);
print(j['title']);

## GET Project Json
url = "http://projects.scratch.mit.edu/internalapi/project/{id}/get/".format(id='169189283')
r = GET(url)
#print(r.headers)
#print(r.content)
