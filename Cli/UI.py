import sys
import Core
import os

# Gebruik deze functie om het ingegeven nummer omtezetten in de juiste extensie.
class Numcheck:
    def picture(number):
        # Lijst met ondersteunde extensies maar 0 geen waarden geven.
        extensies = [None, "jpeg", "png", "jpg", "gif", "heic", "webp", "bmp", "tiff", "ico"]
        return extensies[number]

    def video(number):
        extensies = [None,  "mp4", "m4v", "ogv", "webm", "gif", "avi", "mp3", "wmv", "mov", "ts"]
        return extensies[number]

    def audio(number):
        extensies = [None, "mp3", "m4a", "ogg", "wav", "m4p", "raw", "webm", "wmv", "cda"]
        return extensies[number]


def getfilenames():
    print("Hoe wil je de bestanden selecteren?")
    print("""+---------------------------------------------------------------------+
| 1) Neem alle bestanden in de huidige map met de opgegeven extensie. |
+---------------------------------------------------------------------+
| 2) Ik geef zelf de bestand(s)naam(en) in                            |
+---------------------------------------------------------------------+
    """)
    # Vragen welke selectie methoden ze willen gebruiken.
    while True:
        keuze_bestandsmethode = int(input("Nummer:"))
        if 3 > keuze_bestandsmethode > 0:
            break
        else:
            print("Dit nummer is geen optie uit de lijst. Probeer opnieuw.")

    if keuze_bestandsmethode == 1:
        # Alle bestanden toevoegen aan de lijst van de map waar script nu instaat.
         lijst_bestanden = os.listdir(os.path.dirname(sys.executable))
         return lijst_bestanden
    elif keuze_bestandsmethode == 2:
        print("Geef de naam van het bestand(en) als het bestand zich in dezelfde map bevind als de applicatie.")
        print("Anders kan je het volledige pad geven")
        while True:
            #Lijst maken
            lijst_bestanden = []
            # Gebruiker laten toevoegen
            lijst_bestanden += [input("Naam/pad?:")]
            nog = input("Wil je nog bestanden ingeven Y/N?:")
            if nog == "N" or "n":
                break
            else:
                continue
        return lijst_bestanden

# Printing ASCII graphics.
#Greetings

print(""" __    __            __         ______                                                      __     
|  \  |  \          |  \       /      \                                                    |  \    
| $$  | $$ _______   \$$      |  $$$$$$\  ______   _______  __     __   ______    ______  _| $$_   
| $$  | $$|       \ |  \      | $$   \$$ /      \ |       \|  \   /  \ /      \  /      \|   $$ \  
| $$  | $$| $$$$$$$\| $$      | $$      |  $$$$$$\| $$$$$$$\\$$\ /  $$|  $$$$$$\|  $$$$$$ $$$$$$  
| $$  | $$| $$  | $$| $$      | $$   __ | $$  | $$| $$  | $$ \$$\  $$ | $$    $$| $$   \$$ | $$ __ 
| $$__/ $$| $$  | $$| $$      | $$__/  \| $$__/ $$| $$  | $$  \$$ $$  | $$$$$$$$| $$       | $$|  
 \$$    $$| $$  | $$| $$       \$$    $$ \$$    $$| $$  | $$   \$$$    \$$     \| $$        \$$  $$
  \$$$$$$  \$$   \$$ \$$        \$$$$$$   \$$$$$$  \$$   \$$    \$      \$$$$$$$ \$$         \$$$$ 
                                                                                                                                                                                              
+-+-+-+-+-+-+-+-+-+-+- +-+ +-+-+-+-+-+-+-+-+-+-+-+-+
|K|o|b|e|M|o|t|m|a|n|s |&| |Z|a|n|d|e|r|C|e|u|n|e|n|
+-+-+-+-+-+-+-+-+-+-+- +-+ +-+-+-+-+-+-+-+-+-+-+-+-+ 
Kijk op https://github.com/ZanderCeunen/file-converter voor meer info.
""")

print("""Welk type bestanden wil je omzetten?
+----------+----------+-----------+
| 1 Video  |  2 Audio |  3 Foto's |
+----------+----------+-----------+""")
# Welke converter moet worden gebruikt.
while True:
    soort_bestand = int(input("Nummer:"))
    if 5 > soort_bestand > 0:
        break
    else:
        print("Dit is geen geldig nummer van een bestandstype. Probeer opnieuw")

if soort_bestand == 1:
    # Als foto geef de ondersteunde extensies
    print("""+-------+--------+--------+--------+
| 1 mp4 | 4 webm | 7 mp3  | 10 ts |
| 2 m4v | 5 gif  | 8 wmv  |       |
| 3 ogv | 6 avi  | 9 mov  |       |
+-------+--------+--------+--------+""")
    while True:  # Zet nummer om in extensie voor de input bestanden.
        gekozen_input_formaat_nummer = int(input("Welke extensie heeft/hebben het/de invoer bestand(en)? Nummer:"))
        if 10 > gekozen_input_formaat_nummer > 0:
            break
        else:
            print("Dit is geen geldig nummer van een bestandsextensie. Probeer opnieuw")
    gekozen_input_formaat_extensie = Numcheck.video(gekozen_input_formaat_nummer)

    while True:
        gekozen_output_formaat_nummer = int(input("Welke extensie heeft/hebben het/de uitvoer bestand(en)? Nummer:"))
        if 10 > gekozen_output_formaat_nummer > 0:
            break
        else:
            print("Dit is geen geldig nummer van een bestandsextensie. Probeer opnieuw")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.video(gekozen_output_formaat_nummer)
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden:
        Core.video_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)
elif soort_bestand == 2:
    # Als foto geef de ondersteunde extensies
    print("""+-------+-------+--------+
| 1 mp3 | 4 wav | 7 webm |
| 2 m4a | 5 mp3 | 8 msv  |
| 3 ogg | 6 raw | 9 cda  |
+-------+-------+--------+""")
    while True:  # Zet nummer om in extensie voor de input bestanden.
        gekozen_input_formaat_nummer = int(input("Welke extensie heeft/hebben het/de invoer bestand(en)? Nummer:"))
        if 10 > gekozen_input_formaat_nummer > 0:
            break
        else:
            print("Dit is geen geldig nummer van een bestandsextensie. Probeer opnieuw")
    gekozen_input_formaat_extensie = Numcheck.audio(gekozen_input_formaat_nummer)

    while True:
        gekozen_output_formaat_nummer = int(input("Welke extensie heeft/hebben het/de uitvoer bestand(en)? Nummer:"))
        if 10 > gekozen_output_formaat_nummer > 0:
            break
        else:
            print("Dit is geen geldig nummer van een bestandsextensie. Probeer opnieuw")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.audio(gekozen_output_formaat_nummer)
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden:
        Core.audio_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)
elif soort_bestand == 3:
    # Als foto geef de ondersteunde extensies
    print("""+--------+--------+--------+
| 1 jpeg | 4 gif  | 7 bmp  |
| 2 png  | 5 heic | 8 tiff |
| 3 jpg  | 6 webp | 9 ico  |
+--------+--------+--------+""")
    while True: # Zet nummer om in extensie voor de input bestanden.
        gekozen_input_formaat_nummer = int(input("Welke extensie heeft/hebben het/de invoer bestand(en)? Nummer:"))
        if 10 > gekozen_input_formaat_nummer > 0:
            break
        else:
            print("Dit is geen geldig nummer van een bestandsextensie. Probeer opnieuw")
    gekozen_input_formaat_extensie = Numcheck.picture(gekozen_input_formaat_nummer)

    while True:
        gekozen_output_formaat_nummer = int(input("Welke extensie heeft/hebben het/de uitvoer bestand(en)? Nummer:"))
        if 10 > gekozen_output_formaat_nummer > 0:
            break
        else:
            print("Dit is geen geldig nummer van een bestandsextensie. Probeer opnieuw")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.picture(gekozen_output_formaat_nummer)
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden:
        Core.foto_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)

# elif soort_bestand == 4:
    # print("")
