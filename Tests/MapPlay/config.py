#This module contains all the variables that will be shared between modules

import tkinter as tk

posx = 5
posy = 5
root = tk.Tk()
playground = tk.Frame(root, bd=1, bg="Black",width=1000,height=1000)
player = tk.Label(playground,width=2,height=1,bg="red")

