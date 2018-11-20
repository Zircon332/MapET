#Create and edit maps
import os
import tkinter as tk
import menu
import input_handling
import process1




def init4(self,parent,mapname,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor):
     parent    =  parent
     gridsize  =  gridsize              # Number that represents the square size
     objectcoord = objectcoord          # Objects are stored as [xcoord, ycoord] (list)
     objectcolor = objectcolor          # Objects' color for each object (set)
     objecttypes = objecttypes          # List of object in the map
     objecttypecolor = objecttypecolor  # List of color of each object
     mapname   =  mapname               # Name of opened map
    
    # Stores the last two coords selected
     end1 = [0,0]
     end2 = [0,0]

    # Frame for this page
     mapeditframe = tk.Frame( parent,height=800,width=1200)
     mapeditframe.place(relx=.5,rely=.5,anchor='c')

    # Title of the map, that can be changed and saved
     mapnamelabel = tk.Label( mapeditframe,text= mapname,width=20,font=("Calibri",20))
     mapnamelabel.place(relx=.1,rely=.02)
    
    # Label for displaying list of coords (should be removed before finalizing)
     showcoord = tk.Label( mapeditframe,text= objectcoord)
     showcoord.place(relx=0.5,rely=.9,anchor="c")

    # Frame for grid
     gridframe = tk.Frame( mapeditframe)
     gridframe.place(relx=.5,rely=.5, anchor="c")
     createmapgrid()  # map the grid

    # Set input
     keyinput = input_handling.SetEditControls( mapeditframe,  gridsize,  objectcoord,  objectcolor,  objecttypes,  objecttypecolor,  gridaxisx,  gridaxisy,  xshift,  yshift,  pix,  end1,  end2)
    
    # Buttons
     btnframe = tk.Frame( mapeditframe)
     btnframe.place(relx=.9,rely=.2,anchor="ne")
     createbuttons()

    # Cell types select box
     typeframe = tk.Frame( mapeditframe)
     typeframe.place(relx=.15,rely=.2,anchor="n")
     createtypes()

#____________________________Functions__________________________________________________________________________________________________________________________________________________________    

# Creates the center grid for mapedit
def createmapgrid(self):
    # display axes
     gridaxisx = []
     gridaxisy = []
     xshift =  yshift = 0   # initialize both shifts to 0, shifting moves the screen
    for i in range( gridsize):
         gridaxisx.append(tk.Label( gridframe,height=1,width=0,text=i+ xshift,font=("Arial",8)))
         gridaxisy.append(tk.Label( gridframe,height=1,width=0,text=i+ yshift,font=("Arial",8)))
         gridaxisx[i].grid(column=i+1,row=0)
         gridaxisy[i].grid(column=0,row=i+1)
        
    # display grid
    # Pix dictionary to store every pixel, c for index
     pix={}
    for y in range( gridsize):
        for x in range( gridsize):
             pix[x,y] = (tk.Label( gridframe,height=1,width=2,background="white",bd=2,relief="groove"))
             pix[x,y].grid(column=x+1,row=y+1)

    # Sets up previously created walls
     setwall()

def createbuttons(self):
    # Button for updating new coord
     updatebutton = tk.Button( btnframe,text="Update new map",command= savemapcoord)
     updatebutton.grid(row=0,pady=20,sticky="w")

    # Button for switching to play mode(currently not working)
     switchbutton = tk.Button( btnframe,text="Switch to Play mode",command= switchplay)
     switchbutton.grid(row=1,pady=20,sticky="w")
    
    # Button for creating lines
     linebutton = tk.Button( btnframe,text="Make a line from last two points",command= keyinput.createline)
     linebutton.grid(row=2,pady=20,sticky="w")

    # Button for clearing everything in the grid
     clearbutton = tk.Button( btnframe,text="Clear walls",command= cleargrid)
     clearbutton.grid(row=3,pady=20,sticky="w")

    # Button for saving objects in the grid
     savebutton = tk.Button( btnframe,text="Save file",command= save)
     savebutton.grid(row=4,pady=20,sticky="w")

# types of things that can be added to the map
def createtypes(self):
     typename = []
     typeimg  = []
     typebtn  = []
    for i in range(len( objecttypes)):
         typename.append(tk.Label( typeframe,height=2,width=9,pady=1,text= objecttypes[i],font=("Calibri",15)))
         typeimg.append(tk.Label( typeframe,height=2,width=10,pady=2,bg= objecttypecolor[i]))
         typebtn.append(tk.Button( typeframe,height=2,width=10,pady=2,padx=1,text="Select",command=lambda i=i: selecttype(i)))
         typename[i].grid(row=i,column=0)
         typeimg[i].grid(row=i,column=1)
         typebtn[i].grid(row=i,column=2)

# display existing walls in the grid
def setwall(self):
    for objects in  objectcoord:
        x = objects[0]
        y = objects[1]
        color =  objectcolor[(x,y)]
         pix[x,y].config(bg=color)

# Update the new map coords into the list config.objectcoord
def savemapcoord(self):
    # Display the list of coords
     showcoord.config(text= keyinput.objectcoord)
    
# does nothing for now, but it should go to play
def switchplay(self):
     mapeditframe.destroy()
     pl = play.PlayMap( parent, objectcoord)

# erase all coord in keyinput (cause everything is transfered there)
def cleargrid(self):
    for x in range( keyinput.gridsize):
        for y in range( keyinput.gridsize):
             keyinput.pix[x,y].config(bg= objecttypecolor[0])
    del  keyinput.objectcoord[:]
     keyinput.objectcolor.clear()

def selecttype(self,index):
     keyinput.color =  objecttypecolor[index]


def save(self):
    with open(os.path.join("maps", mapname,"data.txt"),"w") as  datamap:
        data = "PlayerCoord=" + "[2,2]" + \
                ";\nGridsize=" + str( gridsize) + \
                ";\nObjectCoord=" + str( keyinput.objectcoord) + \
                ";\nObjectColor=" + str( keyinput.objectcolor) + \
                ";\nObjecttypes=" + str( objecttypes) + \
                ";\nObjectTypeColor=" + str( objecttypecolor)
         datamap.write(data)
