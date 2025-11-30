"""
College Conquest UVM Edition
Elijah Burton, Luke Price, Hannah Reing
CS 1210 G
"""

import random
import math
import tkinter as tk
from tkinter.ttk import *
# pip installed Pillow so we can upload images as jpegs.
from PIL import Image, ImageTk

window = tk.Tk()
window.title("College Conquest UVM Edition")

# Allows dimensions of window to change.
canvas_width = 700
canvas_height = 700
spacing = 40
offset = 30
canvas = tk.Canvas(window, width=canvas_width,
                   height=canvas_height, background="#154734")
canvas.grid(row=0, column=0, rowspan=11, columnspan=11)

# Create all image objects.
# CAS
cas_image = Image.open("College Images/CAS.jpeg")
resized_cas = cas_image.resize((60, 60))
final_cas_image = ImageTk.PhotoImage(resized_cas)

# CALS
cals_image = Image.open("College Images/CALS.jpeg")
resized_cals = cals_image.resize((60, 60))
final_cals_image = ImageTk.PhotoImage(resized_cals)

# CEMS

# CESS

# CNHS

# GSB

for x in range(11):
    for y in range(11):
        text = f"({x}, {y})"
        random_image = random.choice([final_cas_image, final_cals_image])
        # Randomly select an image.

        button = tk.Button(text=text, foreground="white",
                           image=random_image)
        button.grid(column=y, row=x)
        # Aligns labels with canvas dimensions
        canvas.create_text(y*spacing + offset, x*spacing +
                           offset)


# Tells Python to run the event loop, blocks any code after from running until you close the window
window.mainloop()
