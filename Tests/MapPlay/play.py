import os
import tkinter as tk
import keycontrol as kct
import config
import mapedit
import pickle
from tkinter import messagebox

#Application with size and position, created in config.py
config.root.geometry(config.screen_size)

#This box(a frame for you to live in) that is created in config.py
config.playground.grid(row=0,column=0)
#Creates the border
for i in range(config.bordersize):
    border = tk.Label(config.playground,width=4,height=2,bg="grey")
    border.grid(column=i,row=0)
    if i >= 1:
        border = tk.Label(config.playground,width=4,height=2,bg="grey")
        border.grid(column=0,row=i)
        border = tk.Label(config.playground,width=4,height=2,bg="grey")
        border.grid(column=(config.bordersize-1),row=i)
        border = tk.Label(config.playground,width=4,height=2,bg="grey")
        border.grid(column=i,row=(config.bordersize-1))

def switchmap():
    config.root.withdraw()
    mapedit.mapedit()
#Buttons for Toggle between map editor and map play
switchbutton = tk.Button(config.root,text="Switch to Map Editor",command=switchmap)
switchbutton.place(x=700,y=50)

#Setting the map
c = 0
prompt = 0
def set_map_prompt():
    global prompt
    if prompt == 0:
        prompt += 1
        setmapprompt.config(text="Pressing this button again will set the map.\nWhat was previously in the map would be erased")
    else:
        prompt = 0
        set_map()
        setmapprompt.config(text="")    
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
setmapbtn = tk.Button(config.root,text="Set the map", command=set_map_prompt)
setmapbtn.place(x=700,y=100)
setmapprompt = tk.Label(config.root,text="")
setmapprompt.place(x=780,y=100)

#Button for savefile
savebtn = tk.Button(config.root,text="Save map",command=kct.save)
savebtn.place(x=700,y=200)

#List of files
config.filelist = tk.Listbox(config.root)
config.filelist.place(x=700,y=300)

config.filename = os.listdir("data")

def set_map_from_file():
    try:
        config.filelist.curselection()[0]
        config.wallcoord = pickle.load(open(os.path.join(os.path.expanduser('~'),'Desktop\MapET\Tests\MapPlay\data',"DamienFace.p"),"rb"))
        set_map()
    except:
        loadmapprompt.config(text="No selected map")
        
#Button for loadfile
loadbtn = tk.Button(config.root,text="Load selected map",command=set_map_from_file)
loadbtn.place(x=700,y=250)

#Prompt for load
loadmapprompt = tk.Label(config.root,text="")
loadmapprompt.place(x=810,y=250)

for item in config.filename:
    config.filelist.insert(tk.END,item)
    
#Hey it's you
config.player.grid(column=config.pos[0],row=config.pos[1])


#Minimap
config.minimap.place(x=1000,y=0)
for i in range(config.bordersize):
    border = tk.Label(config.minimap,width=2,height=1,bg="grey")
    border.grid(column=i,row=0)
    if i >= 1:
        border = tk.Label(config.minimap,width=2,height=1,bg="grey")
        border.grid(column=0,row=i)
        border = tk.Label(config.minimap,width=2,height=1,bg="grey")
        border.grid(column=(config.bordersize-1),row=i)
        border = tk.Label(config.minimap,width=2,height=1,bg="grey")
        border.grid(column=i,row=(config.bordersize-1))
config.miniplayer.grid(column=config.pos[0],row=config.pos[1])

#set key controls
kct.set_controls()


#Before closing, save the file 
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        config.root.destroy()

config.root.protocol("WM_DELETE_WINDOW", on_closing)

#the end
config.root.mainloop()
