import tkinter as tk
import keycontrol as kct
import config

#Application with size and position, created in config.py
config.root.geometry("800x700+0+0")

#This box(a frame for you to live in) that is created in config.py
config.playground.grid(row=0,column=0)
for i in range(config.bordersize):
    border = tk.Label(config.playground,width=2,height=1,bg="grey")
    border.grid(column=i,row=0)
    if i >= 1:
        border = tk.Label(config.playground,width=2,height=1,bg="grey")
        border.grid(column=0,row=i)
        border = tk.Label(config.playground,width=2,height=1,bg="grey")
        border.grid(column=(config.bordersize-1),row=i)
        border = tk.Label(config.playground,width=2,height=1,bg="grey")
        border.grid(column=i,row=(config.bordersize-1))

#Setting walls
for i in config.wall:
    wall = tk.Label(config.playground,width=2,height=1,bg="grey")
    wall.grid(column=i[0],row=i[1])
        
#Hey it's you
config.player.grid(column=config.pos[0],row=config.pos[1])

#set key controls
kct.set_controls()

#the end
config.root.mainloop()
