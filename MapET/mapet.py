#Create and edit maps

import tkinter as tk
import choosemap
import input
import play

class Mapedit:    
    def __init__(self,parent,gridsize,wallcoord):
        self.parent = parent
        self.gridsize = gridsize
        self.wallcoord = wallcoord
        self.screenwallcoord = wallcoord
        
        # Stores the last two coords selected
        self.end1 = 0
        self.end2 = 0

        # Label for displaying list of coords (should be removed before finalizing)
        self.showcoord = tk.Label(self.parent,text=self.wallcoord)
        self.showcoord.place(relx=.01,y=.9)

        # Frame for grid
        self.frame = tk.Frame(self.parent)
        self.frame.place(relx=0.5,rely=0.5, anchor="c")

        #----------------------------- MAP GRID ---------------------------------------------------------------
        # display axes
        self.gridaxisx = []
        self.gridaxisy = []
        self.xshift = self.yshift = 0   # set both shifts to 0, shifting moves the screen
        for i in range(self.bordersize):
            self.gridaxisx.append(tk.Label(self.frame,height=1,width=0,text=i+self.xshift,font=("Arial",8)))
            self.gridaxisy.append(tk.Label(self.frame,height=1,width=0,text=i+self.yshift,font=("Arial",8)))
            self.gridaxisx[i].grid(column=i+1,row=0)
            self.gridaxisy[i].grid(column=0,row=i+1)
        # display grid
        # Pix dictionary to store every pixel, c for index
        self.pix={}
        for y in range(self.bordersize):
            for x in range(self.bordersize):
                self.pix[x,y] = (tk.Label(self.frame,height=1,width=2,background="white",bd=2,relief="groove"))
                self.pix[x,y].grid(column=x+1,row=y+1)

        # Sets up previously created walls
        self.setwall()
        ################################ map grid #############################################################
        
        
        #----------------------------- BUTTONS ---------------------------------------------------------------
        # Button for updating new coord
        self.updatebutton = tk.Button(self.parent,text="Update new map",command=self.savemapcoord)
        self.updatebutton.place(relx=0.1,rely=0.05)

        # Button for switching to play mode(currently not working)
        self.switchbutton = tk.Button(self.parent,text="Switch to Play mode",command=self.switchplay)
        self.switchbutton.place(relx=.9,rely=.1)

        # Button for creating lines
        self.linebutton = tk.Button(self.parent,text="Make a line from last two points",command=self.createline)
        self.linebutton.place(relx=.9,rely=.2)

        # Set input
        input.SetEditControls(self.parent, self.bordersize, self.wallcoord, self.gridaxisx, self.gridaxisy, self.xshift, self.yshift, self.screenwallcoord, self.pix)
        ############################### buttons ##############################################################

#_Functions__________________________________________________________________________________________________________________________________________________________    

    # display existing walls in the grid
    def setwall(self):
        for walls in self.wallcoord:
            self.index = int(walls[0]) + (self.bordersize * walls[1])
            self.pix[x,y].config(bg="grey")

    # Update the new map coords into the list config.wallcoord
    def savemapcoord(self):
        self.tempwallcoord = []
        for x in range(self.gridsize):
            for 
            if self.pix[i].cget("bg") == "grey":
                xi = i
                yi = 0
                while xi >= self.bordersize:
                    xi -= self.bordersize
                    yi += 1
                coord = [int(xi),int(yi)]
                self.tempwallcoord.append(coord)
        self.wallcoord = self.tempwallcoord
        #Display the list of coords
        self.showcoord.config(text=self.wallcoord)


    # does nothing for now, but it should go to play
    def switchplay(self):
        self.parent.withdraw()
##        self.parent.deiconify()

    #Create a line between last two points if they are on the same line
    def createline(self):
        #Finding out which row
        if self.end1//self.bordersize == self.end2//self.bordersize:
            if self.end1 < self.end2:
                while self.end2-1 > self.end1:
                    self.end2 -= 1
                    self.pix[self.end2].config(bg="grey")
            if self.end1 > self.end2:
                while self.end2+1 < self.end1:
                    self.end2 += 1
                    self.pix[self.end2].config(bg="grey")        
        elif str(self.end1)[-1] == str(self.end2)[-1]:
            if self.end1 < self.end2:
                while self.end2-self.bordersize > self.end1:
                    self.end2 -= self.bordersize
                    self.pix[self.end2].config(bg="grey")
            if self.end1 > self.end2:
                while self.end2+self.bordersize < self.end1:
                    self.end2 += self.bordersize
                    self.pix[self.end2].config(bg="grey")

