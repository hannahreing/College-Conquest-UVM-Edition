"""
College Conquest UVM Edition
Elijah Burton, Luke Price, Hannah Reing
CS 1210 G
Hopefully the Gods of the mormon turtle church favor us
"""

import random
import math
import tkinter as tk
from tkinter.ttk import *
# pip installed Pillow so we can upload images as jpgs.
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Match 3: Graduate for Free!")

# Allows dimensions of window to change.
canvas_width = 700
canvas_height = 700
spacing = 45
offset = 60
canvas = tk.Canvas(window, width=canvas_width,
                   height=canvas_height, background="#154734")
canvas.grid(row=0, column=0, rowspan=10, columnspan=10)

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

gameboard = [[None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None, None, None]]

images = [final_cas_image, final_cals_image, final_cems_image,
          final_cess_image, final_cnhs_image, final_gsb_image, final_rsenr_image]
collegedata = ["cas", "cals", 'cems', "cess", "cnhs", "gsb", "rsenr"]

selected = None


def button_click_handler(row, col):
    # If no button has been selected yet, store this position
    global selected

    # Cannot select
    if gameboard[row][col] is None:
        pass

    print(f"Clicked: ({row}, {col})")

    # First click
    if selected is None:
        selected = (row, col)
        highlight_button(row, col)
        print(f"Selected: ({row}, {col})")
   # Second click
    else:
        old_row, old_col = selected
        new_row, new_col = row, col

        if adjacent(old_row, old_col, new_row, new_col):
            try_swap(old_row, old_col, new_row, new_col)
        else:
            print("Not adjacent")

        unhighlight_button(old_row, old_col)
        selected = None


def highlight_button(row, col):
    btn = gameboard[row][col]
    if btn:
        btn.config(bg="yellow", relief="sunken", borderwidth=4)


def unhighlight_button(row, col):
    btn = gameboard[row][col]
    if btn:
        btn.config(bg="SystemButtonFace", relief="raised", borderwidth=2)


def adjacent(r1, c1, r2, c2):
    if r1 == r2 and abs(c1 - c2) == 1:
        return True
    if c1 == c2 and abs(r1-r2) == 1:
        return True
    else:
        return False


def buildbutton(row, col):
    # Randomly selects an image using random generation of a number 0-6.
    index_college = random.randrange(0, 7)
    random_image = images[index_college]

    button = tk.Button(
    foreground="white",
    image=random_image,
    command=lambda r=row, c= col : button_click_handler(r,c)
    )


    # Creates an attribute for each button that stores its college.
    button.type = collegedata[index_college]
    button.row = row
    button.col = col

    button.config(command=lambda b=button: button_click_handler(b.row, b.col))

    # Positions buttons in a grid layout.
    button.grid(row=row, column=col)

    # Assigns each button to a space in a 2d list "gameboard" corresponding with the board.
    # For example, gameboard[1][2] gives button in second row, third column (Python is zero indexed).
    gameboard[row][col] = button

    return button

# Builds button for each coordinate pair on board.


def drawboard():
    for row in range(10):
        for col in range(10):
            if gameboard[row][col] is None:
                buildbutton(row, col)


# horiz_finder scans across columns for each row, vertical_finder scans across rows for each column


def matchfinder(gameboard):

    def horiz_finder(gameboard):
        matches = []
        # For each row.
        for row in range(len(gameboard)):
            current_type = None
            streak = 0
            # For each column in this row.
            for col in range(len(gameboard[row])):
                # Get piece type at (x,y)
                if gameboard[row][col] is None:
                    new_type = None
                else:
                    new_type = gameboard[row][col].type

                if new_type != current_type:
                    # Check if previous streak was long enough.
                    if streak >= 3:
                        # Save coordinates from start of streak to current - 1.
                        # For example, if y = 3 and streak = 3, then range is [0, 1, 2],
                        # so (row, 0), (row, 1), (row, 2) get added to matches in a smaller list.
                        small_list = []
                        for k in range(col - streak, col):
                            small_list.append((row, k))
                        matches.append(small_list)
                    # Reset streak tracking
                    current_type = new_type
                    streak = 1
                else:
                    streak += 1
            # Catches the edge cases when a streak reaches the end of a row
            # because there is no current_type = new_type to save it.
            if streak >= 3:
                small_list = []
                for k in range(len(gameboard[row]) - streak, len(gameboard[row])):
                    small_list.append((row, k))
                matches.append(small_list)
        # Returns a list of lists of tuples (inside lists are coordinates with same images)
        return matches

    def vertical_finder(gameboard):
        matches = []

        # Number of columns
        width = len(gameboard[0])

        # Number of rows
        height = len(gameboard)

        # For each column
        for col in range(width):
            current_type = None
            streak = 0

            # For each column, scan down rows.
            for row in range(height):
                if gameboard[row][col] is None:
                    new_type = None
                else:
                    new_type = gameboard[row][col].type

                if new_type != current_type:
                    if streak >= 3:
                        small_list = []
                        for k in range(row - streak, row):
                            small_list.append((k, col))
                        matches.append(small_list)
                    current_type = new_type
                    streak = 1
                else:
                    streak += 1

            if streak >= 3:
                small_list = []
                for k in range(height - streak, height):
                    small_list.append((k, col))
                matches.append(small_list)

        return matches
    # Returns total matches
    return horiz_finder(gameboard) + vertical_finder(gameboard)

def matchremover(matches):
    #Collect all coordinates to remove (unduplicate)
    coords = set()
    for group in matches:
        for (row, col) in group:
            coords.add((row, col))

    #Destroy matched buttons and mark spots None
    for (row, col) in coords:
        btn = gameboard[row][col]
        if btn is not None:
            try:
                btn.destroy()
            except Exception:
                pass
        gameboard[row][col] = None

    #For each column, move buttons down and fill new ones
    for col in range(10):
        # Gather all existing buttons in the column
        existing_buttons = [gameboard[r][col] for r in range(10) if gameboard[r][col] is not None]

        # Clear the column
        for r in range(10):
            gameboard[r][col] = None

        # Place existing buttons at the bottom
        write_row = 9
        for btn in reversed(existing_buttons):
            gameboard[write_row][col] = btn
            btn.grid(row=write_row, column=col)
            btn.row = write_row
            btn.col = col
            write_row -= 1

        # Fill the rest of the column with new buttons at the top
        for r in range(write_row, -1, -1):
            buildbutton(r, col)


def init_board(gameboard):
    drawboard()
    print(matchfinder(gameboard))
    while matchfinder(gameboard):
        matchremover(matchfinder(gameboard))


def try_swap(r1, c1, r2, c2):
    btn1 = gameboard[r1][c1]
    btn2 = gameboard[r2][c2]

    # Swap them in the gameboard
    gameboard[r1][c1], gameboard[r2][c2] = btn2, btn1

    # Update their .row and .col attributes
    btn1.row, btn1.col = r2, c2
    btn2.row, btn2.col = r1, c1

    # Update positions on the screen
    btn1.grid(row=r2, column=c2)
    btn2.grid(row=r1, column=c1)

    # Check for matches after swap
    if matchfinder(gameboard):
        matchremover(matchfinder(gameboard))
    else:
        # No matches → swap back
        gameboard[r1][c1], gameboard[r2][c2] = btn1, btn2
        btn1.row, btn1.col = r1, c1
        btn2.row, btn2.col = r2, c2
        btn1.grid(row=r1, column=c1)
        btn2.grid(row=r2, column=c2)



def board_is_softlocked(gameboard):
    rows = len(gameboard)
    cols = len(gameboard[0])

    # swap two coordinates
    def swap(a, b):
        (r1, c1), (r2, c2) = a, b
        gameboard[r1][c1], gameboard[r2][c2] = gameboard[r2][c2], gameboard[r1][c1]

    # Try swapping each tile with RIGHT and DOWN neighbors
    for row in range(rows):
        for col in range(cols):

            # Skip empty spaces (shouldn't happen but safe)
            if gameboard[row][col] is None:
                continue

            # Try right swap
            if col + 1 < cols:
                if gameboard[row][col+1] is not None:
                    swap((row, col), (row, col+1))
                    if matchfinder(gameboard):
                        swap((row, col), (row, col+1))  # swap back
                        return False           # NOT softlocked
                    swap((row, col), (row, col+1))      # swap back

            # Try down swap
            if row + 1 < rows:
                if gameboard[row+1][col] is not None:
                    swap((row, col), (row+1, col))
                    if matchfinder(gameboard):
                        swap((row, col), (row+1, col))
                        return False
                    swap((row, col), (row+1, col))

    return True   # no swaps produced matches -> softlocked


if __name__ == "__main__":
    init_board(gameboard)
    # Tells Python to run the event loop, blocks any code after from running until you close the window
    window.mainloop()
