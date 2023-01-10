#Kirjastot:
import datetime
import sys


#Luokat
class HINTATIEDOT:
    Aika = None
    Hinta = None
    
class ANALYSOIDUTTIEDOT:
    Aika = None
    Hinta = None


def kysyTiedostonNimi(Valinta):
    #Tarkistetaan valinnan avulla, että kysytäänkö kirjoitettavan vai luettavan tiedoston nimi:
    if Valinta == 1:
        TiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    elif Valinta == 3 or Valinta == 4:
        TiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")
        
    return TiedostonNimi

def lueTiedosto(LuettuLista, TiedostonNimi):
    try:
        #Tyhjennetään luettulista:
        LuettuLista.clear()
        
        #Avataan luettava tiedosto:
        Tdsto = open(TiedostonNimi, "r", encoding="UTF-8")
        
        #Luetaan ensmmäinen "Turha rivi":
        Tdsto.readline()[:-1]
        
        #Luetaan tiedoston rivi ja lisätään tiedot olioon ja lopulta lisätään olio listaan:
        Rivi = Tdsto.readline()[:-1]
        while (len(Rivi) > 0): 
            HintaTiedot = HINTATIEDOT()      
            Rivi = Rivi.split(";")
            #Tallennetaan aikatiedot datetime oliona:
            HintaTiedot.Aika = datetime.datetime.strptime(Rivi[0], '"%Y-%m-%d %H:%M:%S"')
            HintaTiedot.Hinta = float(Rivi[1])
            #Lisätään tiedot sisältävä oli luettuun listaan:
            LuettuLista.append(HintaTiedot)
            #Luetaan uusi rivi:
            Rivi = Tdsto.readline()[:-1]
        
        #Tiedoston lukemisen jälkeen suljetaan tiedosto ja ilmoitetaan käyttäjälle, että tiedosto on luettu:
        Tdsto.close()
        Tulosta = "Tiedosto '" + TiedostonNimi + "' luettu."
        print(Tulosta)
        print("")

    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0)
        
    #Palautetaan kutsuvaan funktioon oliolista:
    return LuettuLista


    
def tilastoAnalyysi(LuettuLista, AnalysoituLista):    
    #Luodaan muuttuja halvimman ja kalleimman sähkönhinnan tallentamiseen:
    HalvinHinta = None
    HalvinHintaAika = None
    KalleinHinta = None
    KalleinHintaAika = None
    
    #Kuinka monelta tunnilta tulokset on laskettu:
    AikaVali = len(LuettuLista)
    
    #Luodaan muuttuja johon lasketaan hintojen summa:
    HintojenSumma = 0
    
    #Luetaan oliolistan ensimmäisestä oliosta hinta ja käytetään sitä alustavana halvimpana ja kalleimpana hintana:
    HalvinHinta = LuettuLista[0].Hinta
    KalleinHinta = LuettuLista[0].Hinta
    
    #Etsitään halvin ja kallein hinta ja aika lopuista tiedoista:
    for obj in LuettuLista:
        if obj.Hinta < HalvinHinta:
            HalvinHinta = obj.Hinta
            HalvinHintaAika = obj.Aika
        
        elif obj.Hinta > KalleinHinta:
            KalleinHinta = obj.Hinta
            KalleinHintaAika = obj.Aika   
        
        #Lasketaan hintojen summa:
        HintojenSumma = HintojenSumma + obj.Hinta
        
    #Lasketaan hintojen keskiarvo
    HinnanKeskiarvo = HintojenSumma / len(LuettuLista)
         
    #Luodaan lista johon tallennetaan analysoidut tilastotiedot:
    AnalysoituLista.clear()
    AnalysoituLista = [AikaVali, HalvinHinta, HalvinHintaAika, KalleinHinta, KalleinHintaAika, HinnanKeskiarvo]
    
    return AnalysoituLista




def laskePaivittaisetKeskiarvot(LuettuLista, PavienKeskiarvot):
    #Otetaan luetun listan ensimmäinen päivä laskettavaksi päiväksi:
    LaskettavaPaiva = LuettuLista[0].Aika.date()
    
    #Luodaanmuuttujat summan ja lukujen määrän laskemiseen:
    Summa = 0
    Lukuja = 0
    
    #Luodaan muuttujat päivien lukumäärän laskemiseen:
    PaivienLukumaara = 0
    
    #Tyhjennetään päivien keskiarvot lista ennen sen käyttöä:
    PavienKeskiarvot.clear()
    
    for i in LuettuLista:
        AnalysoidutTiedot = ANALYSOIDUTTIEDOT()
        if i.Aika.date() == LaskettavaPaiva:
            Summa = Summa + i.Hinta
            Lukuja = Lukuja + 1

        elif i.Aika.date() != LaskettavaPaiva:
            Keskiarvo = Summa / Lukuja
            AnalysoidutTiedot.Aika = LaskettavaPaiva
            AnalysoidutTiedot.Hinta = Keskiarvo
            PavienKeskiarvot.append(AnalysoidutTiedot)
                        
            #Alustetaan summa ja luku muuttuja ja muutetaan laskttava päivä:
            Summa = 0
            Lukuja = 0
            LaskettavaPaiva = i.Aika.date()
            
            Summa = Summa + i.Hinta
            Lukuja = Lukuja + 1
            PaivienLukumaara = PaivienLukumaara + 1
    
    #Lasketaan vielä viimeisen päivän tiedot:
    AnalysoidutTiedot = ANALYSOIDUTTIEDOT()
    Keskiarvo = Summa / Lukuja
    AnalysoidutTiedot.Aika = LaskettavaPaiva
    AnalysoidutTiedot.Hinta = Keskiarvo
    
    PavienKeskiarvot.append(AnalysoidutTiedot)
    PaivienLukumaara = PaivienLukumaara + 1
    
    #Ilmoitetaan käyttäjälle, että tiedosto on analysoitu:
    AlkioidenMaara = len(LuettuLista)
    
    print("Tilastotietojen analyysi suoritettu " + str(AlkioidenMaara) + " alkiolle.")
    print("Päivittäiset keskiarvot laskettu " + str(PaivienLukumaara) + " päivälle.")
    print("")
    
    return PavienKeskiarvot



def viikonpaivaAnalyysi(LuettuLista, TulosteLista, Viikonpaivat):
    #Tyhjennetään tulostelista
    TulosteLista.clear()
    
    #Sanakirja, johon tallennetaan viikonpäivien summat ja lukumäärät:
    #Sanakirjan avaimmet ovat viikonpäivä 1 = maanantai, 2 = tiistai, jne. Arvot ovat listoja, joiden ensimmäinen alkio on viikonpäivien lukumäärä ja toinen alkio summa:
    ViikonpaivienLukumaaratJaSummat = {0:[0, 0], 1:[0, 0], 2:[0, 0], 3:[0, 0], 4:[0, 0], 5:[0, 0], 6:[0, 0]}
    
    #Käydään listan alkiot läpi ja lisätään alkioiden hinnat oikeisiin summiin ja lasketaan päivien lukumäärät:
    for i in LuettuLista:
        ViikonpaivienLukumaaratJaSummat[i.Aika.weekday()][0] = ViikonpaivienLukumaaratJaSummat[i.Aika.weekday()][0] + 1
        ViikonpaivienLukumaaratJaSummat[i.Aika.weekday()][1] = ViikonpaivienLukumaaratJaSummat[i.Aika.weekday()][1] + i.Hinta
        
    #Lasketaan pävien keskiarvo ja tallennetaan ne tilapäiseen listaan:
    for i in ViikonpaivienLukumaaratJaSummat:
        Lukumaara = ViikonpaivienLukumaaratJaSummat[i][0]
        Summa = ViikonpaivienLukumaaratJaSummat[i][1]
        
        #Lasketaan keskiarvo:
        if Lukumaara != 0:
            Keskiarvo = Summa / Lukumaara
        else:
            Keskiarvo = 0.0
        
        #Muotoilaan tuloste ja lisätään se listaan:
        Tuloste = "{0};{1}\n".format(Viikonpaivat[i], round(Keskiarvo, 1))
        TulosteLista.append(Tuloste)
     
    #Lisätään tulosteeseen vielä otsikkorivi:
    TulosteLista.insert(0, "Viikonpäivä;Keskimääräinen hinta snt/kWh\n") 
        
    #Tyhjennetään viikonpäivät ja summat sanakirja:
    ViikonpaivienLukumaaratJaSummat.clear()
        
    return TulosteLista



def muotoileTuloste(TilastotiedotLista, PaivittaisetKeskiarvot, TulosteListaEnsimmainenAnalyysi):
    
    #Muotoillaan tulostettava tilastotieto osio:
    TulosteListaEnsimmainenAnalyysi.clear()
    TulosteListaEnsimmainenAnalyysi.append("Analyysin tulokset " + str(TilastotiedotLista[0]) + " tunnilta ovat seuraavat:\n")
    TulosteListaEnsimmainenAnalyysi.append("Sähkön keskihinta oli " + str(round(TilastotiedotLista[5], 1)) + " snt/kWh.\n")
    TulosteListaEnsimmainenAnalyysi.append("Halvimmillaan sähkö oli " + str(round(TilastotiedotLista[1],2)) + " snt/kWh, " + str(TilastotiedotLista[2].strftime("%d.%m.%Y %H:%M")) + ".\n")
    TulosteListaEnsimmainenAnalyysi.append("Kalleimmillaan sähkö oli " + str(round(TilastotiedotLista[3],2)) + " snt/kWh, " + str(TilastotiedotLista[4].strftime("%d.%m.%Y %H:%M")) + ".\n")
    TulosteListaEnsimmainenAnalyysi.append("\n")
    TulosteListaEnsimmainenAnalyysi.append("Päivittäiset keskiarvot (Pvm;snt/kWh):\n")
    
    #lisätään tulostelistaa päivät ja niiden keskiarvot:
    for i in PaivittaisetKeskiarvot:
        Paivamaara = i.Aika.strftime("%d.%m.%Y")
        TulosteListaEnsimmainenAnalyysi.append(str(Paivamaara) + ";" + str(round(i.Hinta ,1)) + "\n")
        
    return TulosteListaEnsimmainenAnalyysi



def kirjoitaTiedosto(TulosteLista, TiedostonNimi):
    try:
        #Avataan kirjoitettava tiedosto:
        Tdsto = open(TiedostonNimi, "w", encoding="UTF-8")
        
        #Kirjoitetaan tiedostoon päivät ja niiden keskiarvot:
        for i in TulosteLista:
            Tdsto.write(i)
        
        #Suljetaan tiedosto:
        Tdsto.close()
        
        #Ilmoitetaan käyttäjälle, että tiedosto on kirjoitettu:
        print("Tiedosto '" + TiedostonNimi + "' kirjoitettu.")
        print("")
    
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(TiedostonNimi))
        sys.exit(0) 
    
    return None
