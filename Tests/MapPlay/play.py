import tkinter as tk
import keycontrol as kct
import config

#Application with size and position

config.root.geometry("800x700+0+0")

#This box(a frame for you to live in)
config.playground.grid(row=0,column=0)
for i in range(20):
    gridder = tk.Label(config.playground,width=2,height=1,bg="grey")
    gridder.grid(column=i,row=0)
for i in range(20):
    gridder = tk.Label(config.playground,width=2,height=1,bg="grey")
    gridder.grid(column=0,row=i)

#Hey it's you
config.player.grid(column=config.posx,row=config.posy)

#set key controls
kct.set_controls()

#the end
config.root.mainloop()
