import os
import tkinter as tk
import input_handling
import menu
import process2

def init3(self, parent , mapname , objectcoord , objectcolor , playercoord , objecttypes , objecttypecolor):
     parent = parent
     mapname = mapname
     playercoord = playercoord
     speedmult = 1
     bordersize = 50
     zoomsize = 10
    #Camera position, top left from position of player
     camcoord = [ playercoord[0] -  zoomsize/2,  playercoord[1] -  zoomsize/2]
     wallcoord = wallcoord
     screenwallcoord = []
     follow = 0

    #Playground Screen
     screen = tk.Canvas( parent, bg="Black", width= bordersize*10, height= bordersize*10, highlightthickness=0,bd=0)
     screen.place(relx=.1,rely=.1)
     set_map()

    #set key controls
     keyinput = input_handling.SetPlayControls( parent, screen, player, playercoord, speedmult, bordersize, zoomsize, camcoord, wallcoord, screenwallcoord, follow)

    #Switch cam to follow
     switch = tk.Button( parent,text="Switch to Follow", command= followswitch)
     switch.place(relx=.9,rely=.1)

def set_map(self):
     screen.delete(tk.ALL)
     set_wall()
    for i in  wallcoord:
         screen.create_rectangle(i[0]*10,i[1]*10,i[0]*10+10,i[1]*10+10,fill="grey",outline="grey")

# sets walls and player
def set_wall(self):
     bds =  bordersize * 10
     border =  screen.create_polygon([0,0, bds,0, bds, bds,0, bds,0,0,10,0,10, bds-10, bds-10, bds-10, bds-10,10,0,10],fill="grey",outline="grey")
     player =  screen.create_rectangle( playercoord[0]*10, playercoord[1]*10, playercoord[0]*10+10, playercoord[1]*10+10,fill="red")

# toggle to switch
def followswitch(self):
    if  follow == 0:
         follow = 1
        # does the function in input, updating the screen before needing to move
        for i in  wallcoord:
             screenx = i[0] -  camcoord[0]
             screeny = i[1] -  camcoord[1]
            if  screenx >= 0 and  screenx <=  zoomsize and  screeny >= 0 and  screeny <=  zoomsize:
                 screenwallcoord.append([ screenx, screeny])
         zoomratio = 10 *  bordersize /  zoomsize
         screen.delete(tk.ALL)
         player =  screen.create_rectangle( zoomsize/2* zoomratio, zoomsize/2* zoomratio, zoomsize/2* zoomratio+ zoomratio, zoomsize/2* zoomratio+ zoomratio,fill="red")
        for i in  screenwallcoord:
             screen.create_rectangle(i[0]* zoomratio,i[1]* zoomratio,i[0]* zoomratio+ zoomratio,i[1]* zoomratio+ zoomratio,fill="grey",outline="grey")
        del  screenwallcoord[:]
    else:
         set_wall()
         follow = 0
        # recreate and update player and walls
         set_map()
         keyinput.player =  player
    #Update follow value in keyinput
     keyinput.follow =  follow


def save(self):
    with open(os.path.join("maps", mapname,"data.txt"),"w") as  datamap:
         datamap.write( mapname)
         datamap.write( bgcolor)

    # Saves the location where the character is before quitting
    with open(os.path.join("maps", mapname,"playerdata.txt"),"w") as  playerdata:
         playerdata.write( playercoord)

