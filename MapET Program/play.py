import os
import tkinter as tk
import input
import config
import pickle

class PlayGame:
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.attributes("-fullscreen", False)
        self.createguif()
    #Setting the map
    def set_map():
        config.screen.delete(tk.ALL)
        set_wall()
        for i in config.wallcoord:
            config.screen.create_rectangle(i[0]*10,i[1]*10,i[0]*10+10,i[1]*10+10,fill="grey",outline="grey")

    def set_wall():
        bds = config.bordersize * 10
        border = config.screen.create_polygon([0,0,bds,0,bds,bds,0,bds,0,0,10,0,10,bds-10,bds-10,bds-10,bds-10,10,0,10],fill="grey",outline="grey")
        config.player = config.screen.create_rectangle(config.pos[0]*10,config.pos[1]*10,config.pos[0]*10+10,config.pos[1]*10+10,fill="red")

    def followswitch():
        if config.follow == 0:
            config.follow = 1
            for i in config.wallcoord:
                screenx = i[0] - config.camcoord[0] 
                screeny = i[1] - config.camcoord[1]
                if screenx >= 0 and screenx <= config.zoomsize and screeny >= 0 and screeny <= config.zoomsize:
                    config.screen_wallcoord.append([screenx,screeny])
            zoomratio = 10 * config.bordersize / config.zoomsize
            config.screen.delete(tk.ALL)
            config.player = config.screen.create_rectangle(config.zoomsize/2*zoomratio,config.zoomsize/2*zoomratio,config.zoomsize/2*zoomratio+zoomratio,config.zoomsize/2*zoomratio+zoomratio,fill="red")
            for i in config.screen_wallcoord:
                config.screen.create_rectangle(i[0]*zoomratio,i[1]*zoomratio,i[0]*zoomratio+zoomratio,i[1]*zoomratio+zoomratio,fill="grey",outline="grey")
            del config.screen_wallcoord[:]
        else:
            config.follow = 0
            set_map()
            
    #Set map coords from file
    # config.wallcoord = pickle.load(open(os.path.join(os.path.expanduser('~'),'Desktop\MapET\Tests\MapPlay\data',"DamienFace.p"),"rb"))

    #Application with size and position, created in config.py
    config.root.geometry(config.screen_size)

    #Playground
    config.screen.place(x=10,y=10)
    set_map()

    #set key controls
    input.set_controls()

    switch = tk.Button(config.root,text="Switch to Follow", command=followswitch)
    switch.place(x=700,y=100)

    config.root.mainloop()
