import os
import re
# import all components 
# from the tkinter library 
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox

root = Tk()

# Make window invisible
root.withdraw()

# Instructions for users
tkinter.messagebox.showinfo('Select .mcf File', 'Please select the file you wish to modify.')

# Get target file
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select .mcf file",filetypes = (("mcf files","*.mcf.gcode"),("all files","*.*")))

# read file in and remove temp pauses
with open (root.filename, "r") as file:
    data = re.sub(re.compile("M105\nM109\sS[0-9]{3}(?!\nM82)", re.MULTILINE), '', file.read())

# Write the file out again
with open(root.filename, 'w') as file:
  file.write(data)

# Inform user of success
tkinter.messagebox.showinfo('Success', 'File has been successfully modified!')

# Exit
root.destroy()
