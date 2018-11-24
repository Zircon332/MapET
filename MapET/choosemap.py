import os
import ast
import tkinter as tk
import play
import mapet
import pickle

class ChooseMap():
    def __init__(self, parent, file):
        self.parent = parent
        self.file = file

        # container for this whole screen
        self.mapall = tk.Frame(self.parent,width=1000,height=1000)
        self.mapall.place(relx=.48,rely=.48, anchor="c")

        parent.backbuttonpage(self.mapall)

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
##        try:
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
        goalcoord = ast.literal_eval(data[6].split("=")[1])
    
        print("\n\nOpening",mapname)
        if self.file == "mapselect":
            self.mapall.place_forget()
            self.pl = play.PlayMap(self.parent,mapname,objectcoord,objectcolor,playercoord,objecttypes,objecttypecolor,goalcoord)
        elif self.file == "mapeditor":
            self.mapall.place_forget()
            self.mp = mapet.Mapedit(self.parent,mapname,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor,goalcoord)

##        except:
##            print("Save file doesn't exist")

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
            
            if self.file == "mapselect":
                self.mapall.place_forget()
                self.pl = play.PlayMap(self.parent,mapname,[],{},playercoord,objecttypes,objecttypecolor,goalcoord)
            elif self.file == "mapeditor":
                self.mapall.place_forget()
                self.mp = mapet.Mapedit(self.parent,mapname,20,[],{},objecttypes,objecttypecolor,goalcoord)
        
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
                os.mkdir(os.path.join("maps",mapname))

                # Destroy the popup
                newmaproot.destroy()

                if self.file == "mapselect":
                    self.mapall.place_forget()
                    self.pl = play.PlayMap(self.parent,mapname,[],{},playercoord,objecttypes,objecttypecolor,goalcoord)
                elif self.file == "mapeditor":
                    self.mapall.place_forget()
                    self.mp = mapet.Mapedit(self.parent,mapname,20,[],{},objecttypes,objecttypecolor,goalcoord)

            # popup root when file already exists
            except FileExistsError:
                warnroot = tk.Tk()
                warnroot.geometry("200x100+250+250")
                warning = tk.Label(warnroot, text="File already exists, do you want to replace it?")
                warning.grid(row=0,columnspan=2)
                yesbtn = tk.Button(warnroot, text="Replace",command=lambda name=mapname:replace(warnroot,name))
                yesbtn.grid(row=1,column=0)
                cancelbtn = tk.Button(warnroot, text="Cancel",command=lambda:warnroot.destroy())
                cancelbtn.grid(row=1,column=1)
                warnroot.mainloop()


        # create tk for inputting name
        newmaproot = tk.Tk()
        newmaproot.geometry("200x100+250+250")
        text = tk.Label(newmaproot,text="Enter the name of the map")
        text.grid(row=0,pady=5)
        entry = tk.Entry(newmaproot,width=15)
        entry.grid(row=1,pady=5)
        entry.focus_set()
        button = tk.Button(newmaproot,text="Done",command=makenewmap)
        button.grid(row=2,pady=5)
        
