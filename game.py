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
canvas = tk.Canvas(window, width=400, height=400, bg="lightgreen")
canvas.grid()

for x in range(11):
    for y in range(11):
        text = f"({x}, {y})"
        label = tk.Label(text=text, foreground="darkblue")
        label.grid(column=y, row=x)

# greeting = tk.Label(text="Hello World")
# greeting.pack()
window.mainloop()
