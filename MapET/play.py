import os
import tkinter as tk
import input
import choosemap
import pickle

class PlayMap:
    def __init__(self, parent, mapname, objectcoord, objectcolor, playercoord, objecttypes, objecttypecolor, goalcoord, movekey):
        self.parent = parent
        self.mapname = mapname  
        self.playercoord = playercoord  # Spawn point for player
        self.speedmult = 1              # How far the player moves each press
        self.bordersize = 60            # Size of still screen (in terms of how many pixels is shown in each axis)
        self.zoomsize = 20              # Size of how much is shown when followig player
        self.pix = 10                   # Size of each pixel in screen
        #Camera position, top left from position of player
        self.camcoord = [self.playercoord[0] - self.zoomsize/2, self.playercoord[1] - self.zoomsize/2]
        self.objectcoord = objectcoord
        self.objectcolor = objectcolor
        self.objecttypes = objecttypes
        self.objecttypecolor = objecttypecolor
        self.goalcoord = goalcoord
        self.movekey = movekey
        self.follow = 0

        # Frame for this page
        self.mainframe = tk.Frame(self.parent,height=800,width=1200)
        self.mainframe.place(relx=.5,rely=.5,anchor='c')
        parent.backbtn.destroy()
        parent.backbuttonpage(self.mainframe)

        # Title of the map, that can be changed and saved
        self.mapnamelabel = tk.Label(self.mainframe,text=self.mapname,width=20,font=("Calibri",20))
        self.mapnamelabel.place(relx=0,rely=.02)

        # Playground Screen
        self.screen = tk.Canvas(self.mainframe, bg="Black", width=self.bordersize*self.pix, height=self.bordersize*self.pix, highlightthickness=0,bd=0)
        self.screen.place(relx=.5,rely=.5, anchor="c")
        self.set_map()

        # Frame for settings
        self.configframe = tk.Frame(self.mainframe)
        self.configframe.place(relx=0.05,rely=.2,anchor="nw")
        self.createconfig()

        # set key controls
        self.keyinput = input.SetPlayControls(self.parent,self.mainframe,self.screen,self.player,self.playercoord,self.speedmult,
                                              self.bordersize,self.zoomsize,self.camcoord,self.objectcoord,self.objectcolor,
                                              self.objecttypes,self.objecttypecolor,self.goalcoord,self.follow
                                              ,self.pix,self.playercoordxent,self.playercoordyent,self.speedmultent,
                                              self.bordersizexent,self.bordersizeyent,self.zoomsizeent,self.pixent,self.movekey)

        # Command buttons frame
        self.commandframe = tk.Frame(self.mainframe)
        self.commandframe.place(relx=.9,rely=.2,anchor="ne")

        # Button to switch camera to follow
        self.switch = tk.Button(self.commandframe,text="Switch to Follow", command=self.followswitch)
        self.switch.grid(row=0,pady=20)

#____________________________Functions__________________________________________________________________________________________________________________________________________________________    

    # Sets player at his coordinates
    def set_player(self):
        self.player = self.screen.create_rectangle(self.playercoord[0]*self.pix,self.playercoord[1]*self.pix,self.playercoord[0]*self.pix+self.pix,self.playercoord[1]*self.pix+self.pix,fill="red")

    # Sets objects with coordinates and colour
    def set_map(self):
        self.screen.delete(tk.ALL)
        self.set_player()
        for i in self.objectcoord:
            color = self.objectcolor[i[0],i[1]]
            self.screen.create_rectangle(i[0]*self.pix,i[1]*self.pix,i[0]*self.pix+self.pix,i[1]*self.pix+self.pix,fill=color,outline=color)
        for i in self.goalcoord:
            self.screen.create_rectangle(i[0]*self.pix,i[1]*self.pix,i[0]*self.pix+self.pix,i[1]*self.pix+self.pix,fill="lightgreen",outline="lightgreen")

    # Allows users to change settings/configurations
    def createconfig(self):
        # Change position of player
        self.playercoordlbl = tk.Label(self.configframe,text="Player Coord")
        self.playercoordlbl.grid(row=0,pady=20,sticky="w")
        self.playercoordxent = tk.Entry(self.configframe,width=5)
        self.playercoordxent.grid(column=1,row=0,pady=20,sticky="w")
        self.playercoordxent.insert(tk.END, self.playercoord[0])
        self.playercoordyent = tk.Entry(self.configframe,width=5)
        self.playercoordyent.grid(column=2,row=0,pady=20,sticky="w")
        self.playercoordyent.insert(tk.END, self.playercoord[1])
        
        # Change how far the player moves each press
        self.speedmultlbl = tk.Label(self.configframe,text="Speed Multiplier")
        self.speedmultlbl.grid(row=1,pady=20,sticky="w")
        self.speedmultent = tk.Entry(self.configframe,width=5)
        self.speedmultent.grid(column=1,row=1,pady=20,sticky="w")
        self.speedmultent.insert(tk.END, self.speedmult)
        
        # Change size of still screen
        self.bordersizelbl = tk.Label(self.configframe,text="Border Size")
        self.bordersizelbl.grid(row=2,pady=20,sticky="w")
        self.bordersizexent = tk.Entry(self.configframe,width=5)
        self.bordersizexent.grid(column=1,row=2,pady=20,sticky="w")
        self.bordersizexent.insert(tk.END, self.bordersize)
        self.bordersizeyent = tk.Entry(self.configframe,width=5)
        self.bordersizeyent.grid(column=2,row=2,pady=20,sticky="w")
        self.bordersizeyent.insert(tk.END, self.bordersize)
        
        # Change size of how much is shown during follow
        self.zoomsizelbl = tk.Label(self.configframe,text="Zoom Size")
        self.zoomsizelbl.grid(row=3,pady=20,sticky="w")
        self.zoomsizeent = tk.Entry(self.configframe,width=5)
        self.zoomsizeent.grid(column=1,row=3,pady=20,sticky="w")
        self.zoomsizeent.insert(tk.END, self.zoomsize)
        
        # Change size of each pixel
        self.pixlbl = tk.Label(self.configframe,text="Pixel Size")
        self.pixlbl.grid(row=4,pady=20,sticky="w")
        self.pixent = tk.Entry(self.configframe,width=5)
        self.pixent.grid(column=1,row=4,pady=20,sticky="w")
        self.pixent.insert(tk.END, self.pix)
        
    # toggle to switch
    def followswitch(self):
        if self.follow == 0:
            self.follow = 1
            # does the function in input, updating the screen before needing to move
            self.keyinput.cammove()
        else:
            self.set_player()
            self.follow = 0
            # recreate and update player and objects
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
