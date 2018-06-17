import urllib.request
import json

url = 'https://www.reddit.com/r/python/.json'
resp = urllib.request.urlopen(url).read()

parsed = json.loads(resp.decode('utf-8'))

for item in parsed['data']['children']:
    doc = item['data']
    print(doc['title'])
    print('#comments: %d' % doc['num_comments'])
    print(doc['url'])
    print()
