from PIL import Image
import os
from pydub import AudioSegment
import ffmpeg


def foto_omzetter(filename: str, from_format: str, to_format: str):
    if filename.lower().endswith(from_format):
        try:
            with Image.open(filename) as img:
                # Maak bestandsnaam met juiste extensie
                uitvoer_bestandsnaam = filename.split(".")[0] + "." + to_format

                # Sla de foto op in het nieuwe formaat met juiste extensie.
                img.save(os.path.join(uitvoer_bestandsnaam), to_format)

        except Exception as e:
            # Geef error weer voor debugging.
            print(f"Error processing {filename}: {str(e)}")


def muziek_omzetter(filename: str, from_format: str, to_format: str):
    raw_audio = AudioSegment.from_file(f"{filename}", format=from_format)
    raw_audio.export(f"{filename}.{to_format}", format=to_format)


def convert_video(filename, from_format, to_format):
    if filename.lower().endswith(from_format):
        try:
            vid = ffmpeg.input(filename)
            # Change filename to match new extension
            export_filename = filename.split(".")[0] + "." + to_format
            # Save video in new extension
            vid = ffmpeg.output(vid, export_filename)
            vid.run()
        except Exception as e:
            # Geef error weer voor debugging
            print(f"Error processing {filename}: {str(e)}")


# Als de uitvoer_map niet bestaat, maak die dan.
fileType = input("Image, Video or Audio?: ")
input_file = input("Wat is de volledige naam van de file?: ")
extension = input("Wat is de huidige extensie van de file?: ")
expectedExtension = input("Wat is de gewenste extensie?: ")

if fileType == "Image":
    foto_omzetter(input_file, extension, expectedExtension)
elif fileType == "Video":
    convert_video(input_file, extension, expectedExtension)
elif fileType == "Audio":
    muziek_omzetter(input_file, extension, expectedExtension)
else:
    print("We do not support this type of file yet, or u made a typo.")
