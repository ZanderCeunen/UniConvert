import tkinter as tk
from tkinter.filedialog import askopenfilenames
import Core


def image_clicked():
    files = askopenfilenames(filetypes=[("Image Files", ".jpeg .png, .jpg .gif .heif .webp .bmp .tiff .ico")])
    newExtensionText = tk.Label(text="What is the new extension? (Write as: png)", font=("Arial", 20))
    newExtensions = tk.Entry(font=("Arial", 20))
    newExtensionEnter = tk.Button(text="Confirm", command=lambda: image_process(files, newExtensions.get()))

    imageLabel.grid_remove()
    videoLabel.grid_remove()
    audioLabel.grid_remove()
    imageButton.grid_remove()
    videoButton.grid_remove()
    audioButton.grid_remove()

    newExtensionText.grid(column=0, row=2, sticky="w")
    newExtensions.grid(column=1, row=2, sticky="w")
    newExtensionEnter.grid(column=2, row=2, sticky="w")


def image_process(files, newExtension):
    for file in files:
        oldExtension = file.split(".")[1]
        Core.foto_omzetter(file, oldExtension, newExtension)
    window.destroy()


def video_clicked():
    files = askopenfilenames(filetypes=[("Video Files", ".mp4 .m4v .ogv .webm .gif .avi .m4p .wmv .mov")])
    newExtensionText = tk.Label(text="What is the new extension? (Write as: png)", font=("Arial", 20))
    newExtensions = tk.Entry(font=("Arial", 20))
    newExtensionEnter = tk.Button(text="Confirm", command=lambda: video_process(files, newExtensions.get()))

    imageLabel.grid_remove()
    videoLabel.grid_remove()
    audioLabel.grid_remove()
    imageButton.grid_remove()
    videoButton.grid_remove()
    audioButton.grid_remove()

    newExtensionText.grid(column=0, row=2, sticky="w")
    newExtensions.grid(column=1, row=2, sticky="w")
    newExtensionEnter.grid(column=2, row=2, sticky="w")


def video_process(files, newExtension):
    for file in files:
        print(file)
        oldExtension = file.split(".")[1]
        Core.video_omzetter(file, oldExtension, newExtension)
    window.destroy()


def audio_clicked():
    files = askopenfilenames(filetypes=[("Image Files", ".mp3 .m4a .ogg .wav .m4p .raw .m4p .wmv .cda")])
    newExtensionText = tk.Label(text="What is the new extension? (Write as: png)", font=("Arial", 20))
    newExtensions = tk.Entry(font=("Arial", 20))
    newExtensionEnter = tk.Button(text="Confirm", command=lambda: audio_process(files, newExtensions.get()))

    imageLabel.grid_remove()
    videoLabel.grid_remove()
    audioLabel.grid_remove()
    imageButton.grid_remove()
    videoButton.grid_remove()
    audioButton.grid_remove()

    newExtensionText.grid(column=0, row=2, sticky="w")
    newExtensions.grid(column=1, row=2, sticky="w")
    newExtensionEnter.grid(column=2, row=2, sticky="w")


def audio_process(files, newExtension):
    for file in files:
        oldExtension = file.split(".")[1]
        Core.audio_omzetter(file, oldExtension, newExtension)
    window.destroy()


# Window settings
window = tk.Tk()
window.title("Uni-Convert")

# Getting screen width and height of display
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# Setting tkinter window size

window.geometry("%dx%d" % (width, height))
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

# Images for buttons
audioPicture = tk.PhotoImage(file="Icon_Images/Audio.png")
videoPicture = tk.PhotoImage(file="Icon_Images/Video.png")
imagePicture = tk.PhotoImage(file="Icon_Images/Image.png")

# Create attributes
# Labels
title = tk.Label(window, text="Welcome to \nUni-Convert!", font=("Arial", 60))
typeLabel = tk.Label(text="Which kind of files would you like to convert?", font=("Arial", 20))

imageLabel = tk.Label(text="Image", font=("Arial", 20))
videoLabel = tk.Label(text="Video", font=("Arial", 20))
audioLabel = tk.Label(text="Audio", font=("Arial", 20))

# Buttons
imageButton = tk.Button(text="Image", image=imagePicture, command=image_clicked)
videoButton = tk.Button(text="Video", image=videoPicture, command=video_clicked)
audioButton = tk.Button(text="Audio", image=audioPicture, command=audio_clicked)

# Grid attributes
# Grid labels
title.grid(column=0, row=0, columnspan=3)
typeLabel.grid(column=0, row=1, columnspan=3)

# Grid buttons
imageButton.grid(column=0, row=3)
videoButton.grid(column=1, row=3)
audioButton.grid(column=2, row=3)

imageLabel.grid(column=0, row=4)
videoLabel.grid(column=1, row=4)
audioLabel.grid(column=2, row=4)


# Run application
window.mainloop()
