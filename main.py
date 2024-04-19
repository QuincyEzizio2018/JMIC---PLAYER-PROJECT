from tkinter import*
from tkinter import ttk, filedialog, messagebox
from pygame import mixer
import customtkinter
from PIL import Image, ImageTk
import os
import requests, time, random, io, pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

main_screen = Tk()
main_screen.title("JMIC Player")

# Get the screen width and height
screen_width = main_screen.winfo_screenwidth()
screen_height = main_screen.winfo_screenheight()

# Calculate the window size relative to the screen
window_width = int(screen_width * 0.45)  # 80% of screen width
window_height = int(screen_height * 0.6)  # 60% of screen height

# Calculate the window position relative to the screen
x_pos = int((screen_width - window_width) / 2)  # Center horizontally
y_pos = int((screen_height - window_height) / 2)  # Center vertically

# Set window size and position
main_screen.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

main_screen.configure(bg="white")
main_screen.resizable(False, False)


"""Quincy"""
def update_progress_bar_with_time():
    ...


def add_songs_from_folder():
    pass


def add_selected_songs():
    pass


def playallsong():
    ...


"""Crown"""
def play(event=None):
    pass


# Create Global Pause Variable
global paused
paused = False
def pause(is_paused):
    ...

def stop():
    ...


def next_song():
    pass


def previous_song():
    pass


def show_menu():
    ...


"""Ifeanyi"""
def delete_song():
    ...


def delete_all_songs():
    ...


def toggle_repeat():
    ...


def shuffle_playlist():
    ...

def update_volume_and_label(x):
    pass



"""Quincy"""
def display_album_cover(song_name):
    ...


def get_default_image():
    ...


def fetch_lyrics():
    ...


def show_lyrics():
    ...


def slide():
    ...




#icon
image_icon = PhotoImage(file="images/logo.png") #this is for the top logo close to JMIC - Player
main_screen.iconphoto(False, image_icon)

"""MR CROWN"""
"""
On Blue : Crown
1. Add Songs Label
2. Open Folded button
3. Pick songs button
4. Playlist frame
5. Playlist list box
6. Playlist title "Song playlist"
7. Playlist Menu "Remove Songs" which will contain "Delete song from playlist" and "Delete all songs from playlist"
8. Scroll bar horizontal and vertical
"""



"""MR IFEANYI"""
"""
On Red : Ifeanyi
1. Music frame
2. Music notebook containing "Music_cover" and "Lyrics"
3. Music welcome label
"""



"""MR QUINCY"""
"""
On Black : Quincy
1. Music label
2. Progress bar slider
3. Music time status
4. Shuffle button
5. Previous button
6. Pause button
7. Play button
8. Stop button
9. Next Button
10. Repeat button
11. Volume label
12. Volume slider
"""
#icon
image_icon = PhotoImage(file="images/logo.png") #this is for the top logo close to JMIC - Player
main_screen.iconphoto(False, image_icon)

#Button
shuffle = PhotoImage(file="images/40x26/shuffle.png", width=40, height=26)
Button(main_screen, text="", compound=LEFT, image=shuffle, fg= "white", bg="white", bd=0, font=("ariel", 10, "bold"), command=shuffle_playlist).place(x=235, y=465)

previous_button = PhotoImage(file="images/40x40/previous.png", width=20, height=20)
Button(main_screen, text="", compound=LEFT, image=previous_button, bd=0, fg= "white", bg="white", command=previous_song).place(x=260, y=460)

pause_button = PhotoImage(file="images/40x40/pause.png", width=20, height=20)
Button(main_screen, text="", compound=LEFT, image=pause_button, bd=0, fg= "white", bg="white", command=lambda: pause(paused)).place(x=290, y=460)

play_button = PhotoImage(file="images/40x40/play.png", width=40, height=40)
Button(main_screen, text="", compound=LEFT, image=play_button, bd=0, fg= "white", bg="white", command=play).place(x=320, y=450)

stop_button = PhotoImage(file="images/40x40/stop.png", width=20, height=20)
Button(main_screen, text="", compound=LEFT, image=stop_button, bd=0, fg= "white", bg="white", command=stop).place(x=370, y=460)

next_button = PhotoImage(file="images/40x40/next.png", width=20, height=20)
Button(main_screen, text="", compound=LEFT, image=next_button, bd=0, fg= "white", bg="white", command=next_song).place(x=400, y=460)

repeat_img = PhotoImage(file="images/40x26/repeat.png", width=40, height=23)
repeat = Button(main_screen, text="", bg="white", bd=0, image=repeat_img, compound=LEFT, fg= "white", font=("ariel", 10, "bold"), command=toggle_repeat)
repeat.place(x=430, y=465)

#Label of Music being played
music_frame = Frame(main_screen, width=250, height=15, bd=4, bg="white").place(x=15, y=408)
music = Label(music_frame, text="Current playing song", font=("ariel", 10), fg="Black", bg="white", wraplength=250)
music.place(x=15, y=408)

# Create Time Status Bar
time_status_bar = Label(main_screen, text='00:00', bd=1, relief=GROOVE, anchor=E)
time_status_bar.place(x=660, y=420, anchor="center")

time_status_bar1 = Label(main_screen, text='00:00', bd=1, relief=GROOVE, anchor=E)
time_status_bar1.place(x=290, y=420, anchor="center")

#Volume nub
volume_slider = customtkinter.CTkSlider(master=main_screen, from_=0, to=100, command=lambda value: [update_volume_and_label(value)], width=100, number_of_steps=100)
volume_slider.place(x=582, y=460)

volume_label = Label(main_screen, text="Volume: 100", font=("Helvetica", 7, "bold"), fg="black", bg="white")
volume_label.place(x=602, y=475)


# Create Music Position Slider
my_slider = ttk.Scale(main_screen, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=320, style="TScale")
my_slider.place(x=315, y=413)
# Create a style object
style = ttk.Style()
style.theme_use("clam")

# Set the background color (left side) of the scale widget
style.configure("TScale", troughcolor="light blue", background="blue", 
                highlightcolor="sea green", slidercolor=[("active", "light green")], 
                gripcount=0, bordercolor="light blue", relief="flat", sliderthickness = 15)



main_screen.mainloop()