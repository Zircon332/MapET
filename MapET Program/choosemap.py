import os
import tkinter as tk
import play
import mapet

class ChooseMap():
    def __init__(self, parent, file):
        self.parent = parent
        self.file = file

        self.mapall = tk.Frame(self.parent,width=1000,height=1000)
        self.mapall.place(relx=.1,rely=.1)

        self.maps = os.listdir("maps")
        self.mapbox = []
        self.mapimg = []
        self.maptext = []
        self.mapbtn = []
        self.coli = 0
        self.rowi = 0
        for i in range(len(self.maps)):
            mapname = str(self.maps[i])
            self.mapbox.append(tk.Frame(self.mapall,width=200,height=200,bd=1,padx=50,pady=50))
            self.mapimg.append(tk.Label(self.mapbox[i],width=20,height=10,bg="white"))
            self.maptext.append(tk.Label(self.mapbox[i],text=mapname,width=10,height=1,font=("arial",20)))
            self.mapbtn.append(tk.Button(self.mapbox[i],text="Choose map",width=10,height=1,command=lambda m=mapname:self.openmapf(m),font=("arial",15)))
            self.mapbox[i].grid(column=self.coli,row=self.rowi)  
            self.mapimg[i].grid(column=0,row=1)
            self.maptext[i].grid(column=0,row=2)
            self.mapbtn[i].grid(column=0,row=3)
            self.coli += 1
            if self.coli == 4:
                self.coli = 0
                self.rowi += 1
            
    def openmapf(self,mapname):
        print("Opening",mapname)
        coord = open(os.path.join("maps",mapname,"coord.txt"),"r")
        if self.file == "mapselect":
            self.mapall.place_forget()
            play.playgamef(self.parent)
        elif self.file == "mapeditor":
            mapet.Mapedit(self.parent,20,coord)
