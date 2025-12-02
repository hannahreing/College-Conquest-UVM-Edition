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

images = [final_cas_image, final_cals_image, final_cems_image, final_cess_image, final_cnhs_image, final_gsb_image, final_rsenr_image]
collegedata = ["cas", "cals", 'cems', "cess", "cnhs", "gsb", "rsenr"]

def buildbutton(x,y):
    text = f"({x}, {y})"
    college = random.randrange(0,6)
    random_image = images[college]
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

def drawboard():
    for x in range(10):
        for y in range(10):
            buildbutton(x,y)

def matchfinder(gameboard):
    def horiz_finder(gameboard):        
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
                        smollist=[]
                        for k in range(y - streak, y):
                            smollist.append((x, k))
                        matches.append(smollist)
                    # Reset streak tracking
                    trn = current_type
                    streak = 1
                else:
                    streak += 1
            if streak >= 3:
                #Not fully understandable ngl but basically if there's still a streak at the end thats over 3 long:
                #We add the indexes starting from when the streak starts to the end of the row
                #(since we reached the end of the row there isnt a character that would end the streak and trigger the signaling of the streak itself)
                smollist=[]
                for k in range(len(gameboard[x]) - streak, len(gameboard[x])):
                    smollist.append((x, k))
                matches.append(smollist)
        return matches
    
    def vertical_finder(gameboard):
        matches = []

        width = len(gameboard[0])     # number of columns
        height = len(gameboard)       # number of rows

        for y in range(width):        # for each column
            trn = None
            streak = 0

            for x in range(height):   # scan top -> bottom
                current_type = gameboard[x][y].type

                if current_type != trn:
                    if streak >= 3:
                        smollist=[]
                        for k in range(x - streak, x):
                            smollist.append((k, y))
                        matches.append(smollist)
                    trn = current_type
                    streak = 1
                else:
                    streak += 1

            if streak >= 3:
                smollist=[]
                for k in range(height - streak, height):
                    smollist.append((k, y))
                matches.append(smollist)

        return matches
    
    return horiz_finder(gameboard) + vertical_finder(gameboard)


def matchremover(m):
    # Ensure every row is exactly 10 columns
    for r in range(10):
        while len(gameboard[r]) < 10:
            gameboard[r].append(None)
        while len(gameboard[r]) > 10:
            gameboard[r].pop()
    #unduplicate the coordinates to remove
    coords = set()
    for group in m:
        for (row, col) in group:
            coords.add((row, col))
    # Destroy matched buttons and mark those spots None
    for (r, c) in coords:
        if 0 <= r < 10 and 0 <= c < 10:
            btn = gameboard[r][c]
            if btn != None:
                try:
                    btn.destroy()
                except Exception:
                    #if button is thanos give up
                    pass
            gameboard[r][c] = None

    #collapsing the column and filling in the top
    for c in range(10):
        write_row = 9  # where the next existing tile should fall to (bottom-up)
        # move existing tiles down
        for r in range(9, -1, -1):
            if gameboard[r][c] != None:
                if r != write_row:
                    gameboard[write_row][c] = gameboard[r][c]
                    gameboard[write_row][c].grid(row=write_row, column=c)
                    gameboard[r][c] = None
                else:
                    gameboard[r][c].grid(row=r, column=c)
                write_row -= 1

        #rebuttonify that mofo
        for r in range(write_row, -1, -1):
            if r < 0:
                break
            buildbutton(r, c)







drawboard() 
print(matchfinder(gameboard))  
while matchfinder(gameboard):
    matchremover(matchfinder(gameboard))




# Tells Python to run the event loop, blocks any code after from running until you close the window
window.mainloop()
