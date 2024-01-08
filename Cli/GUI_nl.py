import tkinter as tk
from tkinter import ttk
from customtkinter import *
from tkinter.filedialog import askopenfilenames
import Core
import webbrowser
import os
import sys

def extensionWindow(files, processType):
    ttk.Style().theme_use("vista")
    loadingLabel = tk.Label(window, text="Bestanden worden omgevormd...", font=("Arial", 15), bg="white")
    newExtensionText = tk.Label(text="Wat wordt de nieuwe extensie? (Schrijf als: png)", font=("Arial", 15), bg="white")
    newExtensions = CTkEntry(master=window, font=("Arial", 20), fg_color="white")
    newExtensionEnter = ttk.Button(master=window, text="Bevestig",
                                   command=lambda: [loadingLabel.grid(column=0, row=3, sticky="ew", columnspan=3),
                                                    window.update(),
                                                    type_process(files, newExtensions.get(), processType)],
                                   cursor="hand2")

    imageLabel.grid_remove()
    videoLabel.grid_remove()
    audioLabel.grid_remove()
    imageButton.grid_remove()
    videoButton.grid_remove()
    audioButton.grid_remove()
    typeLabel.grid_remove()
    buttonFrame.grid_remove()

    newExtensionText.grid(column=0, row=2, sticky="w")
    newExtensions.grid(column=1, row=2, sticky="w")
    newExtensionEnter.grid(column=2, row=2, sticky="w")


def type_process(files, newExtension, fileOmzetter):
    for file in files:
        oldExtension = file.split(".")[1]
        fileOmzetter(file, oldExtension, newExtension)
    window.destroy()


def image_clicked():
    files = askopenfilenames(filetypes=[("Image Files", ".jpeg .png, .jpg .gif .heif .webp .bmp .tiff .ico")])
    if files != "":
        extensionWindow(files, Core.foto_omzetter)


def video_clicked():
    files = askopenfilenames(filetypes=[("Video Files", ".mp4 .m4v .ogv .webm .gif .avi .m4p .wmv .mov .tf")])
    if files != "":
        extensionWindow(files, Core.video_omzetter)


def audio_clicked():
    files = askopenfilenames(filetypes=[("Image Files", ".mp3 .m4a .ogg .wav .m4p .raw .m4p .wmv .cda")])
    if files != "":
        extensionWindow(files, Core.audio_omzetter)


def callback(event):
    webbrowser.open_new("https://github.com/ZanderCeunen/UniConvert")


def resource_path(relative_path):
    # get path for retard pyinstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # It's what their docs say
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Window settings
window = tk.Tk()
window.title("Uni-Convert")
window.configure(bg="white")
klein_logo = tk.PhotoImage(file=resource_path("logo_16.png"))
groot_logo = tk.PhotoImage(file=resource_path("logo_32.png"))
window.iconphoto(False, groot_logo, klein_logo)

# Getting screen width and height of display
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# Setting tkinter window size

window.geometry("%dx%d" % (width / 1.8, height / 1.8))
window.resizable()

# Column and row settings
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)

gitFrame = tk.Frame(window, bg="white")
buttonFrame = tk.Frame(window, bg="white")

buttonFrame.grid_columnconfigure(0, weight=1)
buttonFrame.grid_columnconfigure(1, weight=1)
buttonFrame.grid_columnconfigure(2, weight=1)

# Images for buttons
audioPicture = tk.PhotoImage(file=resource_path("Audio.png"))
videoPicture = tk.PhotoImage(file=resource_path("Video.png"))
imagePicture = tk.PhotoImage(file=resource_path("Image.png"))

gitHubPicture = tk.PhotoImage(file=resource_path("GitHub.png"))
gitHubLabel = tk.Label(gitFrame, image=gitHubPicture, bg="white", cursor="hand2")
gitVersion = tk.Label(gitFrame, text="v1.0 stable", bg="white")
gitHubLabel.bind("<Button-1>", callback)

# Create attributes
# Labels
title = tk.Label(window, text="Welcome bij \nUni-Convert!", font=("Arial", 50), bg="white")
typeLabel = tk.Label(text="Welk soort bestand wil je converteren?", font=("Arial", 20), bg="white")

imageLabel = tk.Label(buttonFrame, text="Foto", font=("Arial", 20), bg="white")
videoLabel = tk.Label(buttonFrame, text="Video", font=("Arial", 20), bg="white")
audioLabel = tk.Label(buttonFrame, text="Audio", font=("Arial", 20), bg="white")

# Buttons
imageButton = tk.Button(buttonFrame, image=imagePicture, command=image_clicked, bg="white", border="0",
                        cursor="hand2")
videoButton = tk.Button(buttonFrame, image=videoPicture, command=video_clicked, bg="white", border="0",
                        cursor="hand2")
audioButton = tk.Button(buttonFrame, image=audioPicture, command=audio_clicked, bg="white", border="0",
                        cursor="hand2")

# Grid attributes
gitFrame.grid(column=0, row=0, sticky="w")
gitHubLabel.grid(column=0, row=0)
gitVersion.grid(column=1, row=0)
buttonFrame.grid(column=0, row=3, columnspan=3)
# Grid labels
title.grid(column=0, row=1, columnspan=3)
typeLabel.grid(column=0, row=2, columnspan=3)

# Grid buttons
imageButton.grid(column=0, row=0)
videoButton.grid(column=1, row=0)
audioButton.grid(column=2, row=0)

imageLabel.grid(column=0, row=1)
videoLabel.grid(column=1, row=1)
audioLabel.grid(column=2, row=1)

# Run application
window.mainloop()