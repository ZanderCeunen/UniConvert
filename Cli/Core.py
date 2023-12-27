from PIL import Image
import os
from pydub import AudioSegment
from moviepy.editor import *

videoAudioCodex = {
    "mp4": "libx264",
    "ogv": "libtheora",
    "webm": "libvpx",
    "ogg": "libvorbis",
    "mp3": "pcm_s16le",
    "wav": "libvorbis",
    "m4a": "libfdk_aac"
}

def foto_omzetter(invoer_bestandsnaam: str, from_format: str, to_format:str):
    if invoer_bestandsnaam.lower().endswith((from_format)):
        try:
            with Image.open(invoer_bestandsnaam) as img:
                # Maak bestandsnaam met juiste extensie
                uitvoer_bestandsnaam = invoer_bestandsnaam.split(".")[0] + "." + to_format

                # Sla de foto op in het nieuwe formaat met juiste extensie.
                img.save(os.path.join(uitvoer_bestandsnaam), to_format)

        except Exception as e:
            # Geef error weer voor debugging.
            print(f"Error processing {invoer_bestandsnaam}: {str(e)}")


def muziek_omzetter(filename: str, from_format: str, to_format: str):
    raw_audio = AudioSegment.from_file(f"{filename}+{from_format}", format=from_format)
    raw_audio.export(f"{filename}+{to_format}", format=to_format)

def convert_video(inputFolder, extension):
    # Voor elk bestand in de invoer_map.
    for inputFilename in os.listdir(inputFolder):

        # Filter de foto's uit de bestanden van de invoer_map.
        if inputFilename.lower().endswith(('.mp4', '.webm', '.mov', '.m4v')):
            file_path = os.path.join(inputFolder, inputFilename)
            try:
                with VideoFileClip(file_path) as vid:
                    # Maak bestandsnaam met png in plaats van jpg of jpeg
                    exportFilename = inputFilename.split(".")[0] + "." + extension

                    # Sla de foto op in het PNG-formaat met de nieuwe bestandsnaam.
                    vid.write_videofile(exportFilename, codec=videoAudioCodex[extension])
            except Exception as e:
                # Geef error weer voor debugging
                print(f"Error processing {inputFilename}: {str(e)}")


# Maakt de invoer_map gelijk aan huidige map
invoer_map = os.path.dirname(os.path.realpath(__file__))

# Vraag de gebruiker waar de uitvoer bewaart moet worden en bewaar in uitvoer_map.
uitvoer_map = input("Wat is de uitvoer map: ")

# Ask filetype
fileType = input("Which filetype are you converting? Choose: Image, Video or Audio: ")

# Ask expected filetype
expectedExtension = input("What extension would you like? (Input as 'png'): ")

# Als de uitvoer_map niet bestaat, maak die dan.
if not os.path.exists(uitvoer_map):
    os.makedirs(uitvoer_map)

if fileType == "Image":
    foto_omzetter(invoer_map, uitvoer_map, expectedExtension)
elif fileType == "Video":
    convert_video(invoer_map, expectedExtension)
    pass
elif fileType == "Audio":
    muziek_omzetter(invoer_map, uitvoer_map, expectedExtension)
else:
    print("We do not support this type of file yet, or u made a typo.")
