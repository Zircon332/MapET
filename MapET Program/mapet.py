#Create and edit maps

import tkinter as tk
import config


class Mapedit:    
    def __init__(self,parent,bordersize,wallcoord):
        self.parent = parent
        self.bordersize = bordersize
        self.wallcoord = wallcoord
        
        self.showcoord = tk.Label(self.parent,text=self.wallcoord)
        self.showcoord.place(relx=.01,y=.01)

        self.frame = tk.Frame(self.parent)
        self.frame.place(relx=0.5,rely=0.5, anchor="c")

        self.end1 = 0
        self.end2 = 0
        
        #Pix list to store every pixel, c for index
        self.c = 0
        self.pix=[]
        for y in range(self.bordersize):
            for x in range(self.bordersize):
                self.pix.append(tk.Label(self.frame,height=1,width=2,background="white",bd=2,relief="groove"))
                self.pix[self.c].grid(column=x,row=y)
                self.c = self.c + 1

        for i in range(self.bordersize**2):
            self.pix[i].bind("<1>",lambda event, i=i: self.togglewallf(i))

        #Sets up previously created walls
        self.setwallf()

        self.updatebutton = tk.Button(self.parent,text="Update new map",command=self.updatemapf)
        self.updatebutton.place(relx=0,rely=0.05)

        self.switchbutton = tk.Button(self.parent,text="Switch to Play mode",command=self.switchplayf)
        self.switchbutton.place(relx=.9,rely=.1)

        self.linebutton = tk.Button(self.parent,text="Make a line from last two points",command=self.createlinef)
        self.linebutton.place(relx=.9,rely=.2)


    def togglewallf(self,i):
        self.end2 = self.end1
        self.end1 = i
        if self.pix[i].cget("bg") == "grey":
            self.pix[i].config(bg="white")
        else:
            self.pix[i].config(bg="grey")

    #Update the new map into the list config.wallcoord
    def updatemapf(self):
        self.tempwallcoord = []
        for i in range(self.bordersize**2):
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
                
    #Shows existing walls
    def setwallf(self):
        for walls in self.wallcoord:
            self.index = walls[0] + (self.bordersize * walls[1])
            self.pix[self.index].config(bg="grey")

    def switchplayf(self):
        self.parent.withdraw()
##        self.parent.deiconify()

    #Create a line between last two points if they are on the same line
    def createlinef(self):
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

