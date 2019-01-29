import requests

headers = {
    'Authorization': 'm1e5enponocicyue9mv8nd4c93ugedwh',
}

params = (
    ('limit', '64'),
    ('rules', 'countrycode=/[AUT/];image=/[yes/];size=/[300x250,320x50,320x480,728x90/]'),
)

#response = requests.get('https://api.mediasmart.io/api/analytics/availability/drilldown/size', headers=headers, params=params)

#response = requests.get('https://api.mediasmart.io/api/analytics/availability/drilldown/size?limit=64&rules=countrycode=\\[AUT\\];image=\\[yes\\];size=\\[300x250,320x50,320x480,728x90\\]', headers=headers)

print (response)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.mediasmart.io/api/analytics/availability/drilldown/size?limit=64&rules=countrycode=\[AUT\];image=\[yes\];size=\[300x250,320x50,320x480,728x90\]', headers=headers)
