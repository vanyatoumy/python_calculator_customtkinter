import tkinter
import customtkinter
from pytube import YouTube


# Downloader functions
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        title.configure(text=yt_object.title)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        finish_label.configure(text="Downloaded!")
    except:
        finish_label.configure(text="Download error!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text=per + '%')
    progress_percentage.update()


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("480x240")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack(pady=10)


# Prgress ercentage
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.pack()

# Download button
download = customtkinter.CTkButton(app, width=100, height=30, text="Download", command=start_download)
download.pack(pady=10)

# Run qpp
app.mainloop()
