import os
import tkinter as tk
import input
import config
import pickle

class playgui:
    def __init__(self, parent, mapname):
        self.parent = parent
        self.playercoord = [2,2]
        self.speedmult = 1
        self.bordersize = 50
        self.zoomsize = 10
        self.camcoord = [self.playercoord[0] - self.zoomsize/2, self.playercoord[1] - self.zoomsize/2]
        self.wallcoord = []
        self.screenwallcoord = []
        self.follow = 0
        
        #Set map coords from file
        self.wallcoord = pickle.load(open(os.path.join('data',mapname),"rb"))


        #Playground Screen
        self.screen = tk.Canvas(self.parent, bg="Black", width=self.bordersize*10, height=self.bordersize*10, highlightthickness=0,bd=0)
        self.screen.place(relx=.1,rely=.1)
        self.set_map()
    
        #set key controls
        self.keyinput = input.set_controls(self.parent,self.screen,self.player,self.playercoord,self.speedmult,self.bordersize,self.zoomsize,self.camcoord,self.wallcoord,self.screenwallcoord,self.follow)

        #Switch cam to follow
        self.switch = tk.Button(self.parent,text="Switch to Follow", command=self.followswitch)
        self.switch.place(relx=.9,rely=.1)
        

    def set_map(self):
        self.screen.delete(tk.ALL)
        self.set_wall()
        for i in self.wallcoord:
            self.screen.create_rectangle(i[0]*10,i[1]*10,i[0]*10+10,i[1]*10+10,fill="grey",outline="grey")

    def set_wall(self):
        self.bds = self.bordersize * 10
        self.border = self.screen.create_polygon([0,0,self.bds,0,self.bds,self.bds,0,self.bds,0,0,10,0,10,self.bds-10,self.bds-10,self.bds-10,self.bds-10,10,0,10],fill="grey",outline="grey")
        self.player = self.screen.create_rectangle(self.playercoord[0]*10,self.playercoord[1]*10,self.playercoord[0]*10+10,self.playercoord[1]*10+10,fill="red")

    def followswitch(self):
        if self.follow == 0:
            self.follow = 1
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
            self.follow = 0
            self.set_map()
        #Update follow value in keyinput
        self.keyinput.follow = self.follow
        

#Runs the class
def playgamef(root):
    playgui(root,"DamienFace.p")


