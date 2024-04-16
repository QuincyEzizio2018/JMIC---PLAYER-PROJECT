from tkinter import*
from tkinter import ttk
import customtkinter

main_screen = Tk()
main_screen.title("JMIC Player")
# main_screen.geometry("700x700")
main_screen.minsize(850,750)
main_screen.configure(bg="#0f1a2b")
main_screen.resizable(False, False)


def update_progress_bar_with_time():
    ...


def add_songs_from_folder():
    pass


def add_selected_songs():
    pass


def playallsong():
    ...


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


def delete_song():
    ...


def delete_all_songs():
    ...


def toggle_repeat():
    ...


def shuffle_playlist():
    ...


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


def update_volume_and_label(x):
    pass






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
4. Playing music label
5. Music time status
"""

"""MR QUINCY"""
"""
On Black : Quincy
1. Progress bar slider
2. Pause button
3. Play button
4. Stop button
5. Next button
6. Previous button
7. Repeat button
8. Shuffle button
9. Volume label
10. Volume slider
"""
# Create Music Position Slider
my_slider = ttk.Scale(main_screen, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=430, style="TScale")
my_slider.place(x=380, y=530)

# Create a style object
style = ttk.Style()
style.theme_use("clam")

# Set the background color (left side) of the scale widget
style.configure("TScale", troughcolor="light blue", background="blue", 
                highlightcolor="sea green", slidercolor=[("active", "light green")], 
                gripcount=0, bordercolor="light blue", relief="flat", sliderthickness = 15)


#BUTTONS
play_button = PhotoImage(file="images/70x70/Play.png", width=70, height=70)
Button(main_screen, text="", compound=LEFT, image=play_button, fg= "white", bg="#0f1a2b", command=play).place(x=450, y=615)

stop_button = PhotoImage(file="images/50x50/Stop.png", width=50, height=50)
Button(main_screen, text="", compound=LEFT, image=stop_button, fg= "white", bg="#0f1a2b", command=stop).place(x=380, y=580)

pause_button = PhotoImage(file="images/50x50/Pause.png")
Button(main_screen, text="", compound=LEFT, image=pause_button, fg= "white", bg="#0f1a2b", command=lambda: pause(paused)).place(x=540, y=580)

previous_button = PhotoImage(file="images/50x50/Previous.png", width=50, height=50)
Button(main_screen, text="", compound=LEFT, image=previous_button, fg= "white", bg="#0f1a2b", command=previous_song).place(x=380, y=660)

next_button = PhotoImage(file="images/50x50/Next.png", width=50, height=50)
Button(main_screen, text="", compound=LEFT, image=next_button, fg= "white", bg="#0f1a2b", command=next_song).place(x=540, y=660)

shuffle = PhotoImage(file="images/50x50/Shuffle.png", width=50, height=50)
Button(main_screen, text="", compound=LEFT, image=shuffle, fg= "white", bg="#0f1a2b", font=("ariel", 10, "bold"), command=shuffle_playlist).place(x=620, y=580)

repeat_img = PhotoImage(file="images/50x50/Repeat.png", width=50, height=50)
repeat = Button(main_screen, text="", bg="#0f1a2b", image=repeat_img, compound=LEFT, fg= "white", font=("ariel", 10, "bold"), command=toggle_repeat)
repeat.place(x=758, y=580)

#VOLUME LABEL AND SLIDER
volume_slider = customtkinter.CTkSlider(master=main_screen, from_=0, to=100, command=lambda value: [update_volume_and_label(value)], width=100, number_of_steps=100)
volume_slider.place(x=660, y=690)

volume_label = Label(main_screen, text="Volume: 100", font=("Helvetica", 10, "bold"), fg="white", bg="#0f1a2b")
volume_label.place(x=670, y=660)



main_screen.mainloop()