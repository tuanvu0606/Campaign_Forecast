import json
from pprint import pprint

with open('result.json') as f:
    data = json.load(f)

pprint(data)

print (data["300x250"])