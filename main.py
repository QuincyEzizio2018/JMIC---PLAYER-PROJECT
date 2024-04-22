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
window_width = int(screen_width * 0.5)  # 80% of screen width
window_height = int(screen_height * 0.65)  # 60% of screen height

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


"""MR CROWN"""
"""
On Blue : Crown
1. Add and Minus(remove) Menu
2. Playlist frame
3. Playlist list box
4. Playlist title "Song playlist"
5. Playlist Menu "Remove Songs" which will contain "Delete song from playlist" and "Delete all songs from playlist"
6. Scroll bar horizontal
"""
#Playlist Frame and title_label
playlist_frame = Frame(main_screen, bd=2, relief=RIDGE)
playlist_frame.place(x=15, y=0, width=250, height=400)

playlist_title = Label(playlist_frame, text="Songs Playlist", font=("Helvetica", 10, "bold"))
playlist_title.pack( anchor="w")

# Create menu
my_menu = Menu(main_screen)
main_screen.config(menu=my_menu)


# Create the Add Songs menu
add_song_menu = Menu(playlist_frame, tearoff=0)
add_song_menu.add_command(label="Add Songs From Folder", command=add_songs_from_folder)
add_song_menu.add_command(label="Pick Out Tracks", command=add_selected_songs)

# Create a Menubutton to display the Remove Songs menu
add_song_button = Menubutton(text="+", font=("ariel", 15, "bold"), fg="black", borderwidth=-5, menu=add_song_menu)
add_song_button.place(x=200, y=3)
add_song_button.bind("<Button-1>", lambda event: show_add())   # Bind the show_remove function to the button click event

# Create the Remove Songs menu
remove_song_menu = Menu(playlist_frame, tearoff=0)
remove_song_menu.add_command(label="Delete Selected Song", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs", command=delete_all_songs)

# Create a Menubutton to display the Remove Songs menu
remove_songs_button = Menubutton(text="~", font=("ariel", 15, "bold"), fg="black", borderwidth=-5, menu=remove_song_menu)
remove_songs_button.place(x=235, y=3)
remove_songs_button.bind("<Button-1>", lambda event: show_remove())   # Bind the show_remove function to the button click event

# Create Playlist Box
#Playlist Scroll Bar
scroll = Scrollbar(playlist_frame)
playlist_box = Listbox(playlist_frame, width=100, font= ("ariel", 10), bg="#D7D4D9", fg="black", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist_box.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist_box.pack(side=LEFT, fill=BOTH)
playlist_box.bind("<Double-1>", lambda event: play()) # Bind double-click event to the playlist

"""MR IFEANYI"""
"""
On Red : Ifeanyi
1. Music frame
2. Music notebook containing "Music_cover" and "Lyrics"
3. Music welcome label
"""
#Notebook Creation for widget
music_diplay = ttk.Notebook(main_screen) #Widgets or Notebooks
music_diplay.place(x=275, y=0, width=400, height=400)


music_img = PhotoImage(file="music_thumbnails/istockphoto-1192064761-612x612.png", width=400, height=400)
music_thumbnail_widget = Label(music_diplay, image=music_img)    #widgets 1  

lyrics_widget = Text(music_diplay, bg="lightblue", fg="black", font=("Arial", 10), wrap="word", width=400, height=400)#widgets 2

music_diplay.add(music_thumbnail_widget, text="Music")
music_diplay.add(lyrics_widget, text="lyrics")

music_display_title = Label(music_diplay, bg="#D7D4D9", text="Welcome to JMIC-Player", font=("Helvetica", 10, "bold"))
music_display_title.pack(pady=0, anchor="e")

lyrics_widget.insert(END, "Lyrics will be displayed here...")
lyrics_widget.config(state=DISABLED)

#Lyrics Scroll Bar
lyrics_scrollbar = Scrollbar(lyrics_widget, orient="vertical", command=lyrics_widget.yview)
lyrics_widget.config(yscrollcommand=lyrics_scrollbar.set)
lyrics_scrollbar.pack(side="right",fill="y")



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