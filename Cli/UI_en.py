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
        extensies = [None, "mp4", "m4v", "ogv", "webm", "gif", "avi", "mp3", "wmv", "mov"]
        return extensies[number]

    def audio(number):
        extensies = [None, "mp3", "m4a", "ogg", "wav", "m4p", "raw", "webm", "wmv", "cda"]
        return extensies[number]


def getfilenames():
    print("How do you wanna select files?")
    print("""+---------------------------------------------------------------------+
| 1) Take all files in the current folder                             |
+---------------------------------------------------------------------+
| 2) I will give the filenames myself                                 |
+---------------------------------------------------------------------+
    """)
    # Vragen welke selectie methoden ze willen gebruiken.
    while True:
        keuze_bestandsmethode = int(input("Number:"))
        if 3 > keuze_bestandsmethode > 0:
            break
        else:
            print("This number is not a valid option of the list.")

    if keuze_bestandsmethode == 1:
        # Alle bestanden toevoegen aan de lijst van de map waar script nu instaat.
        lijst_bestanden = os.listdir(os.path.dirname(sys.executable))
        return lijst_bestanden
    elif keuze_bestandsmethode == 2:
        print("Give the name of the files if the exe is in the same path.")
        print("Otherwise give the full path like C:/Users/test/Images/1.png")
        while True:
            # Lijst maken
            lijst_bestanden = []
            # Gebruiker laten toevoegen
            lijst_bestanden += [input("Name/path?:")]
            nog = input("Have you another file to convert Y/N?:")
            if nog == "N" or "n":
                break
            else:
                continue
        return lijst_bestanden


# Printing ASCII graphics.
# Greetings

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
Look at https://github.com/ZanderCeunen/file-converter for more information.
""")

print("""Wich type of files would you like to convert?
+----------+----------+-----------+
| 1 Video  |  2 Audio |  3 Foto's |
+----------+----------+-----------+""")
# Welke converter moet worden gebruikt.
while True:
    soort_bestand = int(input("Number:"))
    if 5 > soort_bestand > 0:
        break
    else:
        print("This is not a valid number of a file type. Please try again.")

if soort_bestand == 1:
    # Als foto geef de ondersteunde extensies
    print("""+-------+--------+--------+
| 1 mp4 | 4 webm | 7 m4p  |
| 2 m4v | 5 gif  | 8 wmv  |
| 3 ogv | 6 avi  | 9 mov  |
+-------+--------+--------+""")
    while True:  # Zet nummer om in extensie voor de input bestanden.
        gekozen_input_formaat_nummer = int(input("Which extension has the input file? Number:"))
        if 10 > gekozen_input_formaat_nummer > 0:
            break
        else:
            print("This is not a valid number of an extension. Please try again.")
    gekozen_input_formaat_extensie = Numcheck.video(gekozen_input_formaat_nummer)

    while True:
        gekozen_output_formaat_nummer = int(input("Wich extension needs the output file? Number?:"))
        if 10 > gekozen_output_formaat_nummer > 0:
            break
        else:
            print("This is not a valid number of an extension. Please try again.")
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
        gekozen_input_formaat_nummer = int(input("Which extension has the input file? Number:"))
        if 10 > gekozen_input_formaat_nummer > 0:
            break
        else:
            print("This is not a valid number of an extension. Please try again.")
    gekozen_input_formaat_extensie = Numcheck.audio(gekozen_input_formaat_nummer)

    while True:
        gekozen_output_formaat_nummer = int(input("Wich extension needs the output file? Number?:"))
        if 10 > gekozen_output_formaat_nummer > 0:
            break
        else:
            print("This is not a valid number of an extension. Please try again.")
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
    while True:  # Zet nummer om in extensie voor de input bestanden.
        gekozen_input_formaat_nummer = int(input("Which extension has the input file? Number:"))
        if 10 > gekozen_input_formaat_nummer > 0:
            break
        else:
            print("This is not a valid number of an extension. Please try again.")
    gekozen_input_formaat_extensie = Numcheck.picture(gekozen_input_formaat_nummer)

    while True:
        gekozen_output_formaat_nummer = int(input("Wich extension needs the output file? Number?:"))
        if 10 > gekozen_output_formaat_nummer > 0:
            break
        else:
            print("This is not a valid number of an extension. Please try again.")
    # Zet het nummer om in een extensie.
    gekozen_output_formaat_extensie = Numcheck.picture(gekozen_output_formaat_nummer)
    # Vraag de lijst met bestanden op.
    bestanden = getfilenames()
    # Voor elk bestand in de lijst bijhorende Core converter uitvoeren.
    for filename in bestanden:
        Core.foto_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)