__author__ = 'S5 (V1S)'

import requests
import xmltodict
from tkinter import *



auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw') #authentication details for logging into the NS-Api
station = input("Over welk station wil je informatie")  #'station' variable will get the same value as the user input.

response = requests.get('http://webservices.ns.nl/ns-api-avt?station=%s' % station , auth=auth_details)
#get information from the api, with the station code from 'station' and with the authentication details.

def schrijf_xml():  #function to write the response from the API into an XML-file.
    bestand = open('testxml', 'w')          #opens the xml file to write.
    bestand.write(str(response.text))       #write the response.
    bestand.close()                         #close the file.

def lees_xml():     #function to read the xml file.
    bestand = open('testxml', 'r')          #opens the xml file to read.
    xml_string = bestand.read()             #make a variable which reads the xml file.
    return xmltodict.parse(xml_string)      #returns the xml file as a dictionary.

schrijf_xml()
api_dict = lees_xml()
keys = []
values = []

for station in api_dict['ActueleVertrekTijden']['VertrekkendeTrein']:   #runs through the xml file
    for x in station:                                                   #runs through every 'VertrekkendeTrein' in the last loop.
        #print(x, station[x])
        keys.append(x)
        values.append(station[x])

for i in values:
    print(i)

window = Tk()

message = Message(window, text= values)
message.pack()
window.mainloop()
