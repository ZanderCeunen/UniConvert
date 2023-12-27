from PIL import Image
import os
from pydub import AudioSegment


def foto_omzetter(invoer_bestandsnaam, uitvoer_map, invoer_map):
    if invoer_bestandsnaam.lower().endswith(('.heic')):
        file_path = os.path.join(invoer_map, invoer_bestandsnaam)
        try:
            with Image.open(file_path) as img:
                # Maak bestandsnaam met jpeg inplaats van
                uitvoer_bestandsnaam = invoer_bestandsnaam.split(".")[0] + ".jpeg"

                # Sla de foto op in het JPEG-formaat met de nieuwe bestandsnaam.
                img.save(os.path.join(uitvoer_map, uitvoer_bestandsnaam), 'JPEG')

        except Exception as e:
            # Geef error weer voor debugging
            print(f"Error processing {invoer_bestandsnaam}: {str(e)}")


    def muziek_omzetter(filename: str, from_format: str, to_format: str):
        raw_audio = AudioSegment.from_file(f"{filename}+{from_format}", format=from_format)
        raw_audio.export(f"{filename}+{to_format}", format=to_format)