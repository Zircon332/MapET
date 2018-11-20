import os
import ast
from tkinter import filedialog
import tkinter as tk
import process1
import process2


class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("MapET")
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+%d+%d" % (self.screen_width,self.screen_height,0,0))
        self.parent.attributes("-fullscreen", False)
        self.creategui()

    def creategui(self):    # Creates logo, menubar and buttons
        # MapET Logo Banner
        self.logoimg = tk.PhotoImage(file="images/logo.gif")
        self.mapetlogo =  tk.Label(self.parent, image=self.logoimg,anchor="c")
        self.mapetlogo.image = self.logoimg

        # Menu bar
        self.menubar = tk.Menu(self.parent)
        # 'File' Menu Bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=lambda:self.filedialog())
        self.filemenu.add_command(label="Save",  command=lambda:print("test"))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.buttonframe = tk.Frame(self, bg="black", height=1920,width=100)    # creates buttons and their frame, then place with function
        self.mapselectbtn = tk.Button(self.buttonframe,text="Play Map",
                                    command=lambda:self.fileopening("mapselect"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.mapetbtn = tk.Button(self.buttonframe,text="Map Editor",
                                    command=lambda:self.fileopening("mapeditor"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.settingsbtn = tk.Button(self.buttonframe,
                                    text="Settings",command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.programexitbtn = tk.Button(self.buttonframe, text="Quit",
                                     command=self.parent.destroy,
                                     width=12,padx=10,pady=20, font=("calibri",20))
        self.placegui()

    def placegui(self):    # display main buttons
        self.mapetlogo.place(relx=.5, rely=.15, anchor="c")
        self.buttonframe.place(x=10,y=10, anchor="c", relx=0.48, rely=0.5)
        self.mapselectbtn.grid(row=0,ipadx=10,ipady=10)
        self.mapetbtn.grid(row=1,ipadx=10,ipady=10)
        self.settingsbtn.grid(row=2,ipadx=10,ipady=10)
        self.programexitbtn.grid(row=3,ipadx=10,ipady=10)

    
    def fileopening(self,file):    # #1-Hides Main buttons, #2-then display Settings buttons / #3-display Map Selection
        for child in self.buttonframe.winfo_children(): #1
            child.grid_forget()
        self.settingsbtn = tk.Button(self.buttonframe,
                                    text="Settings",    #2
                                    command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        if file == "settings":
            self.settings()
        else: #3
            self.mapetlogo.place_forget()
            self.buttonframe.place_forget()
            self.backbuttonpage()
            return(file)

    # Hides Settings buttons and display Main buttons
    def settingback(self):
        self.fullscreenbtn.grid_forget()
        self.backbtn.grid_forget()
        self.placegui()

    # display Settings button
    def settings(self):
        self.fullscreenbtn = tk.Button(self.buttonframe,text="Toggle Fullscreen",
                                    command=lambda:self.fullscreen(),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.fullscreenbtn.grid(row=0,ipadx=10,ipady=10)
        self.backbtn = tk.Button(self.buttonframe, text="Back",
                                    command=lambda:self.settingback(),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.backbtn.grid(row=3,ipadx=10,ipady=10)
    # Toggle Fullscreen
    def fullscreen(self):
        self.parent.attributes("-fullscreen", not self.parent.attributes('-fullscreen'))

    # Opens file dialog to choose a file
    def filedialog(self):
        self.filedialogpath = filedialog.askopenfilename()

    def backbuttonpage(self):
        self.backbtn = tk.Button(self.parent, text="Back", command=lambda:deleteall(),
                                width=12,padx=3,pady=3, font=("calibri",15))
        self.backbtn.place(anchor="nw", relx=0.02, rely=0.02)

        def deleteall():
            try:
                self.cm.mapall.destroy()
            except:
                pass

            try:
                self.cm.pl.screen.destroy()
                self.cm.pl.switch.destroy()
            except:
                pass

            try:
                self.cm.mp.mapeditframe.destroy()
            except:
                pass
            try:
                self.cm.mp.pl.screen.destroy()
                self.cm.mp.pl.switch.destroy()
            except:
                pass
            self.backbtn.destroy()
            self.placegui()


class ChooseMap():
    def __init__(self, parent, file):
        self.parent = parent
        self.file = file

        # container for this whole screen
        self.mapall = tk.Frame(self.parent,width=1000,height=1000)
        self.mapall.place(relx=.48,rely=.48, anchor="c")

        ## Display files in folder
        # list of all files
        self.maps = os.listdir("maps")
        # creating lists to contain every file
        self.mapbox = []
        self.mapimg = []
        self.maptext = []
        self.mapbtn = []
        self.coli = 0
        self.rowi = 0
        # append files as frames
        for i in range(len(self.maps)+1):
            if i < len(self.maps):
                mapname = str(self.maps[i])
                self.mapbox.append(tk.Frame(self.mapall,width=200,height=200,bd=1,padx=50,pady=50))
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
                self.mapbox.append(tk.Frame(self.mapall,width=200,height=200,bd=1,padx=50,pady=50))
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
            if self.coli == 4:
                self.coli = 0
                self.rowi += 1
                
    # Opens selected file, hide map select container, display play/mapet
    def openmap(self,mapname):
        print("Loading file information...")
        with open(os.path.join("maps",mapname,"data.txt"),"r") as self.datamap:
            data = self.datamap.read().split(";")
        for i in data:
            print(i,end="")
        playercoord = ast.literal_eval(data[0].split("=")[1])       # ast converts strings back to lists
        gridsize = ast.literal_eval(data[1].split("=")[1])
        objectcoord = ast.literal_eval(data[2].split("=")[1])
        objectcolor = ast.literal_eval(data[3].split("=")[1])
        objecttypes = ast.literal_eval(data[4].split("=")[1])
        objecttypecolor = ast.literal_eval(data[5].split("=")[1])
        
        print("\n\nOpening",mapname)
        if self.file == "mapselect":
            self.mapall.place_forget()
            self.pl = process.PlayMap(self.parent,mapname,objectcoord,objectcolor,playercoord,objecttypes,objecttypecolor)
        elif self.file == "mapeditor":
            self.mapall.place_forget()
            self.mp = process.Mapedit(self.parent,mapname,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor)

    # Function to create new map
    def createmap(self):
        def replace(warnroot,mapname):
            playercoord = [2,2]                                                                     # Default coord at 2,2
            objecttypes = ("land", "water", "walls", "lava", "home", "goal", "spikes", "door")      # Default object list
            objecttypecolor = ("white", "cyan", "grey", "red", "green", "blue", "black", "brown")   # Default colors for objects 

            os.rmdir(os.path.join("maps",mapname))      # remove old folder
            os.mkdir(os.path.join("maps",mapname))      # create new folder

            newmaproot.destroy()
            warnroot.destroy()
            
            self.mapall.place_forget()

    def getlist(self):
        return(["new",self.parent,self.file])
            
        
        # private function for button when creating map
        def makenewmap():
            # Iniaializing variables 
            mapname = entry.get()                                                                   # Get the entered map name
            playercoord = [2,2]                                                                     # Default coord at 2,2
            objecttypes = ("land", "water", "walls", "lava", "home", "goal", "spikes", "door")      # Default object list
            objecttypecolor = ("white", "cyan", "grey", "red", "green", "blue", "black", "brown")   # Default colors for objects 
        
            # create a directory for the map, if it already exists, ask if replace
            try:
                os.mkdir(os.path.join("maps",mapname))

                # Destroy the popup
                newmaproot.destroy()

                self.mapall.place_forget()
                return(["new",self.file])

            # popup root when file already exists
            except FileExistsError:
                warnroot = tk.Tk()
                warning = tk.Label(warnroot, text="File already exists, do you want to replace it?")
                warning.grid(row=0,columnspan=2)
                yesbtn = tk.Button(warnroot, text="Replace",command=lambda name=mapname:replace(warnroot,name))
                yesbtn.grid(row=1,column=0)
                cancelbtn = tk.Button(warnroot, text="Cancel",command=lambda:warnroot.destroy())
                cancelbtn.grid(row=1,column=1)
                warnroot.mainloop()


        # create tk for inputting name
        newmaproot = tk.Tk()
        newmaproot.geometry("400x100+50+50")
        text = tk.Label(newmaproot,text="Enter the name of the map")
        text.grid(row=0,pady=5)
        entry = tk.Entry(newmaproot,width=15)
        entry.grid(row=1,pady=5)
        entry.focus_set()
        button = tk.Button(newmaproot,text="Done",command=makenewmap)
        button.grid(row=2,pady=5)
        
