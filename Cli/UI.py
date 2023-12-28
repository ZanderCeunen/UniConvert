import Core
import os

class Numcheck:
    def picture(number):
        extensies = ["none", "jpeg", "png", "gif", "heic", "heif", "Webp", "bmp", "tiff", "ico"]
        return extensies[number]

    def video(number):
        extensies = []
        return extensies[number]

    def muziek(number):
        extensies = []
        return extensies[number]

def getfilenames():
    print("Hoe wil je de bestanden selecteren?")
    print("""+---------------------------------------------------------------------+
| 1) Neem alle bestanden in de huidige map met de opgegeven extensie. |
+---------------------------------------------------------------------+
| 2) Ik geef zelf de bestand(s)naam(en) in                            |
+---------------------------------------------------------------------+
    """)
    while True:
        keuze_bestandsmethode = int(input("Nummer:"))
        if 3 > keuze_bestandsmethode > 0:
            break
        else:
            print("Dit nummer is geen optie uit de lijst. Probeer opnieuw.")
    if keuze_bestandsmethode == 1:
         return os.listdir(os.path.dirname(os.path.realpath(__file__)))


# Printing ASCII graphics.
print("""                                                                                                                                                                               
  ,----..                                                       ___                        
 /   /   \                                                    ,--.'|_                      
|   :     :  ,---.        ,---,                      __  ,-.  |  | :,'             __  ,-. 
.   |  ;. / '   ,'\   ,-+-. /  |     .---.         ,' ,'/ /|  :  : ' :           ,' ,'/ /| 
.   ; /--` /   /   | ,--.'|'   |   /.  ./|  ,---.  '  | |' |.;__,'  /     ,---.  '  | |' | 
;   | ;   .   ; ,. :|   |  ,"' | .-' . ' | /     \ |  |   ,'|  |   |     /     \ |  |   ,' 
|   : |   '   | |: :|   | /  | |/___/ \: |/    /  |'  :  /  :__,'| :    /    /  |'  :  /   
.   | '___'   | .; :|   | |  | |.   \  ' .    ' / ||  | '     '  : |__ .    ' / ||  | '    
'   ; : .'|   :    ||   | |  |/  \   \   '   ;   /|;  : |     |  | '.'|'   ;   /|;  : |    
'   | '/  :\   \  / |   | |--'    \   \  '   |  / ||  , ;     ;  :    ;'   |  / ||  , ;    
|   :    /  `----'  |   |/         \   \ |   :    | ---'      |  ,   / |   :    | ---'     
 \   \ .'           '---'           '---" \   \  /             ---`-'   \   \  /           
  `---`                                    `----'                        `----'            """)
print(""" +-+-+-+-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+-+-+
 |k|o|b|i|b|o|y| |&| |Z|a|n|d|e|r|C|e|u|n|e|n|
 +-+-+-+-+-+-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+-+-+ 
""")

print("""+----------+-----------+-----------+---------------+
| 1 video  |  2 Muziek |  3 foto's |  4 documenten |
+----------+-----------+-----------+---------------+""")
while True:
    soort_bestand = int(input("Welk type bestand(en) wil je omzetten? Nummer:"))
    if 5 > soort_bestand > 0:
        break
    else:
        print("Dit is geen geldig nummer van een bestandstype. Probeer opnieuw")

if soort_bestand == 1:
    print("")
elif soort_bestand == 2:
    print("")
elif soort_bestand == 3:
    print("""+--------+--------+--------+
| 1 jpeg | 4 heic | 7 bmp  |
| 2 png  | 5 heif | 8 tiff |
| 3 gif  | 6 Webp | 9 ico  |
+--------+--------+--------+""")
    while True: #zet nummer om in extensie voor de input bestanden.
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
    gekozen_output_formaat_extensie = Numcheck.picture(gekozen_output_formaat_nummer)
    bestanden = getfilenames()
    for filename in bestanden:
        Core.foto_omzetter(filename, gekozen_input_formaat_extensie, gekozen_output_formaat_extensie)

elif soort_bestand == 4:
    print("")
