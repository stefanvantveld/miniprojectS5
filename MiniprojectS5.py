__author__ = 'S5 (V1S)'

import requests
import xmltodict


auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw')

response = requests.get('http://webservices.ns.nl/ns-api-avt?station=Ut', auth=auth_details)

def schrijf_xml():
    try:
        bestand = open('testxml', 'w')
        try:
            bestand.write(response.text)
            bestand.close()
        except:
            print('Kan bestand niet schrijven')
        finally:
            print('klaar (write)')
    except:
        print('Kan bestand niet openen')
    finally:
        print('klaar')

def lees_xml():
    try:
        bestand = open('testxml', 'r')
        try:
            xml_string = bestand.read()
            return xmltodict.parse(xml_string)
            bestand.close()
        except:
            print('kan bestand niet lezen/verwerken')
        finally:
            print('klaar')
    except:
        print('kan bestand niet openen')
    finally:
        print('klaar (openen)')

schrijf_xml()
api_dict = lees_xml()
print(api_dict['ActueleVertrekTijden']['VertrekkendeTrein'][0])

#print(response.text)

print("Eindelijk gelukt")

print("Waarom is dit niet duidelijk??????")

print("Beter gaat nu niet alles weg of iets")

