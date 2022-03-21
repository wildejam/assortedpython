from __future__ import unicode_literals
import tkinter as tk
import youtube_dl

#------------------------------Defining Youtube-dl functions------------------------------------------------------------
def Download():
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry.get()])

#---------------------------- Initializing the Window and Canvas -------------------------------------------------------
win_width = 500
win_height = 400

root = tk.Tk()
root.title("Youtube Video Downloader")

canvas = tk.Canvas(root, height=win_height, width=win_width)
canvas.pack()
main_frame = tk.Frame(canvas, bg="gray")
main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
#--------------------------- Initializing Widgets ----------------------------------------------------------------------
title = tk.Label(main_frame, text="Youtube Video Downloader!", bg="yellow")
title.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.25)

entry = tk.Entry(main_frame, bg="red")
entry.place(relx=0.1, rely=0.4, relwidth=0.55, relheight=0.1)

button = tk.Button(main_frame, text="Test Button", bg="blue", command=Download())
button.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)

help_text = tk.Text(main_frame, wrap="word")
help_text.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.3)
help_text.insert(tk.INSERT, "This tool will download a Youtube video as an mp3. To use it, paste the url of the "
                            "Youtube video you wish to download into the text bar, and press the button.")
help_text.config(state="disabled")
#----------------------------- Initializing GUI ------------------------------------------------------------------------
root.mainloop()














