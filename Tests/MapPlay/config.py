#This module contains all the variables that will be shared between modules
#

import tkinter as tk

#Start position and speed mult
pos = [1,1]
speed_mult = 1

#Set border size
bordersize = 20

#Declaring interactive things
root = tk.Tk()
root.title("Map Play")

#getting screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = str(screen_width) + "x" + str(screen_height)

playground = tk.Frame(root, bd=1, bg="Black",width=1000,height=1000)
player = tk.Label(playground,width=2,height=1,bg="red")
minimap = tk.Canvas(root, bg="Black", width=200, height=200, highlightthickness=0,bd=0)
minimap2 = tk.Canvas(root, bg="Black", width=20, height=20, highlightthickness=0,bd=0)

#list of all coords that are walls, excluding border
wallcoord = [[0, 0]]
wall=[]
c = 0

    
