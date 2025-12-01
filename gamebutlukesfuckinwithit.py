"""
College Conquest UVM Edition
Elijah Burton, Luke Price, Hannah Reing
CS 1210 G
"""

import random
import math
import tkinter as tk
from tkinter.ttk import *
# pip installed Pillow so we can upload images as jpgs.
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
button_dimensions = 60
# CAS
cas_image = Image.open("College Images/COLLEGE ICONS/CAS.jpg")
resized_cas = cas_image.resize((button_dimensions, button_dimensions))
final_cas_image = ImageTk.PhotoImage(resized_cas)

# CALS
cals_image = Image.open("College Images/COLLEGE ICONS/CALS.jpg")
resized_cals = cals_image.resize((button_dimensions, button_dimensions))
final_cals_image = ImageTk.PhotoImage(resized_cals)

# CEMS
cems_image = Image.open("College Images/COLLEGE ICONS/CEMS.jpg")
resized_cems = cems_image.resize((button_dimensions, button_dimensions))
final_cems_image = ImageTk.PhotoImage(resized_cems)

# CESS
cess_image = Image.open("College Images/COLLEGE ICONS/CESS.jpg")
resized_cess = cess_image.resize((button_dimensions, button_dimensions))
final_cess_image = ImageTk.PhotoImage(resized_cess)

# CNHS
cnhs_image = Image.open("College Images/COLLEGE ICONS/CNHS.jpg")
resized_cnhs = cnhs_image.resize((button_dimensions, button_dimensions))
final_cnhs_image = ImageTk.PhotoImage(resized_cnhs)

# GSB
gsb_image = Image.open("College Images/COLLEGE ICONS/GSB.jpg")
resized_gsb = gsb_image.resize((button_dimensions, button_dimensions))
final_gsb_image = ImageTk.PhotoImage(resized_gsb)

# RSENR
rsenr_image = Image.open("College Images/COLLEGE ICONS/RSENR.jpg")
resized_rsenr = rsenr_image.resize((button_dimensions, button_dimensions))
final_rsenr_image = ImageTk.PhotoImage(resized_rsenr)

gameboard = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]


for x in range(10):
    for y in range(10):
        text = f"({x}, {y})"
        images = [final_cas_image, final_cals_image, final_cems_image, final_cess_image, final_cnhs_image, final_gsb_image, final_rsenr_image]
        college = random.randrange(0,6)
        random_image = images[college]
        collegedata = ["cas", "cals", 'cems', "cess", "cnhs", "gsb", "rsenr"]
        # Randomly select an image.

        button = tk.Button(text=text, foreground="white",
                           image=random_image)
        
        #create an attribute for each button that stores its college
        button.type = collegedata[college]

        button.grid(column=y, row=x)

        #assign each button to a space in a 2d list corresponding with the board
        gameboard[x][y] = button

        # Aligns labels with canvas dimensions
        canvas.create_text(y*spacing + offset, x*spacing +
                           offset)
        
matches = []
# Go through each row: x is the row index
for x in range(len(gameboard)):
    trn = None        # type right now
    streak = 0        
    # Go through each column: y is the column index
    for y in range(len(gameboard[x])):
        current_type = gameboard[x][y].type

        if current_type != trn:
            # New piece type, check if previous streak was long enough
            if streak >= 3:
                # Add ALL coordinates from the streak
                for k in range(y - streak, y):
                    matches.append((x, k))
            # Reset streak tracking
            trn = current_type
            streak = 1
        else:
            streak += 1
    if streak >= 3:
        for k in range(len(gameboard[x]) - streak, len(gameboard[x])):
            matches.append((x, k))
print(matches)


        




# Tells Python to run the event loop, blocks any code after from running until you close the window
window.mainloop()
