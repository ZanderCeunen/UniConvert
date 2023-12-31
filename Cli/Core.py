from PIL import Image
import os
from pydub import AudioSegment
import ffmpeg


def foto_omzetter(filename: str, from_format: str, to_format: str):
    if filename.lower().endswith(from_format):
        try:
            with Image.open(filename) as img:
                # Maak bestandsnaam met juiste extensie
                filename = filename.split("/")[-1]
                uitvoer_bestandsnaam = filename.split(".")[0] + "." + to_format
                if img.mode in ("RGBA", "P"): img = img.convert("RGB")
                # Sla de foto op in het nieuwe formaat met juiste extensie.
                img.save(os.path.join(uitvoer_bestandsnaam))

        except Exception as e:
            # Geef error weer voor debugging.
            print(f"Error processing {filename}: {str(e)}")


def audio_omzetter(filename: str, from_format: str, to_format: str):
    if filename.lower().endswith(from_format):
        try:
            raw_audio = AudioSegment.from_file(f"{filename}", format=from_format)
            # Maak bestandsnaam met juiste extensie
            filename = filename.split("/")[-1]
            uitvoer_bestandsnaam = filename.split(".")[0] + "." + to_format

            # Sla de foto op in het nieuwe formaat met juiste extensie.
            raw_audio.export(uitvoer_bestandsnaam, format=to_format)

        except Exception as e:
            # Geef error weer voor debugging.
            print(f"Error processing {filename}: {str(e)}")


def video_omzetter(filename, from_format, to_format):
    if filename.lower().endswith(from_format):
        try:
            vid = ffmpeg.input(filename)
            # Change filename to match new extension
            filename = filename.split("/")[-1]
            uitvoer_bestandsnaam = filename.split(".")[0] + "." + to_format
            # Save video in new extension
            vid = ffmpeg.output(vid, uitvoer_bestandsnaam)
            vid.run()
        except Exception as e:
            # Geef error weer voor debugging
            print(f"Error processing {filename}: {str(e)}")
