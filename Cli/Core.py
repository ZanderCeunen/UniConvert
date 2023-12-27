from PIL import Image
import os
from pydub import AudioSegment


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