# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:19:14 2021

@author: Ismail khan
"""
#digital clock
'''from tkinter import *

from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)
    
label = Label(root, font=("ds-digital",80), background="Black",foreground = "white")
label.pack(anchor='center')
time()
mainloop()'''

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Ismails Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("ds-digital",80),background='blue',foreground='white')
label.pack(anchor= "center")

time()
mainloop()