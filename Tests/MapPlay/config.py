#This module contains all the variables that will be shared between modules
#

import tkinter as tk

#Start position
pos = [5,5]

#Declaring interactive things
root = tk.Tk()
playground = tk.Frame(root, bd=1, bg="Black",width=1000,height=1000)
player = tk.Label(playground,width=2,height=1,bg="red")

#Set border size
bordersize = 100

#list of all coords that are walls, excluding border
wall = [[10,10],[15,4],[9,10],[14,10],[14,11],[14,12],[13,12],[8,3]]
