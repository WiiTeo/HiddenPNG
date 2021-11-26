from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
import sys

filepath = askopenfilename(title="Open a image",filetypes=[('PNG Image File','.png'),('Other File','.*')])

fileopen = open(filepath, "a")

print("HiddenPNG 2021 (by WiiTeo)")
print(f"Selected image : {filepath}")

userType = input("Text>")

fileopen.write(userType)
fileopen.close()
