import os
import tkinter as tk
import keycontrol as kct
import config
import mapedit
import pickle
from tkinter import messagebox

#Application with size and position, created in config.py
config.root.geometry(config.screen_size)

#menu button
##menu = tk.Menubutton(config.root,text="File",relief=tk.RAISED)
##menu.place(x=1,y=1)
##menu.menu1 = tk.Menu(menu,tearoff=0)
##menu["menu1"] = menu.menu1
##menu.menu1.add_checkbutton(label="Sup")

#This box(a frame for you to live in) that is created in config.py
config.playground.place(x=0,y=30)
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
    set_minimap()
        
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

def set_map_from_file():
    try:
        config.wallcoord = pickle.load(open("data\DamienFace.p","rb"))
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

def set_miniwall():
    border = config.minimap.create_rectangle(0,0,200,10,fill="grey",outline="grey")
    border = config.minimap.create_rectangle(0,0,10,200,fill="grey",outline="grey")
    border = config.minimap.create_rectangle(190,0,200,200,fill="grey",outline="grey")
    border = config.minimap.create_rectangle(0,190,200,200,fill="grey",outline="grey")
    config.miniplayer = config.minimap.create_rectangle(config.pos[0]*10,config.pos[1]*10,config.pos[0]*10+10,config.pos[1]*10+10,fill="red")
  
def set_minimap():
    config.minimap.delete(tk.ALL)
    set_miniwall()
    for i in config.wallcoord:
        config.minimap.create_rectangle(i[0]*10,i[1]*10,i[0]*10+10,i[1]*10+10,fill="grey",outline="grey")

#Minimap
config.minimap.place(x=1200,y=0)
set_miniwall()

#Minimap 2
def set_miniwall2():
    border = config.minimap2.create_rectangle(0,0,20,1,fill="grey",outline="grey")
    border = config.minimap2.create_rectangle(0,0,1,20,fill="grey",outline="grey")
    border = config.minimap2.create_rectangle(19,0,20,20,fill="grey",outline="grey")
    border = config.minimap2.create_rectangle(0,19,20,20,fill="grey",outline="grey")
    config.miniplayer2 = config.minimap2.create_rectangle(config.pos[0],config.pos[1],config.pos[0]+1,config.pos[1]+1,fill="white",outline="white")
  
def set_minimap2():
    config.minimap2.delete(tk.ALL)
    set_miniwall2()
    for i in config.wallcoord:
        config.minimap2.create_rectangle(i[0],i[1],i[0]+10,i[1]+10,fill="grey",outline="grey")

config.minimap2.place(x=1200,y=300)
set_miniwall2()


#set key controls
kct.set_controls()

#Before closing, save the file 
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        config.root.destroy()

config.root.protocol("WM_DELETE_WINDOW", on_closing)


#the end
config.root.mainloop()
