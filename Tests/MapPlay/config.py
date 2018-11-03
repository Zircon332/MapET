#This module contains all the variables that will be shared between modules
#

import tkinter as tk

#Start position
pos = [5,5]

#Declaring interactive things
root = tk.Tk()
root.title("Map Play")

#getting screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_size = str(screen_width) + "x" + str(screen_height)

playground = tk.Frame(root, bd=1, bg="Black",width=1000,height=1000)
player = tk.Label(playground,width=4,height=2,bg="red")
minimap = tk.Frame(root, bd=1, bg="Black", width=500, height=500)
miniplayer = tk.Label(minimap,width=2,height=1,bg="red",text="A")

#Set border size
bordersize = 20

#list of all coords that are walls, excluding border
wallcoord = [[0, 0]]
wall=[]
c = 0

    
