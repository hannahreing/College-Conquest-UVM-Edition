"""
College Conquest UVM Edition
Elijah Burton, Luke Price, Hannah Reing
CS 1210 G
"""

import random
import math
import tkinter as tk

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

for x in range(11):
    for y in range(11):
        text = f"({x}, {y})"
        # Using labels allows us to add buttons
        button = tk.Button(text=text, foreground="white")
        button.grid(column=y, row=x)
        # Aligns labels with canvas dimensions
        canvas.create_text(y*spacing + offset, x*spacing +
                           offset)
# Tells Python to run the event loop, blocks any code after from running until you close the window
window.mainloop()
