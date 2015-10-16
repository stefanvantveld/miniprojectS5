from tkinter import *
import requests
import xmltodict
import codecs

# Hiermee geven we een variable een bepaalde font
Gfont=("arial", 45, "bold")
Buttonfont=("arial", 16)
Buttonfont2=("arial", 11)

# Hiermee wordt naar de API van de NS authorisatie aangevraagd doormiddel van een gebruikersnaam en wachtwoord
auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw')

# Deze fuctie is geschreven om een lijst met alle stations en schrijftypes in te vullen in een tuple
def Stations_Lijst():
    antwoord_API = requests.get("http://webservices.ns.nl/ns-api-stations-v2", auth=auth_details) # Dit is de request die je stuurt naar de API en het wordt opgeslagen in de variabele genaamd antwoord_API
    stations_dict = xmltodict.parse(antwoord_API.text)
    global stationlijst                           # dit maakt de lijst_met_stations globaal zodat hij later nog kan worden aangeroepen
    stationlijst = []                          # Dit is de lege set die zo gevuld gaat worden
    global lijst_met_stationcodes
    lijst_met_stationcodes = []
    for i in stations_dict["Stations"]["Station"]:      # Dit is de loop die door alle verzamelde informatie gaat onder de dictionaries ["Stations"]["Station"]
        if (i["Land"]) == "NL":
            stationlijst.append(i["Namen"]["Lang"])      # Dit voegt het station toe aan de tuple
            lijst_met_stationcodes.append(i["Code"])                # Dit is de afkorting van  het station

Stations_Lijst()                          # dit roept de functie aan om de grote tuple van Stations aan te maken

def venster2(event):
    Button1.place(x=9000,y=1000)
    Button2.place(x=9000,y=1000)
    KoopOV.place(x=9000,y=1000)
    Button4.place(x=9000,y=1000)
    Button5.place(x=9000,y=1000)
    foto.place(x=2000,y=2000)
    Button6.place(x=250, y=300)
    Button7.place(x=400, y=300)
    Return.place(x=599,y=537)

def venster3(event):
    Button6.place(x=9000,y=400)
    Button7.place(x=9000, y=400)
    HuidigStation.pack()
    NSwelkom.pack_forget()
    Vtijd.place(x=40,y=250)
    EBestemming.place(x=190,y=250)
    VSpoor.place(x=340,y=250)
    TSoort.place(x=490,y=250)
    Vvoerder.place(x=640,y=250)
    global listbox
    global listbox1
    global listbox2
    global listbox3
    global listbox4
    auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw') #authentication details for logging into the NS-Api
    station = "Utrecht Centraal"  #'station' variable will get the same value as the user input.

    response = requests.get('http://webservices.ns.nl/ns-api-avt?station=%s' % station, auth=auth_details)
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

    #Here I've made all the empty lists.
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

    listbox = Listbox(root)
    listbox1 = Listbox(root)
    listbox2 = Listbox(root)
    listbox3 = Listbox(root)
    listbox4 = Listbox(root)

    for i, k in enumerate(VertrekTijd[:10]):
        listbox.insert(i, str(k[11:16]))
        listbox.pack()
        listbox.place(x=40,y=300)
    for i, k in enumerate(EindBestemming[:10]):
        listbox1.insert(i, str(k))
        listbox1.pack()
        listbox1.place(x=190,y=300)
    for i, k in enumerate(VertrekSpoor[:10]):
        listbox2.insert(i, str(k))
        listbox2.pack()
        listbox2.place(x=340,y=300)
    for i, k in enumerate(TreinSoort[:10]):
        listbox3.insert(i, str(k))
        listbox3.pack()
        listbox3.place(x=490,y=300)
    for i, k in enumerate(Vervoerder[:10]):
        listbox4.insert(i, str(k))
        listbox4.pack()
        listbox4.place(x=640,y=300)

def venster4(event):
    global option
    Button6.place(x=9000,y=1000)
    Button7.place(x=9000, y=1000)
    AnderStation.pack()
    NSwelkom.pack_forget()
    option.pack()
    option.place(x=200,y=295)
    Confirm.pack()
    Confirm.place(x=420,y=290)

def vensterkeuze(event):
    AnderStation.pack_forget()
    AndereStation.pack()
    option.place(x=9000, y=9000)
    Confirm.place(x=9000, y=9000)
    Vtijd.place(x=40,y=250)
    EBestemming.place(x=190,y=250)
    VSpoor.place(x=340,y=250)
    TSoort.place(x=490,y=250)
    Vvoerder.place(x=640,y=250)
    global listbox
    global listbox1
    global listbox2
    global listbox3
    global listbox4
    auth_details = ('stefan.vantveld@student.hu.nl', 'D1TBMhlZz8dkv5FLZC9RgkVflWjntOvmOXHV6mGDoGvLoeGE-SlOfw') #authentication details for logging into the NS-Api
    station = var.get()  #'station' variable will get the same value as the user input.

    response = requests.get('http://webservices.ns.nl/ns-api-avt?station=%s' % station, auth=auth_details)
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

    #Hier worden allemaal lege lijsten aangemaakt
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

    listbox = Listbox(root)
    listbox1 = Listbox(root)
    listbox2 = Listbox(root)
    listbox3 = Listbox(root)
    listbox4 = Listbox(root)

    for i, k in enumerate(VertrekTijd[:10]):
        listbox.insert(i, str(k[11:16]))
        listbox.pack()
        listbox.place(x=40,y=300)
    for i, k in enumerate(EindBestemming[:10]):
        listbox1.insert(i, str(k))
        listbox1.pack()
        listbox1.place(x=190,y=300)
    for i, k in enumerate(VertrekSpoor[:10]):
        listbox2.insert(i, str(k))
        listbox2.pack()
        listbox2.place(x=340,y=300)
    for i, k in enumerate(TreinSoort[:10]):
        listbox3.insert(i, str(k))
        listbox3.pack()
        listbox3.place(x=490,y=300)
    for i, k in enumerate(Vervoerder[:10]):
        listbox4.insert(i, str(k))
        listbox4.pack()
        listbox4.place(x=640,y=300)

def reset(event):
    NSwelkom.pack()
    Button1.place(x=50,y=400)
    Button2.place(x=190,y=400)
    KoopOV.place(x=330,y=400)
    Button4.place(x=470,y=400)
    Button5.place(x=610,y=400)
    Button6.place(x=9000,y=1000)
    Button7.place(x=9000,y=1000)
    foto.pack()
    Return.place(x=9000,y=1000)
    HuidigStation.pack_forget()
    AnderStation.pack_forget()
    option.place(x=9000, y=9000)
    Confirm.place(x=9000, y=9000)
    listbox.place(x=100,y=9000)
    listbox1.place(x=100,y=9000)
    listbox2.place(x=100,y=9000)
    listbox3.place(x=100,y=9000)
    listbox4.place(x=100,y=9000)
    Vtijd.place(x=40,y=9000)
    EBestemming.place(x=40,y=9000)
    VSpoor.place(x=40,y=9000)
    TSoort.place(x=40,y=9000)
    Vvoerder.place(x=40,y=9000)
    AndereStation.pack_forget()
    werkniet.place(x=9000,y=9000)

def GUI_build():
    global NSwelkom
    global root
    global Button1
    global Button2
    global KoopOV
    global Button4
    global Button5
    global foto
    global Button6
    global Button7
    global HuidigStation
    global Return
    global AnderStation
    global option
    global Confirm
    global var
    global variabletest
    global Vtijd
    global EBestemming
    global VSpoor
    global TSoort
    global Vvoerder
    global AndereStation
    global werkniet
    global listbox
    global listbox1
    global listbox2
    global listbox3
    global listbox4

    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry("800x600")
    root.config(bg="gold")

    var = StringVar(root)

    NSwelkom = Label(root, height=3, bg="gold", fg="darkblue", text="Welkom bij de NS", font=Gfont)
    NSwelkom.pack()

    HuidigStation = Label(root, wraplength=500, height=3, bg="gold", fg="darkblue", text="Informatie over station Utrecht", font=Gfont)
    HuidigStation.pack_forget()

    AndereStation = Label(root, wraplength=500, height=3, bg="gold", fg="darkblue", text="Informatie over station" + str(var.get()), font=Gfont)
    AndereStation.pack_forget()

    Vtijd = Label(root, height=3, bg="gold", fg="darkblue", text="Vertrektijd", font=Buttonfont2)
    Vtijd.pack()
    Vtijd.place(x=40,y=9000)

    EBestemming = Label(root, height=3, bg="gold", fg="darkblue", text="EindBestemming", font=Buttonfont2)
    EBestemming.pack()
    EBestemming.place(x=190,y=9000)

    VSpoor = Label(root, height=3, bg="gold", fg="darkblue", text="VertrekSpoor", font=Buttonfont2)
    VSpoor.pack()
    VSpoor.place(x=340,y=9000)

    TSoort = Label(root, height=3, bg="gold", fg="darkblue", text="TreinSoort", font=Buttonfont2)
    TSoort.pack()
    TSoort.place(x=490,y=9000)

    Vvoerder = Label(root, height=3, bg="gold", fg="darkblue", text="Vervoerder", font=Buttonfont2)
    Vvoerder.pack()
    Vvoerder.place(x=640,y=9000)

    AnderStation = Label(root, wraplength=550, height=3, bg="gold", fg="darkblue", text="Selecteer een ander station", font=Gfont)
    AnderStation.pack_forget()

    werkniet = Label(root, text=" Er is geen informatie beschikbaar over stations in het buitenland", font=Buttonfont)
    werkniet.pack()
    werkniet.place(x=9000, y=9001)

    Button1 = Button(root, wraplength=125, justify=LEFT, text="Ik wil naar Amsterdam",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button1.pack()
    Button1.place(x=50,y=400)

    Button2 = Button(root, wraplength=125, justify=LEFT, text="Kopen los kaartje",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button2.pack()
    Button2.place(x=190,y=400)

    KoopOV = Button(root, wraplength=125, justify=LEFT, text="Kopen OV-chipkaart",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    KoopOV.pack()
    KoopOV.place(x=330,y=400)

    Button4 = Button(root, wraplength=125, justify=LEFT, text="naar het buitenland",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button4.pack()
    Button4.place(x=470,y=400)

    Button5 = Button(root, wraplength=125, justify=LEFT, text="Informatie over station",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button5.bind('<Button-1>', venster2)
    Button5.pack()
    Button5.place(x=610,y=400)

    Button6 = Button(root, wraplength=125, justify=LEFT, text="Info voor huidig station",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button6.bind('<Button-1>', venster3)
    Button6.pack()
    Button6.place(x=9000,y=1000)

    Button7 = Button(root, wraplength=125, justify=LEFT, text="Info voor ander station",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button7.bind('<Button-1>', venster4)
    Button7.pack()
    Button7.place(x=9000,y=1000)

    OV=PhotoImage(file="ov.png")
    foto = Label(root, image=OV, bg="gold")
    foto.pack()

    bluebar=PhotoImage(file="test.png")
    foto1 = Label(root, image=bluebar, bg="darkblue")
    foto1.pack(side=BOTTOM)

    Return = Button(root, wraplength=200, justify=LEFT, text="Terug naar startscherm",bg = "red", fg = "white",font = Buttonfont, width=16)
    Return.bind('<Button-1>', reset)
    Return.pack()
    Return.place(x=9000,y=1000)

    option = OptionMenu(root, var, *stationlijst)
    var.set('Amsterdam')
    option.pack_forget()

    Confirm = Button(root, wraplength=125, justify=LEFT, text="bevestig",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Confirm.bind('<Button-1>', vensterkeuze)
    Confirm.pack()
    Confirm.place(x=9000,y=1000)

    root.mainloop()
GUI_build()