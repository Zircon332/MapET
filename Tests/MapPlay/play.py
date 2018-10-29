import tkinter as tk
import keycontrol as kct
import config
import mapedit

#Application with size and position, created in config.py
config.root.geometry("800x700+0+0")

#This box(a frame for you to live in) that is created in config.py
config.playground.grid(row=0,column=0)
#Creates the border
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
#Fill in the rest
##mapgrid = []
##c = 0
##for x in range(1,config.bordersize-1):
##    for y in range(1,config.bordersize-1):
##        mapgrid.append(tk.Label(config.playground,width=2,height=1,bg="white"))
##        mapgrid[c].grid(column=x,row=y)
##        c += 1


def switchmap():
    config.root.withdraw()
    mapedit.mapedit()
#Buttons for Toggle between map editor and map play
switchbutton = tk.Button(config.root,text="Switch to Map Editor",command=switchmap)
switchbutton.place(x=500,y=50)

#Setting the map
c = 0
def set_map():
    global c
    if c > 0:
        for i in range(c):
            config.wall[i].grid_remove()
    c = 0
    for i in config.wallcoord:
        config.wall.append(tk.Label(config.playground,width=2,height=1,bg="grey"))
        config.wall[c].grid(column=i[0],row=i[1])
        c += 1
setmapbtn = tk.Button(config.root,text="Set the map", command=set_map)
setmapbtn.place(x=500,y=100)

#Hey it's you
config.player.grid(column=config.pos[0],row=config.pos[1])

#set key controls
kct.set_controls()

#the end
config.root.mainloop()
