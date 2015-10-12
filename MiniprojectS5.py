__author__ = 'S5 (V1S)'

import requests

auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw')

response = requests.get('http://webservices.ns.nl/ns-api-avt?station=Ut', auth=auth_details)

print(response.text)

print("Eindelijk gelukt")