import os
import ast
from tkinter import filedialog
import tkinter as tk
import process1
import process2


def init1(self, parent):
    super().__init__(parent)
    title("MapET")
     screen_width =  parent.winfo_screenwidth()
     screen_height =  parent.winfo_screenheight()
     parent.geometry("%dx%d+%d+%d" % ( screen_width, screen_height,0,0))
     parent.attributes("-fullscreen", False)
     creategui()

def creategui(self):    # Creates logo, menubar and buttons
    # MapET Logo Banner
     logoimg = tk.PhotoImage(file="images/logo.gif")
     mapetlogo =  tk.Label( parent, image= logoimg,anchor="c")
     mapetlogo.image =  logoimg

    # Menu bar
     menubar = tk.Menu( parent)
    # 'File' Menu Bar
     filemenu = tk.Menu( menubar, tearoff=0)
     filemenu.add_command(label="Open", command=lambda: filedialog())
     filemenu.add_command(label="Save",  command=lambda:print("test"))
     filemenu.add_separator()
     filemenu.add_command(label="Exit", command= parent.quit)
     menubar.add_cascade(label="File", menu= filemenu)

     buttonframe = tk.Frame(self, bg="black", height=1920,width=100)    # creates buttons and their frame, then place with function
     mapselectbtn = tk.Button( buttonframe,text="Play Map",
                                command=lambda: fileopening("mapselect"),
                                width=12,padx=10,pady=20,font=("calibri",20))
     mapetbtn = tk.Button( buttonframe,text="Map Editor",
                                command=lambda: fileopening("mapeditor"),
                                width=12,padx=10,pady=20,font=("calibri",20))
     settingsbtn = tk.Button( buttonframe,
                                text="Settings",command=lambda: fileopening("settings"),
                                width=12,padx=10,pady=20,font=("calibri",20))
     programexitbtn = tk.Button( buttonframe, text="Quit",
                                    command= parent.destroy,
                                    width=12,padx=10,pady=20, font=("calibri",20))
     placegui()

def placegui(self):    # display main buttons
     mapetlogo.place(relx=.5, rely=.15, anchor="c")
     buttonframe.place(x=10,y=10, anchor="c", relx=0.48, rely=0.5)
     mapselectbtn.grid(row=0,ipadx=10,ipady=10)
     mapetbtn.grid(row=1,ipadx=10,ipady=10)
     settingsbtn.grid(row=2,ipadx=10,ipady=10)
     programexitbtn.grid(row=3,ipadx=10,ipady=10)


def fileopening(self,file):    # #1-Hides Main buttons, #2-then display Settings buttons / #3-display Map Selection
    for child in  buttonframe.winfo_children(): #1
        child.grid_forget()
     settingsbtn = tk.Button( buttonframe,
                                text="Settings",    #2
                                command=lambda: fileopening("settings"),
                                width=12,padx=10,pady=20,font=("calibri",20))
    if file == "settings":
         settings()
    else: #3
         mapetlogo.place_forget()
         buttonframe.place_forget()
         backbuttonpage()
        return(file)

# Hides Settings buttons and display Main buttons
def settingback(self):
     fullscreenbtn.grid_forget()
     backbtn.grid_forget()
     placegui()

# display Settings button
def settings(self):
     fullscreenbtn = tk.Button( buttonframe,text="Toggle Fullscreen",
                                command=lambda: fullscreen(),
                                width=12,padx=10,pady=10, font=("calibri",20))
     fullscreenbtn.grid(row=0,ipadx=10,ipady=10)
     backbtn = tk.Button( buttonframe, text="Back",
                                command=lambda: settingback(),
                                width=12,padx=10,pady=10, font=("calibri",20))
     backbtn.grid(row=3,ipadx=10,ipady=10)
# Toggle Fullscreen
def fullscreen(self):
     parent.attributes("-fullscreen", not  parent.attributes('-fullscreen'))

# Opens file dialog to choose a file
def filedialog(self):
     filedialogpath = filedialog.askopenfilename()

def backbuttonpage(self):
     backbtn = tk.Button( parent, text="Back", command=lambda:deleteall(),
                            width=12,padx=3,pady=3, font=("calibri",15))
     backbtn.place(anchor="nw", relx=0.02, rely=0.02)

    def deleteall():
        try:
             cm.mapall.destroy()
        except:
            pass

        try:
             cm.pl.screen.destroy()
             cm.pl.switch.destroy()
        except:
            pass

        try:
             cm.mp.mapeditframe.destroy()
        except:
            pass
        try:
             cm.mp.pl.screen.destroy()
             cm.mp.pl.switch.destroy()
        except:
            pass
         backbtn.destroy()
         placegui()

#____________________________________________________________________________________________________________________________
def init2(self, parent, file):
     parent = parent
     file = file

    # container for this whole screen
     mapall = tk.Frame( parent,width=1000,height=1000)
     mapall.place(relx=.48,rely=.48, anchor="c")

    ## Display files in folder
    # list of all files
     maps = os.listdir("maps")
    # creating lists to contain every file
     mapbox = []
     mapimg = []
     maptext = []
     mapbtn = []
     coli = 0
     rowi = 0
    # append files as frames
    for i in range(len( maps)+1):
        if i < len( maps):
            mapname = str( maps[i])
             mapbox.append(tk.Frame( mapall,width=200,height=200,bd=1,padx=50,pady=50))
            try:
                 banner = tk.PhotoImage(file=os.path.join("maps",mapname,"banner.gif"))
                 mapimg.append(tk.Label( mapbox[i],width=200,height=100,image= banner))
                 mapimg[i].image =  banner
            except:
                 mapimg.append(tk.Label( mapbox[i],width=20,height=10,bg="white"))
             maptext.append(tk.Label( mapbox[i],text=mapname,width=10,height=1,font=("arial",20)))
             mapbtn.append(tk.Button( mapbox[i],text="Choose map",width=10,height=1,command=lambda m=mapname: openmap(m),font=("arial",15)))
            # get the banner img of the mapfile, if any

        else:
            # create-new-map frame
             mapbox.append(tk.Frame( mapall,width=200,height=200,bd=1,padx=50,pady=50))
             mapimg.append(tk.Label( mapbox[i],width=20,height=10,bg="grey"))
             maptext.append(tk.Label( mapbox[i],text="Create New",width=10,height=1,font=("arial",20)))
             mapbtn.append(tk.Button( mapbox[i],text="Choose map",width=10,height=1,command= createmap,font=("arial",15)))
        # grid them
         mapbox[i].grid(column= coli,row= rowi)
         mapimg[i].grid(row=1)
         maptext[i].grid(row=2)
         mapbtn[i].grid(row=3)
        # count each column, when column reach 4, start next row
         coli += 1
        if  coli == 4:
             coli = 0
             rowi += 1
            
# Opens selected file, hide map select container, display play/mapet
def openmap(self,mapname):
    print("Loading file information...")
    with open(os.path.join("maps",mapname,"data.txt"),"r") as  datamap:
        data =  datamap.read().split(";")
    for i in data:
        print(i,end="")
    playercoord = ast.literal_eval(data[0].split("=")[1])       # ast converts strings back to lists
    gridsize = ast.literal_eval(data[1].split("=")[1])
    objectcoord = ast.literal_eval(data[2].split("=")[1])
    objectcolor = ast.literal_eval(data[3].split("=")[1])
    objecttypes = ast.literal_eval(data[4].split("=")[1])
    objecttypecolor = ast.literal_eval(data[5].split("=")[1])
    
    print("\n\nOpening",mapname)
    if  file == "mapselect":
         mapall.place_forget()
         pl = process.PlayMap( parent,mapname,objectcoord,objectcolor,playercoord,objecttypes,objecttypecolor)
    elif  file == "mapeditor":
         mapall.place_forget()
         mp = process.Mapedit( parent,mapname,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor)

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
        
         mapall.place_forget()

def getlist(self):
    return(["new", parent, file])
        
    
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

             mapall.place_forget()
            return(["new", file])

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
    
