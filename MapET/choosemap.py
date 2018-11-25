import os
import ast
import tkinter as tk
import play
import mapet
import pickle

class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent         = parent
        self.parent.title("MapET")
        self.screen_width   = self.parent.winfo_screenwidth()
        self.screen_height  = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+%d+%d" % (self.screen_width,self.screen_height,0,0))
        self.parent.attributes("-fullscreen", False)
        self.creategui()

        self.movekey = 0    # initialise move key to decide which set of keys to use

    def creategui(self):    # Creates logo, menubar and buttons
        # MapET Logo Banner
        self.logoimg            = tk.PhotoImage(file="images/logo.gif")
        self.mapetlogo          =  tk.Label(self.parent, image=self.logoimg,anchor="c")
        self.mapetlogo.image    = self.logoimg

        self.buttonframe        = tk.Frame(self, bg="black", height=1920,width=100,)    # creates buttons and their frame, then place with function
        self.mapselectbtn       = tk.Button(self.buttonframe,text="Play Map",
                                    command=lambda:self.fileopening("mapselect"),
                                    width=12,padx=10,pady=20,font=("calibri",20))

        self.mapetbtn           = tk.Button(self.buttonframe,text="Map Editor",
                                    command=lambda:self.fileopening("mapeditor"),
                                    width=12,padx=10,pady=20,font=("calibri",20))

        self.settingsbtn        = tk.Button(self.buttonframe,text="Settings",
                                    command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))

        self.tutorialbtn        = tk.Button(self.buttonframe,text="Tutorial",
                                    command=lambda:self.tutorial(),
                                    width=12,padx=10,pady=20,font=("calibri",20))
                                    
        self.programexitbtn     = tk.Button(self.buttonframe, text="Quit",
                                     command=self.parent.destroy,
                                     width=12,padx=10,pady=20, font=("calibri",20))
        self.placegui()
    
    def tutorial(self):
        self.img            = tk.PhotoImage(file="images/tutorial.gif")
        self.tutorialpanel  = tk.Label(self.parent, image = self.img, anchor="c")
        self.tutorialpanel.place(relx=.5,rely=.5, anchor="c")

    def placegui(self):    # display main buttons
        self.mapetlogo.place(relx=.5, rely=.15, anchor="c")
        self.buttonframe.place(x=10,y=10, anchor="c", relx=0.48, rely=0.5)
        self.mapselectbtn.grid(row=0,ipadx=10,ipady=10)
        self.mapetbtn.grid(row=1,ipadx=10,ipady=10)
        self.settingsbtn.grid(row=2,ipadx=10,ipady=10)
        self.tutorialbtn.grid(row=3,ipadx=10,ipady=10)
        self.programexitbtn.grid(row=4,ipadx=10,ipady=10)

    
    def fileopening(self,file):    # #1-Hides Main buttons, #2-then display Settings buttons / #3-display Map Selection
        for child in self.buttonframe.winfo_children(): #1
            child.grid_forget()
        self.settingsbtn = tk.Button(self.buttonframe,text="Settings",    #2
                                    command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        if file == "settings":
            self.fullscreenbtn = tk.Button(self.buttonframe,text="Toggle Fullscreen",
                                    command=lambda:self.parent.attributes("-fullscreen",
                                    not self.parent.attributes('-fullscreen')),
                                    width=12,padx=10,pady=10, font=("calibri",20))
            self.fullscreenbtn.grid(row=0,ipadx=10,ipady=10,columnspan=2)
            self.movecontrols =  tk.Button(self.buttonframe,text="Move controls\n(↑ ↓ ← →)",command=lambda:self.changecontrol(),
                                        width=12,padx=10,pady=10, font=("calibri",20))
            self.movecontrols.grid(row=1,ipadx=10,ipady=10,column=0)
            self.backbtn = tk.Button(self.buttonframe, text="Back",command=lambda:self.settingback(),
                                        width=12,padx=10,pady=10, font=("calibri",20))
            self.backbtn.grid(row=3,ipadx=10,ipady=10,columnspan=2)
        else: #3
            self.mapetlogo.place_forget()
            self.buttonframe.place_forget()
            self.cm = ChooseMap(self, file, self.movekey) #calls choosemap

    # Hides Settings buttons and display Main buttons
    def settingback(self):
        self.fullscreenbtn.grid_forget()
        self.movecontrols.grid_forget()
        self.backbtn.grid_forget()
        self.placegui()

    def changecontrol(self):
        if self.movekey == 0:
            self.movecontrols.config(text="Move controls\n(W A S D)")
            self.movekey = 1
        elif self.movekey == 1:
            self.movecontrols.config(text="Move controls\n(↑W ↓S ←A →D)")
            self.movekey = 2
        elif self.movekey == 2:
            self.movecontrols.config(text="Move controls\n(↑ ↓ ← →)")
            self.movekey = 0

    def backbutton(self,frame):
        self.backbtn = tk.Button(self.parent, text="Back", command=lambda:deleteall(frame),width=12,padx=3,pady=3, font=("calibri",15))
        self.backbtn.place(anchor="nw", relx=0.02, rely=0.02)
        def deleteall(frame):
            frame.destroy()
            try:
                self.parent.win.destroy()
            except:
                pass
            self.backbtn.destroy()
            self.placegui()


class ChooseMap():
    def __init__(self, parent, file, movekey):
        self.parent = parent
        self.file = file
        self.movekey = movekey

        # container for this whole screen
        self.mainframe = tk.Frame(self.parent,width=1000,height=1000)
        self.mainframe.place(relx=.48,rely=.48, anchor="c")

        parent.backbutton(self.mainframe)

        ## Display files in folder
        # list of all files
        self.maps = os.listdir("maps")
        # creating lists to contain every file
        self.mapbox  =  []
        self.mapimg  =  []
        self.maptext =  []
        self.mapbtn  =  []
        self.coli    =  0
        self.rowi    =  0
        # append files as frames
        if len(self.maps) > 7:
            pad = 0
            limit = 6
        else:
            pad = 50
            limit = 4
        for i in range(len(self.maps)+1):
            if i < len(self.maps):
                mapname = str(self.maps[i])
                self.mapbox.append(tk.Frame(self.mainframe,width=200,height=200,bd=1,padx=pad,pady=pad))
                try:
                    self.banner = tk.PhotoImage(file=os.path.join("maps",mapname,"banner.gif"))
                    self.mapimg.append(tk.Label(self.mapbox[i],width=200,height=100,image=self.banner))
                    self.mapimg[i].image = self.banner
                except:
                    self.mapimg.append(tk.Label(self.mapbox[i],width=20,height=10,bg="white"))
                self.maptext.append(tk.Label(self.mapbox[i],text=mapname,width=10,height=1,font=("arial",20)))
                self.mapbtn.append(tk.Button(self.mapbox[i],text="Choose map",width=10,height=1,command=lambda m=mapname:self.openmap(m),font=("arial",15)))
                # get the banner img of the mapfile, if any

            else:
                # create-new-map frame
                self.mapbox.append(tk.Frame(self.mainframe,width=200,height=200,bd=1,padx=pad,pady=pad))
                self.mapimg.append(tk.Label(self.mapbox[i],width=20,height=10,bg="grey"))
                self.maptext.append(tk.Label(self.mapbox[i],text="Create New",width=10,height=1,font=("arial",20)))
                self.mapbtn.append(tk.Button(self.mapbox[i],text="Choose map",width=10,height=1,command=self.createmap,font=("arial",15)))
            # grid them
            self.mapbox[i].grid(column=self.coli,row=self.rowi)
            self.mapimg[i].grid(row=1)
            self.maptext[i].grid(row=2)
            self.mapbtn[i].grid(row=3)
            # count each column, when column reach 4, start next row
            self.coli += 1
            if self.coli == limit:
                self.coli = 0
                self.rowi += 1
                
    # Opens selected file, hide map select container, display play/mapet
    def openmap(self,mapname):
        print("Loading file information...")
        try:
            with open(os.path.join("maps",mapname,"data.txt"),"r") as self.datamap:
                data = self.datamap.read().split(";")
            for i in data:
                print(i,end="")
            playercoord     =   ast.literal_eval(data[0].split("=")[1])       # ast converts strings back to lists/dictionaries
            gridsize        =   ast.literal_eval(data[1].split("=")[1])
            objectcoord     =   ast.literal_eval(data[2].split("=")[1])
            objectcolor     =   ast.literal_eval(data[3].split("=")[1])
            objecttypes     =   ast.literal_eval(data[4].split("=")[1])
            objecttypecolor =   ast.literal_eval(data[5].split("=")[1])
            goalcoord       =   ast.literal_eval(data[6].split("=")[1])

            # Start play/mapedit with stored data
            print("\n\nOpening",mapname)
            if self.file == "mapselect":
                self.mainframe.place_forget()
                self.pl = play.PlayMap(self.parent,mapname,objectcoord,objectcolor,playercoord,objecttypes,objecttypecolor,goalcoord,self.movekey)
            elif self.file == "mapeditor":
                self.mainframe.place_forget()
                self.mp = mapet.Mapedit(self.parent,mapname,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor,goalcoord,self.movekey)

        except:
            print("File does not exist, or is corrupted. Make sure to save before exiting.")

    # Function to create new map
    def createmap(self):
        def replace(warnroot,mapname):
            playercoord = [2,2]                                                                     # Default coord at 2,2
            objecttypes = ("land", "water", "walls", "lava", "tree", "deep water", "space", "log")  # Default object list
            objecttypecolor = ("white", "cyan", "grey", "red", "green", "blue", "black", "brown")   # Default colors for objects 
            goalcoord = []

            for i in os.listdir(os.path.join("maps",mapname)):
                os.remove(os.path.join("maps",mapname,i))
            os.rmdir(os.path.join("maps",mapname))      # remove old folder
            os.mkdir(os.path.join("maps",mapname))      # create new folder

            newmaproot.destroy()
            warnroot.destroy()

            # Start mapedit/play with default/empty data
            if self.file == "mapselect":
                self.mainframe.place_forget()
                self.pl = play.PlayMap(self.parent,mapname,[],{},playercoord,objecttypes,objecttypecolor,goalcoord,self.movekey)
            elif self.file == "mapeditor":
                self.mainframe.place_forget()
                self.mp = mapet.Mapedit(self.parent,mapname,20,[],{},objecttypes,objecttypecolor,goalcoord,self.movekey)
        
        # private function for button when creating map
        def makenewmap():
            # Iniaializing variables 
            mapname = entry.get()                                                                   # Get the entered map name
            playercoord = [2,2]                                                                     # Default coord at 2,2
            objecttypes = ("land", "water", "walls", "lava", "tree", "deep water", "space", "log")  # Default object list
            objecttypecolor = ("white", "cyan", "grey", "red", "green", "blue", "black", "brown")   # Default colors for objects
            goalcoord = []
        
            # create a directory for the map, if it already exists, ask if replace
            try:
                # Make new dir
                os.mkdir(os.path.join("maps",mapname))

                # Destroy the popup
                newmaproot.destroy()

                # Start play/mapedit with empty/default data
                if self.file == "mapselect":
                    self.mainframe.place_forget()
                    self.pl = play.PlayMap(self.parent,mapname,[],{},playercoord,objecttypes,objecttypecolor,goalcoord,self.movekey)
                elif self.file == "mapeditor":
                    self.mainframe.place_forget()
                    self.mp = mapet.Mapedit(self.parent,mapname,20,[],{},objecttypes,objecttypecolor,goalcoord,self.movekey)

            # popup root when file already exists
            except FileExistsError:
                warnroot = tk.Tk()
                warnroot.geometry("300x100+550+300")
                warning = tk.Label(warnroot, text="File already exists, do you want to replace it?",font=("calibri",12))
                warning.grid(row=0,columnspan=2)
                yesbtn = tk.Button(warnroot, text="Replace",command=lambda name=mapname:replace(warnroot,name),font=("calibri",12))
                yesbtn.grid(row=1,column=0)
                cancelbtn = tk.Button(warnroot, text="Cancel",command=lambda:warnroot.destroy(),font=("calibri",12))
                cancelbtn.grid(row=1,column=1)
                warnroot.mainloop()

            except:
                print("Error in naming. Choose a name that doesn't contain these 3 characters \n \" ' \\ ")

        # create tk for inputting name
        newmaproot = tk.Tk()
        newmaproot.geometry("300x200+500+250")
        text = tk.Label(newmaproot,text="Enter the name of the map",width=25,font=("calibri",15))
        text.grid(row=0,pady=5)
        entry = tk.Entry(newmaproot,width=25,font=("calibri",15))
        entry.grid(row=1,pady=5)
        entry.focus_set()
        button = tk.Button(newmaproot,text="Done",command=makenewmap,font=("calibri",15))
        button.grid(row=2,pady=5)
        
