from tkinter import *
from tkinter import filedialog
from youtube_download_music import download_song
import subprocess

def naslov():
    l2.configure(text="music loading...")
    outputfolder = filedialog.askdirectory(parent=root, initialdir=r"\\")
    strings = ["'", '"', ",", "_", "/", "+", " ", "$", "!", "@", "&", ".", "%", "ž", "đ", "ž", "š", "ć", "č", "?", "*", "=", "(", ")"]
    url = e2.get()
    ime = ""
    if e1.get() != "":
        for char in e1.get():
            if char not in strings:
                ime += char
    else:
        ime="songs"

    ##thread = Thread()
    download_song(url, outputfolder, ime)

    ##subprocess.Popen(download_song(url, outputfolder, ime))
    ##thread.start_new_thread(target = download_song, args = (url, outputfolder, ime))
    
   
    e2.delete(0, END)
    l2.configure(text="")
    

def exit():
    exit()


root=Tk()

root.geometry("430x250")
root.title("Music2GO")
root.configure(background="#444444")
root.focus_set()

l = Label(root, text="Playlist name:", font=("Arial", 15), bg="#444444", fg="#FFFFFF")
l.place(x = 10,
        y = 5,
        width=130,
        height=30)

e1 = Entry(root, font=("Arial", 20))
e1.place(x = 10,
        y = 40,
        width=250,
        height=40)


l = Label(root, text="Playlist url:", font=("Arial", 15), bg="#444444", fg="#FFFFFF")
l.place(x = 10,
        y = 85,
        width=110,
        height=30)

e2 = Entry(root, font=("Arial", 20))
e2.place(x = 10,
        y = 120,
        width=410,
        height=40)

button = Button(root, text="Download", command=naslov, font=("Arial", 15, "bold"), bg="grey")
button.place(x = 10,
        y = 170,
        width=200,
        height=60)

button = Button(root, text="Exit", command=root.destroy, font=("Arial", 15, "bold"), bg="grey")
button.place(x = 220,
        y = 170,
        width=200,
        height=60)

l2 = Label(root, text="", font=("Arial", 8, "bold"), bg="#444444", fg="#FFFFFF")
l2.place(x = 10,
        y = 232,
        width=100,
        height=10)

e1.focus_set()
root.mainloop()
