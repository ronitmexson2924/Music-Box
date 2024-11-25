# Importing the libraries
from tkinter import *
import pygame
import os

# Initializing pygame
pygame.init()

# Creating the main window
root = Tk()

# Setting the title and geometry
root.title("Music Box")
root.geometry("1352x700+0+0")
root.configure(background="white")

# Creating the frames
abc = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
abc.grid()
abc1 = Frame(abc, bg="powder blue", bd=20, relief=RIDGE)
abc1.grid()
abc2 = Frame(abc, bg="powder blue", relief=RIDGE)
abc2.grid()
abc3 = Frame(abc, bg="powder blue", relief=RIDGE)
abc3.grid()

# Variable to display the current key
str_var = StringVar()
str_var.set("Just like Music")

# Function to play a sound
def play_sound(note, file_path):
    try:
        if os.path.exists(file_path):
            str_var.set(note)
            sound = pygame.mixer.Sound(file_path)
            sound.play()
        else:
            str_var.set(f"File not found: {note}")
    except Exception as e:
        str_var.set(f"Error: {str(e)}")

# Define functions for each musical note
def value_Cs(): play_sound("C#", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\C# Db Single Note.mp3")
def value_A(): play_sound("A", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\A Single Note.mp3")
def value_B(): play_sound("B", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\B Single Note.mp3")
def value_C(): play_sound("C", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\C Single Note.mp3")
def value_Bb(): play_sound("Bb", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\A# Bb Single Note.mp3")
def value_Gs(): play_sound("G#", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\G# Ab Single Note.mp3")
def value_Ds(): play_sound("D#", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\D# Eb Single Note.mp3")
def value_Fs(): play_sound("F#", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\F# Gb Single Note.mp3")
def value_G(): play_sound("G", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\G Single Note.mp3")
def value_D(): play_sound("D", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\D Single Note.mp3")
def value_E(): play_sound("E", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\E Single Note.mp3")
def value_F(): play_sound("F", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\F Single Note.mp3")
def value_C1(): play_sound("C1", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\C Single Note.mp3")
def value_D1(): play_sound("D1", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\D Single Note.mp3")
def value_Cs1(): play_sound("C#1", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\C# Db Single Note.mp3")
def value_Ds1(): play_sound("D#1", r"C:\Users\ronit\OneDrive\Desktop\Python Files\Projects\Piano Game\Audio file of chords\D# Eb Single Note.mp3")

# Label
Label(
    abc1, text="Piano Musical Keys", font=("arial", 25, "bold"), padx=8, pady=8, bd=4, width=59, bg="powder blue",
    fg="white", height=1, justify=CENTER
).grid(row=0, column=0, columnspan=11)

# Display
Entry(
    abc1, textvariable=str_var, font=("arial", 18, "bold"), width=35, bd=34, bg="powder blue", fg="black",
    justify=CENTER
).grid(row=1, column=5, pady=1)

# Buttons
keys = [
    ("C#", value_Cs), ("D#", value_Ds), ("", None), ("F#", value_Fs), ("G#", value_Gs),
    ("Bb", value_Bb), ("", None), ("C#1", value_Cs1), ("D#1", value_Ds1)
]
for i, (text, cmd) in enumerate(keys):
    if text:
        Button(
            abc2, height=6, width=4, bd=4, text=text, font=("arial", 18, "bold"), bg="black", fg="white",
            command=cmd
        ).grid(row=0, column=i, padx=5, pady=5)
    else:
        Button(
            abc2, state=DISABLED, height=6, width=2, bg="powder blue", relief=FLAT
        ).grid(row=0, column=i, padx=0, pady=0)

# More buttons
white_keys = [
    ("C", value_C), ("D", value_D), ("E", value_E), ("F", value_F), ("G", value_G),
    ("A", value_A), ("B", value_B), ("C1", value_C1), ("D1", value_D1), ("E1", value_E)
]
for i, (text, cmd) in enumerate(white_keys):
    Button(
        abc3, bd=4, width=4, height=6, text=text, bg="white", fg="black", font=("arial", 18, "bold"), command=cmd
    ).grid(row=0, column=i, padx=5, pady=5)

# Mainloop
root.mainloop()

