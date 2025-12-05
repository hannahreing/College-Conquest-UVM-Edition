"""
College Conquest UVM Edition
Elijah Burton, Luke Price, Hannah Reing
CS 1210 G
"""

from itertools import count
import random
import math
import tkinter as tk
from tkinter.ttk import *
# pip installed Pillow so we can upload images as jpgs.
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Match 3: Graduate for Free!")

# Ensure the main window is raised so it appears to the user.
window.lift()
window.attributes('-topmost', True)
# Clear the topmost flag shortly after to allow normal window behavior
window.after(100, lambda: window.attributes('-topmost', False))

# If a secondary window is needed, use a Toplevel (uncomment to use):
# root_test = tk.Toplevel(window)
# root_test.title("Diploma!")

# Allows dimensions of window to change.
canvas_width = 800
canvas_height = 900
spacing = 45
offset = 150
canvas = tk.Canvas(window, width=canvas_width,
                   height=canvas_height, background="#154734")
canvas.grid(row=0, column=0, rowspan=10, columnspan=10)

#create a frame for the timer
timer_frame = tk.Frame(window, width=200, height=70, bg="#FFD700", highlightbackground="white", highlightthickness=5)
timer_frame.grid(row=0, column=0, pady=20, padx=20)

# Creates timer label
timer_label = tk.Label(window, font=("Helvetica", 36), fg="white", bg="#FFD700")  
timer_label.grid(row=0, column=0, pady=30, padx=30)
def countdown(count):
    # convert seconds to minutes and seconds
    minutes = count // 60
    seconds = count % 60
    time_format = f"{minutes:02d}:{seconds:02d}"

    if count > 0:
        # update the label every 1000 milliseconds (1 second)
        timer_label.config(text=time_format, fg="white")
        window.after(1000, countdown, count-1)
    else:
        timer_label.config(text="Time's up!",font=("Helvetica", 24), fg="#154734")
        return False

grid_frame = tk.Frame(canvas,
                      width=700,
                      height=700,
                      highlightbackground="white",
                      highlightthickness=10,
                      background="#154734")

test_frame = tk.Frame(canvas,
                      width=150,
                      height=50,
                      highlightbackground="white",
                      highlightthickness=10,
                      background="#FFD700")

#create windows for frames on canvas now that they are defined
canvas.create_window(50, 150, anchor="nw", window=grid_frame)
canvas.create_text(75, 25, text="CREDITS", font=("Arial", 20), fill="white")

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


def buildbutton(x, y):
    # Randomly selects an image using random generation of a number 0-6.
    index_college = random.randrange(0, 7)
    random_image = images[index_college]

    button = tk.Button(grid_frame, foreground="white",
                       image=random_image, command=lambda x=x, y=y: button_click_handler(x, y))

    # Creates an attribute for each button that stores its college.
    button.type = collegedata[index_college]

    # Positions buttons in a grid layout.
    button.grid(row=x, column=y, padx=1, pady=1)

    # Assigns each button to a space in a 2d list "gameboard" corresponding with the board.
    # For example, gameboard[1][2] gives button in second row, third column (Python is zero indexed).
    gameboard[x][y] = button

    # Aligns labels with canvas dimensions.
    canvas.create_text(y * spacing + offset, x * spacing +
                       offset)

    return button

# Builds button for each coordinate pair on board.


def drawboard():
    for x in range(10):
        for y in range(10):
            if gameboard[x][y] is None:
                buildbutton(x, y)


# horiz_finder scans across columns for each row, vertical_finder scans across rows for each column


def matchfinder(gameboard):

    def horiz_finder(gameboard):
        matches = []
        # For each row.
        for x in range(len(gameboard)):
            current_type = None
            streak = 0
            # For each column in this row.
            for y in range(len(gameboard[x])):
                # Get piece type at (x,y)
                if gameboard[x][y] is None:
                    new_type = None
                else:
                    new_type = gameboard[x][y].type

                if new_type != current_type:
                    # Check if previous streak was long enough.
                    if streak >= 3:
                        # Save coordinates from start of streak to current - 1.
                        # For example, if y = 3 and streak = 3, then range is [0, 1, 2],
                        # so (x, 0), (x, 1), (x, 2) get added to matches in a smaller list.
                        small_list = []
                        for k in range(y - streak, y):
                            small_list.append((x, k))
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
                for k in range(len(gameboard[x]) - streak, len(gameboard[x])):
                    small_list.append((x, k))
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
        for y in range(width):
            current_type = None
            streak = 0

            # For each column, scan down rows.
            for x in range(height):
                if gameboard[x][y] is None:
                    new_type = None
                else:
                    new_type = gameboard[x][y].type

                if new_type != current_type:
                    if streak >= 3:
                        small_list = []
                        for k in range(x - streak, x):
                            small_list.append((k, y))
                        matches.append(small_list)
                    current_type = new_type
                    streak = 1
                else:
                    streak += 1

            if streak >= 3:
                small_list = []
                for k in range(height - streak, height):
                    small_list.append((k, y))
                matches.append(small_list)

        return matches
    # Returns total matches
    return horiz_finder(gameboard) + vertical_finder(gameboard)


def matchremover(m):

    # Unduplicate the coordinates to remove
    coords = set()
    for group in m:
        for (row, col) in group:
            coords.add((row, col))
    # Destroy matched buttons and mark those spots None
    for (r, c) in coords:
        if 0 <= r < 10 and 0 <= c < 10:
            btn = gameboard[r][c]
            if btn is not None:
                try:
                    btn.destroy()
                except Exception:
                    # if button is thanos give up
                    pass
            gameboard[r][c] = None

    # For each column
    for c in range(10):
        # Where the next existing tile should fall to (bottom-up)
        write_row = 9
        # Scanning up the column
        for r in range(9, -1, -1):

            if gameboard[r][c] is not None:
                btn = gameboard[r][c]
                # If button needs to be moved down
                if r != write_row:
                    # Move to lower place
                    gameboard[write_row][c] = btn
                    # Update on screen
                    btn.grid(row=write_row, column=c)

                    # Clears old position
                    gameboard[r][c] = None
                else:
                    # Already in correct position
                    btn.grid(row=r, column=c)
                write_row -= 1

        # Create new buttons at the top
        for r in range(write_row, -1, -1):
            if r < 0:
                break
            buildbutton(r, c)


def init_board(gameboard):
    drawboard()
    print(matchfinder(gameboard))
    while matchfinder(gameboard):
        matchremover(matchfinder(gameboard))


#def button_click_handler(row, col):


if __name__ == "__main__":
        init_board(gameboard)
        print(matchfinder(gameboard))
        countdown(10)

# Tells Python to run the event loop, blocks any code after from running until you close the window
window.mainloop()
