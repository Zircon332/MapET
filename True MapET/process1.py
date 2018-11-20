import os
import tkinter as tk
import input_handling
import menu
import process2

class PlayMap:
    def __init__(self, parent , mapname , objectcoord , objectcolor , playercoord , objecttypes , objecttypecolor):
        self.parent = parent
        self.mapname = mapname
        self.playercoord = playercoord
        self.speedmult = 1
        self.bordersize = 50
        self.zoomsize = 10
        #Camera position, top left from position of player
        self.camcoord = [self.playercoord[0] - self.zoomsize/2, self.playercoord[1] - self.zoomsize/2]
        self.wallcoord = wallcoord
        self.screenwallcoord = []
        self.follow = 0
    
        #Playground Screen
        self.screen = tk.Canvas(self.parent, bg="Black", width=self.bordersize*10, height=self.bordersize*10, highlightthickness=0,bd=0)
        self.screen.place(relx=.1,rely=.1)
        self.set_map()

        #set key controls
        self.keyinput = input_handling.SetPlayControls(self.parent,self.screen,self.player,self.playercoord,self.speedmult,self.bordersize,self.zoomsize,self.camcoord,self.wallcoord,self.screenwallcoord,self.follow)

        #Switch cam to follow
        self.switch = tk.Button(self.parent,text="Switch to Follow", command=self.followswitch)
        self.switch.place(relx=.9,rely=.1)

    def set_map(self):
        self.screen.delete(tk.ALL)
        self.set_wall()
        for i in self.wallcoord:
            self.screen.create_rectangle(i[0]*10,i[1]*10,i[0]*10+10,i[1]*10+10,fill="grey",outline="grey")

    # sets walls and player
    def set_wall(self):
        self.bds = self.bordersize * 10
        self.border = self.screen.create_polygon([0,0,self.bds,0,self.bds,self.bds,0,self.bds,0,0,10,0,10,self.bds-10,self.bds-10,self.bds-10,self.bds-10,10,0,10],fill="grey",outline="grey")
        self.player = self.screen.create_rectangle(self.playercoord[0]*10,self.playercoord[1]*10,self.playercoord[0]*10+10,self.playercoord[1]*10+10,fill="red")

    # toggle to switch
    def followswitch(self):
        if self.follow == 0:
            self.follow = 1
            # does the function in input, updating the screen before needing to move
            for i in self.wallcoord:
                self.screenx = i[0] - self.camcoord[0]
                self.screeny = i[1] - self.camcoord[1]
                if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                    self.screenwallcoord.append([self.screenx,self.screeny])
            self.zoomratio = 10 * self.bordersize / self.zoomsize
            self.screen.delete(tk.ALL)
            self.player = self.screen.create_rectangle(self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,fill="red")
            for i in self.screenwallcoord:
                self.screen.create_rectangle(i[0]*self.zoomratio,i[1]*self.zoomratio,i[0]*self.zoomratio+self.zoomratio,i[1]*self.zoomratio+self.zoomratio,fill="grey",outline="grey")
            del self.screenwallcoord[:]
        else:
            self.set_wall()
            self.follow = 0
            # recreate and update player and walls
            self.set_map()
            self.keyinput.player = self.player
        #Update follow value in keyinput
        self.keyinput.follow = self.follow


    def save(self):
        with open(os.path.join("maps",self.mapname,"data.txt"),"w") as self.datamap:
            self.datamap.write(self.mapname)
            self.datamap.write(self.bgcolor)

        # Saves the location where the character is before quitting
        with open(os.path.join("maps",self.mapname,"playerdata.txt"),"w") as self.playerdata:
            self.playerdata.write(self.playercoord)
