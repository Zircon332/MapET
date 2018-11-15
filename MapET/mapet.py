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
        
        # Stores the last two coords selected
        self.end1 = [0,0]
        self.end2 = [0,0]

        self.mapname = tk.Entry(self.parent,width=20,text="EnterName")
        self.mapname.place(relx=.3,rely=.1)

        # Label for displaying list of coords (should be removed before finalizing)
        self.showcoord = tk.Label(self.parent,text=self.wallcoord)
        self.showcoord.place(relx=.1,y=.9)

        # Frame for grid
        self.frame = tk.Frame(self.parent)
        self.frame.place(relx=0.5,rely=0.5, anchor="c")
        self.createmapgrid()  # map the grid

        # Set input
        self.keyinput = input.SetEditControls(self.parent, self.gridsize, self.wallcoord, self.gridaxisx, self.gridaxisy, self.xshift, self.yshift, self.pix, self.end1, self.end2)
        
        # Buttons
        self.btnframe = tk.Frame(self.parent)
        self.btnframe.place(relx=.9, rely=.2, anchor="ne")
        self.createbuttons()

        # Cell types select box
        self.types = ["land","water","walls","lava","home","goal","spikes","door"]
        self.typecolor = ["white","cyan","grey","red","green","blue","black","brown"]
        self.typeframe = tk.Frame(self.parent)
        self.typeframe.place(relx=.15, rely=.2, anchor="n")
        self.createtypes()

#____________________________Functions__________________________________________________________________________________________________________________________________________________________    

    # Creates the center grid for mapedit
    def createmapgrid(self):
        # display axes
        self.gridaxisx = []
        self.gridaxisy = []
        self.xshift = self.yshift = 0   # initialize both shifts to 0, shifting moves the screen
        for i in range(self.gridsize):
            self.gridaxisx.append(tk.Label(self.frame,height=1,width=0,text=i+self.xshift,font=("Arial",8)))
            self.gridaxisy.append(tk.Label(self.frame,height=1,width=0,text=i+self.yshift,font=("Arial",8)))
            self.gridaxisx[i].grid(column=i+1,row=0)
            self.gridaxisy[i].grid(column=0,row=i+1)
        # display grid
        # Pix dictionary to store every pixel, c for index
        self.pix={}
        for y in range(self.gridsize):
            for x in range(self.gridsize):
                self.pix[x,y] = (tk.Label(self.frame,height=1,width=2,background="white",bd=2,relief="groove"))
                self.pix[x,y].grid(column=x+1,row=y+1)

        # Sets up previously created walls
        self.setwall()

    def createbuttons(self):
        # Button for updating new coord
        self.updatebutton = tk.Button(self.btnframe,text="Update new map",command=self.savemapcoord)
        self.updatebutton.grid(row=0,pady=20,sticky="w")

        # Button for switching to play mode(currently not working)
        self.switchbutton = tk.Button(self.btnframe,text="Switch to Play mode",command=self.switchplay)
        self.switchbutton.grid(row=1,pady=20,sticky="w")

        # Button for creating lines
        self.linebutton = tk.Button(self.btnframe,text="Make a line from last two points",command=self.keyinput.createline)
        self.linebutton.grid(row=2,pady=20,sticky="w")

        self.clearbutton = tk.Button(self.btnframe,text="Clear walls",command=self.cleargrid)
        self.clearbutton.grid(row=3,pady=20,sticky="w")

    # types of things that can be added to the map
    def createtypes(self):
        self.typename = []
        self.typeimg = []
        self.typebtn = []
        for i in range(len(self.types)):
            self.typename.append(tk.Label(self.typeframe,height=2,width=9,pady=1,text=self.types[i],font=("Calibri", 15)))
            self.typeimg.append(tk.Label(self.typeframe,height=2,width=10,bg=self.typecolor[i],pady=2))
            self.typebtn.append(tk.Button(self.typeframe,height=2,width=10,pady=2,padx=1,text="Select",command=lambda i=i:self.selecttype(i)))
            self.typename[i].grid(row=i, column=0)
            self.typeimg[i].grid(row=i, column=1)
            self.typebtn[i].grid(row=i, column=2)


    # display existing walls in the grid
    def setwall(self):
        for walls in self.wallcoord:
            x = walls[0]
            y = walls[1]
            self.pix[x,y].config(bg="grey")

    # Update the new map coords into the list config.wallcoord
    def savemapcoord(self):
        #Display the list of coords
        self.showcoord.config(text=self.keyinput.wallcoord)

    # does nothing for now, but it should go to play
    def switchplay(self):
        self.frame.destroy()
        self.showcoord.destroy()
        self.typeframe.destroy()
        self.btnframe.destroy()
        self.pl = play.PlayMap(self.parent, self.wallcoord)

    # erase all coord in keyinput (cause everything is transfered there)
    def cleargrid(self):
        for x in range(self.keyinput.gridsize):
            for y in range(self.keyinput.gridsize):
                self.keyinput.pix[x,y].config(bg="white")
        del self.keyinput.wallcoord[:]

    def selecttype(self,index):
        self.keyinput.color = self.typecolor[index]
