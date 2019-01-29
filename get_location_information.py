from geopy.geocoders import Nominatim
import json
from pprint import pprint
import wikipedia

geolocator = Nominatim()
location = geolocator.reverse("47.389169,13.644511")

# print(location.address)
# with open('result.json') as f:
#     data = json.load(f)

data = location.raw

# pprint(data)

print (data["address"]["town"])

ny = wikipedia.page("New York City")
print (ny.content)