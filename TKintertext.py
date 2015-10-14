from tkinter import *
import requests
import xmltodict


Gfont=("arial", 45, "bold")
Buttonfont=("arial", 16)
Buttonfont2=("arial", 11)

def venster2(event):
    Button1.place(x=1000,y=1000)
    Button2.place(x=1000,y=1000)
    Button3.place(x=1000,y=1000)
    Button4.place(x=1000,y=1000)
    Button5.place(x=1000,y=1000)
    NSwelkom.pack_forget()
    foto.place(x=2000,y=2000)
    Button6.place(x=200, y=300)
    Button7.place(x=400, y=300)
    Button8.place(x=599,y=537)

def venster3(event):
    Button6.place(x=1000,y=400)
    Button7.place(x=1000, y=400)
    HuidigStation.pack()
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
    station = "Rotterdam Centraal"  #'station' variable will get the same value as the user input.

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
                VertrekSpoor.append(station[x])
            elif x == 'Vervoerder':
                Vervoerder.append(station[x])
            elif x == 'VertrekVertragingTekst':
                Vertraging.append(station[x])
            else:
                pass



    def OnMouseWheel(event):
        listbox.yview("scroll", event.delta,"units")
        listbox1.yview("scroll",event.delta,"units")
        listbox2.yview("scroll", event.delta,"units")
        listbox3.yview("scroll",event.delta,"units")
        listbox4.yview("scroll", event.delta,"units")
        return "break"


    listbox = Listbox(root)
    listbox1 = Listbox(root)
    listbox2 = Listbox(root)
    listbox3 = Listbox(root)
    listbox4 = Listbox(root)

    for i, k in enumerate(VertrekTijd):
        listbox.insert(i, str(k[11:16]))
        listbox.pack()
        listbox.place(x=40,y=300)
        listbox.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(EindBestemming):
        listbox1.insert(i, str(k))
        listbox1.pack()
        listbox1.place(x=190,y=300)
        listbox1.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(VertrekSpoor):
        listbox2.insert(i, str(k))
        listbox2.pack()
        listbox2.place(x=340,y=300)
        listbox2.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(TreinSoort):
        listbox3.insert(i, str(k))
        listbox3.pack()
        listbox3.place(x=490,y=300)
        listbox3.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(Vervoerder):
        listbox4.insert(i, str(k))
        listbox4.pack()
        listbox4.place(x=640,y=300)
        listbox4.bind("<MouseWheel>", OnMouseWheel)

def venster4(event):
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000, y=1000)
    AnderStation.pack()
    option.pack()
    Button9.pack()

def vensterkeuze(event):
    AnderStation.pack_forget()
    AndereStation.pack()
    option.pack_forget()
    Button9.pack_forget()
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
                VertrekSpoor.append(station[x])
            elif x == 'Vervoerder':
                Vervoerder.append(station[x])
            elif x == 'VertrekVertragingTekst':
                Vertraging.append(station[x])
            else:
                pass

    def OnMouseWheel(event):
        listbox.yview("scroll", event.delta,"units")
        listbox1.yview("scroll",event.delta,"units")
        listbox2.yview("scroll", event.delta,"units")
        listbox3.yview("scroll",event.delta,"units")
        listbox4.yview("scroll", event.delta,"units")
        return "break"


    listbox = Listbox(root)
    listbox1 = Listbox(root)
    listbox2 = Listbox(root)
    listbox3 = Listbox(root)
    listbox4 = Listbox(root)

    for i, k in enumerate(VertrekTijd):
        listbox.insert(i, str(k[11:16]))
        listbox.pack()
        listbox.place(x=40,y=300)
        listbox.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(EindBestemming):
        listbox1.insert(i, str(k))
        listbox1.pack()
        listbox1.place(x=190,y=300)
        listbox1.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(VertrekSpoor):
        listbox2.insert(i, str(k))
        listbox2.pack()
        listbox2.place(x=340,y=300)
        listbox2.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(TreinSoort):
        listbox3.insert(i, str(k))
        listbox3.pack()
        listbox3.place(x=490,y=300)
        listbox3.bind("<MouseWheel>", OnMouseWheel)

    for i, k in enumerate(Vervoerder):
        listbox4.insert(i, str(k))
        listbox4.pack()
        listbox4.place(x=640,y=300)
        listbox4.bind("<MouseWheel>", OnMouseWheel)
    if var.get() == "Utrecht":
        print ("gelukt")

def reset(event):

    NSwelkom.pack()
    Button1.place(x=50,y=400)
    Button2.place(x=190,y=400)
    Button3.place(x=330,y=400)
    Button4.place(x=470,y=400)
    Button5.place(x=610,y=400)
    Button6.place(x=1000,y=1000)
    Button7.place(x=1000,y=1000)
    foto.pack()
    Button8.place(x=1000,y=1000)
    HuidigStation.pack_forget()
    AnderStation.pack_forget()
    option.pack_forget()
    Button9.pack_forget()
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

def GUI_build():
    global NSwelkom
    global root
    global Button1
    global Button2
    global Button3
    global Button4
    global Button5
    global foto
    global Button6
    global Button7
    global HuidigStation
    global Button8
    global AnderStation
    global option
    global Button9
    global var
    global variabletest
    global Vtijd
    global EBestemming
    global VSpoor
    global TSoort
    global Vvoerder
    global AndereStation


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

    AnderStation = Label(root, height=3, bg="gold", fg="darkblue", text="Selecteer een ander station", font=Gfont)
    AnderStation.pack_forget()

    Button1 = Button(root, wraplength=125, justify=LEFT, text="Ik wil naar Amsterdam",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button1.pack()
    Button1.place(x=50,y=400)

    Button2 = Button(root, wraplength=125, justify=LEFT, text="Kopen los kaartje",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button2.pack()
    Button2.place(x=190,y=400)

    Button3 = Button(root, wraplength=125, justify=LEFT, text="Kopen OV-chipkaart",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button3.pack()
    Button3.place(x=330,y=400)

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
    Button6.place(x=1000,y=1000)

    Button7 = Button(root, wraplength=125, justify=LEFT, text="Info voor ander station",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button7.bind('<Button-1>', venster4)
    Button7.pack()
    Button7.place(x=1000,y=1000)

    OV=PhotoImage(file="ov.png")
    foto = Label(root, image=OV, bg="gold")
    foto.pack()

    bluebar=PhotoImage(file="test.png")
    foto1 = Label(root, image=bluebar, bg="darkblue")
    foto1.pack(side=BOTTOM)

    Button8 = Button(root, wraplength=200, justify=LEFT, text="Terug naar startscherm",bg = "red", fg = "white",font = Buttonfont, width=16)
    Button8.bind('<Button-1>', reset)
    Button8.pack()
    Button8.place(x=1000,y=1000)


    choices = {
    'Amsterdam': 'ASD',
    'Utrecht': 'UT',
    'Rotterdam': 'RD',
    'Alkmaar': 'AMR',
    'Amersfoort': 'AMF',
    'Soest': 'SOT'
        }
    option = OptionMenu(root, var, *choices)
    var.set('Amsterdam')
    option.pack_forget()

    Button9 = Button(root, wraplength=125, justify=LEFT, text="bevestig",bg = "darkblue", fg = "white",font = Buttonfont, width=10)
    Button9.bind('<Button-1>', vensterkeuze)
    Button9.pack()
    Button9.place(x=1000,y=1000)


    root.mainloop()
GUI_build()