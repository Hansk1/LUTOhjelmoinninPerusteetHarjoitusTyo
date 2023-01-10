######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Hannes Karppinen
# Opiskelijanumero: 491936
# Päivämäärä: 10.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# ----
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py
# eof


import HTPerusKirjasto as kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    Syote = input("Anna valintasi: ")
    Valinta = int(Syote)
    return Valinta


def paaohjelma():
    Valinta = 1
    #Lista johon tallennetaan luetut tiedot:
    LuettuLista = []
    
    #Listat johon tallennetaan ensimmäisen analyysin tulokset:
    TilastoTiedotLista = []
    PaivienKeskiarvot = [] 
    AnalysoituLista = []
    
    #Lista johon on tallennettu viikonpäivät toista analyysia varten:
    Viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
    
    #Listat johon tallennetaan muodoilut listat, jotka ovat kirjoittamista varten valmiina:
    TulosteLista = []
    TulosteListaEnsimmainenAnalyysi = []
    
    #Sanakirja, johon tallennetaan viikonpäivien summat ja lukumäärät:
    
#Ikisilmukka, joka pyörittää valikkoa:
    while (Valinta != 0):
        Valinta = valikko()
        if (Valinta == 1):
            LuettavanTiedostonNimi = kirjasto.kysyTiedostonNimi(Valinta)
            LuettuLista = kirjasto.lueTiedosto(LuettuLista, LuettavanTiedostonNimi)
            
        elif (Valinta == 2):
            if len(LuettuLista) > 0:
                TilastoTiedotLista = kirjasto.tilastoAnalyysi(LuettuLista, AnalysoituLista)
                PaivienKeskiarvot = kirjasto.laskePaivittaisetKeskiarvot(LuettuLista, PaivienKeskiarvot)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
                print("")
            
        elif (Valinta == 3):
            if len(TilastoTiedotLista) and len(PaivienKeskiarvot) > 0:        
                KirjoitettavanTiedostonNimi = kirjasto.kysyTiedostonNimi(Valinta)
                TulosteLista = kirjasto.muotoileTuloste(TilastoTiedotLista, PaivienKeskiarvot, TulosteListaEnsimmainenAnalyysi)
                kirjasto.kirjoitaTiedosto(TulosteLista, KirjoitettavanTiedostonNimi)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
                print("")
                        
        elif (Valinta == 4):
            if len(LuettuLista) > 0:
                KirjoitettavanTiedostonNimi = kirjasto.kysyTiedostonNimi(Valinta)
                TulosteLista = kirjasto.viikonpaivaAnalyysi(LuettuLista, TulosteLista, Viikonpaivat)
                kirjasto.kirjoitaTiedosto(TulosteLista, KirjoitettavanTiedostonNimi)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
                print("")
            
        elif (Valinta == 0):
            print("Lopetetaan.")
            print("")
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print("")  
             
    #Tyhjennetään listat:
    LuettuLista.clear()
    TilastoTiedotLista.clear()    
    PaivienKeskiarvot.clear()
    AnalysoituLista.clear()
    Viikonpaivat.clear()
    TulosteLista.clear()
    TulosteListaEnsimmainenAnalyysi.clear()
    
    print("Kiitos ohjelman käytöstä.")    
    return None
  
paaohjelma()