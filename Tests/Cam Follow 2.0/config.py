#This module contains all the variables that will be shared between modules
#

import tkinter as tk

#Start position and speed mult
pos = [6,6]
speed_mult = 1

#Set border size
bordersize = 50
zoomsize = 5

#Camera from position of player, top left
camcoord = [pos[0]-zoomsize/2, pos[1]-zoomsize/2]

#Declaring interactive things
root = tk.Tk()
root.title("Map Play")

#getting screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = str(screen_width) + "x" + str(screen_height)

screen = tk.Canvas(root, bg="Black", width=bordersize*10, height=bordersize*10, highlightthickness=0,bd=0)

#list of all coords that are walls, excluding border, can be negative
wallcoord = [[0, 0]]

#Empty screen wall coords that keeps track of what should be displayed 
screen_wallcoord = []

follow = 0

