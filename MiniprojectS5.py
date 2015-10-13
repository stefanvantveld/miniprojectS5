__author__ = 'S5 (V1S)'

import requests
import xmltodict
from tkinter import *

auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw')
station = input("Over welk station wil je informatie")

response = requests.get('http://webservices.ns.nl/ns-api-avt?station=%s' % station , auth=auth_details)

def schrijf_xml():
    bestand = open('testxml', 'w')
    bestand.write(response.text)
    bestand.close()

def lees_xml():
    bestand = open('testxml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

schrijf_xml()
api_dict = lees_xml()
#print(api_dict['ActueleVertrekTijden']['VertrekkendeTrein'])

for station in api_dict['ActueleVertrekTijden']['VertrekkendeTrein']:
    #print(station)
    for x in station:
        print(x , station[x])
window = Tk()
label = Label(window, text = api_dict['ActueleVertrekTijden']['VertrekkendeTrein'])
label.pack()
window.mainloop()
#print(response.text)