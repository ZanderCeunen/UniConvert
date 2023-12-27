import Core
#printing ASCII graphics
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
    soort_bestand = int(input("Welk type bestand wil je omzetten? Nummer:"))
    if (5 > soort_bestand > 0):
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

elif soort_bestand == 4:
    print("")
