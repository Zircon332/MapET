#Create and edit maps
import os
import tkinter as tk
import menu
import input_handling
import process1



class Mapedit:    
    def __init__(self,parent,mapname,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor):
        self.parent    =  parent
        self.gridsize  =  gridsize              # Number that represents the square size
        self.objectcoord = objectcoord          # Objects are stored as [xcoord, ycoord] (list)
        self.objectcolor = objectcolor          # Objects' color for each object (set)
        self.objecttypes = objecttypes          # List of object in the map
        self.objecttypecolor = objecttypecolor  # List of color of each object
        self.mapname   =  mapname               # Name of opened map
        
        # Stores the last two coords selected
        self.end1 = [0,0]
        self.end2 = [0,0]

        # Frame for this page
        self.mapeditframe = tk.Frame(self.parent,height=800,width=1200)
        self.mapeditframe.place(relx=.5,rely=.5,anchor='c')

        # Title of the map, that can be changed and saved
        self.mapnamelabel = tk.Label(self.mapeditframe,text=self.mapname,width=20,font=("Calibri",20))
        self.mapnamelabel.place(relx=.1,rely=.02)
        
        # Label for displaying list of coords (should be removed before finalizing)
        self.showcoord = tk.Label(self.mapeditframe,text=self.objectcoord)
        self.showcoord.place(relx=0.5,rely=.9,anchor="c")

        # Frame for grid
        self.gridframe = tk.Frame(self.mapeditframe)
        self.gridframe.place(relx=.5,rely=.5, anchor="c")
        self.createmapgrid()  # map the grid

        # Set input
        self.keyinput = input_handling.SetEditControls(self.mapeditframe, self.gridsize, self.objectcoord, self.objectcolor, self.objecttypes, self.objecttypecolor, self.gridaxisx, self.gridaxisy, self.xshift, self.yshift, self.pix, self.end1, self.end2)
        
        # Buttons
        self.btnframe = tk.Frame(self.mapeditframe)
        self.btnframe.place(relx=.9,rely=.2,anchor="ne")
        self.createbuttons()

        # Cell types select box
        self.typeframe = tk.Frame(self.mapeditframe)
        self.typeframe.place(relx=.15,rely=.2,anchor="n")
        self.createtypes()

#____________________________Functions__________________________________________________________________________________________________________________________________________________________    

    # Creates the center grid for mapedit
    def createmapgrid(self):
        # display axes
        self.gridaxisx = []
        self.gridaxisy = []
        self.xshift = self.yshift = 0   # initialize both shifts to 0, shifting moves the screen
        for i in range(self.gridsize):
            self.gridaxisx.append(tk.Label(self.gridframe,height=1,width=0,text=i+self.xshift,font=("Arial",8)))
            self.gridaxisy.append(tk.Label(self.gridframe,height=1,width=0,text=i+self.yshift,font=("Arial",8)))
            self.gridaxisx[i].grid(column=i+1,row=0)
            self.gridaxisy[i].grid(column=0,row=i+1)
            
        # display grid
        # Pix dictionary to store every pixel, c for index
        self.pix={}
        for y in range(self.gridsize):
            for x in range(self.gridsize):
                self.pix[x,y] = (tk.Label(self.gridframe,height=1,width=2,background="white",bd=2,relief="groove"))
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

        # Button for clearing everything in the grid
        self.clearbutton = tk.Button(self.btnframe,text="Clear walls",command=self.cleargrid)
        self.clearbutton.grid(row=3,pady=20,sticky="w")

        # Button for saving objects in the grid
        self.savebutton = tk.Button(self.btnframe,text="Save file",command=self.save)
        self.savebutton.grid(row=4,pady=20,sticky="w")

    # types of things that can be added to the map
    def createtypes(self):
        self.typename = []
        self.typeimg  = []
        self.typebtn  = []
        for i in range(len(self.objecttypes)):
            self.typename.append(tk.Label(self.typeframe,height=2,width=9,pady=1,text=self.objecttypes[i],font=("Calibri",15)))
            self.typeimg.append(tk.Label(self.typeframe,height=2,width=10,pady=2,bg=self.objecttypecolor[i]))
            self.typebtn.append(tk.Button(self.typeframe,height=2,width=10,pady=2,padx=1,text="Select",command=lambda i=i:self.selecttype(i)))
            self.typename[i].grid(row=i,column=0)
            self.typeimg[i].grid(row=i,column=1)
            self.typebtn[i].grid(row=i,column=2)

    # display existing walls in the grid
    def setwall(self):
        for objects in self.objectcoord:
            x = objects[0]
            y = objects[1]
            color = self.objectcolor[(x,y)]
            self.pix[x,y].config(bg=color)

    # Update the new map coords into the list config.objectcoord
    def savemapcoord(self):
        # Display the list of coords
        self.showcoord.config(text=self.keyinput.objectcoord)
        
    # does nothing for now, but it should go to play
    def switchplay(self):
        self.mapeditframe.destroy()
        self.pl = play.PlayMap(self.parent,self.objectcoord)

    # erase all coord in keyinput (cause everything is transfered there)
    def cleargrid(self):
        for x in range(self.keyinput.gridsize):
            for y in range(self.keyinput.gridsize):
                self.keyinput.pix[x,y].config(bg=self.objecttypecolor[0])
        del self.keyinput.objectcoord[:]
        self.keyinput.objectcolor.clear()

    def selecttype(self,index):
        self.keyinput.color = self.objecttypecolor[index]


    def save(self):
        with open(os.path.join("maps",self.mapname,"data.txt"),"w") as self.datamap:
            data = "PlayerCoord=" + "[2,2]" + \
                   ";\nGridsize=" + str(self.gridsize) + \
                   ";\nObjectCoord=" + str(self.keyinput.objectcoord) + \
                   ";\nObjectColor=" + str(self.keyinput.objectcolor) + \
                   ";\nObjecttypes=" + str(self.objecttypes) + \
                   ";\nObjectTypeColor=" + str(self.objecttypecolor)
            self.datamap.write(data)
