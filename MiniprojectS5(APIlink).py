__author__ = 'S5 (V1S)'

import codecs
import requests
import xmltodict
import tkinter as tk



auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw') #authentication details for logging into the NS-Api




stationslijst = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=auth_details)
def schrijf_stationlijst():
    bestand = codecs.open('stationinfo', 'w', 'utf-8')
    bestand.write(str(stationslijst.text))
    bestand.close()

def schrijf_xml():  #function to write the response from the API into an XML-file.
    bestand = open('testxml', 'w')          #opens the xml file to write.
    bestand.write(str(response.text))       #write the response.
    bestand.close()                         #close the file.

def lees_xml():     #function to read the xml file.
    bestand = open('testxml', 'r')          #opens the xml file to read.
    xml_string = bestand.read()             #make a variable which reads the xml file.
    return xmltodict.parse(xml_string)      #returns the xml file as a dictionary.

def lees_stationlijst():
    bestand = codecs.open('stationinfo', 'r', 'utf-8')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

schrijf_stationlijst()
stat_dict = lees_stationlijst()

naam = []
code = []

for x in stat_dict['Stations']['Station']:
    for y in x:
        if y == 'Code':
            code.append(x[y])

for x in stat_dict['Stations']['Station']:
    for y in x['Namen']:
        if y == 'Lang':
            naam.append(x['Namen'][y])

print(naam)
input = input('Welke station wil je informatie?')
dekeuze = naam.index(input)
print(code[dekeuze])
station = code[dekeuze]

response = requests.get('http://webservices.ns.nl/ns-api-avt?station=%s' % station , auth=auth_details)
#get information from the api, with the station code from 'station' and with the authentication details.

schrijf_xml()
api_dict = lees_xml()

EindBestemming = []
VertrekTijd= []
RouteTekst = []
RitNummer = []
TreinSoort = []
Vervoerder = []
VertrekSpoor = []
Vertraging = []

for station in api_dict['ActueleVertrekTijden']['VertrekkendeTrein']:   #runs through the xml file
    for x in station:                                                   #runs through every 'VertrekkendeTrein' in the last loop.
        if x == 'EindBestemming':                                       #Check for all the possible branches and saves them in their respective list.
            EindBestemming.append(station[x])
        elif x == 'VertrekTijd':
            VertrekTijd.append(station[x])
        elif x == 'RouteTekst':
            RouteTekst.append(station[x])
        elif x == 'RitNummer':
            RitNummer.append(station[x])
        elif x == 'TreinSoort':
            TreinSoort.append(station[x])
        elif x == 'VertrekSpoor':
            VertrekSpoor.append(station[x]['#text'])
        elif x == 'Vervoerder':
            Vervoerder.append(station[x])
        elif x == 'VertrekVertragingTekst':
            Vertraging.append(station[x])
        else:
            pass

class SimpleGridApp(object):        #This class makes a grid with columns.
    def __init__(self, master, **kwargs):
        self.message = []
        for i, k in enumerate(VertrekTijd[:20]):
            message = tk.Message(root, text=k[11:16], width=200, bg="goldenrod1")
            message.grid(row=i, column=1)
        for i, k in enumerate(EindBestemming[:20]):
            message = tk.Message(root, text=k, width=200, bg='goldenrod1')
            message.grid(row=i, column=2)
        for i, k in enumerate(VertrekSpoor[:20]):
            message = tk.Message(root, text=k, width=200, bg='goldenrod1')
            message.grid(row=i, column=3)
        for i, k in enumerate(TreinSoort[:20]):
            message = tk.Message(root, text=k, width=100, bg='goldenrod1')
            message.grid(row=i, column=4)
        for i, k in enumerate(Vervoerder[:20]):
            message = tk.Message(root, text=k, width=100, bg='goldenrod1')
            message.grid(row=i, column=5)


root = tk.Tk()
root.geometry("800x600")
#root.resizable(width=False, height=False)
root.config(bg="goldenrod1")
app = SimpleGridApp(root, title='Hello, world')
root.mainloop()