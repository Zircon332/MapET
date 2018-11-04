#This is a module, 
#a prototype for INPUT.py of the main program


##    Welcome to keycontrol
##    
##    To import, 'import keycontrol'
##    To call, type 'set_controls(root)' in the program
##
##
##    OTHER IMPORTANT DETAILS:
##    The bindings bind to the entire program
##    The name of the tk is 'root'
##    The positions x and y are posx and posy
##    Player movement is measured in grids
    
import tkinter as tk
import config
import pickle
import os
import time

#Empty function to clear binds
def clear(event):
    print("Cleared")

c = 0
##def addwall(event):
##    global c
##    newcoord = [event.x // 20 , event.y // 21]
##    config.wallcoord.append(newcoord)
##    config.wall.append(tk.Label(config.playground,width=2,height=1,bg="grey"))
##    config.wall[c].grid(column=newcoord[0],row=newcoord[1])
##    config.wall[c].bind("<1>",lambda event, i=i: removewall(i))
##    c += 1
##def removewall(i):
##    print(i)
##    config.wallcoord.remove(i)
##    config.wall[c].destroy()

full = 0
def fullscreen(event):
    global full
    if full:
        config.root.attributes("-fullscreen", False)
        full = 0
    else:
        config.root.attributes("-fullscreen", True)
        full = 1

def save():
    path = os.path.expanduser('~') + '\Desktop\MapET\Tests\MapPlay\data'
    
    print(path)
    pickle.dump(config.wallcoord,open(os.path.join(path,"DamienFace.p"),"wb"))


def set_controls():
    def move(x,y):
        x *= config.speed_mult
        y *= config.speed_mult
        test_x = config.pos[0] + x
        test_y = config.pos[1] - y
        if [test_x,test_y] not in config.wallcoord:            
            if (config.pos[0] + x) > 0 and (config.pos[0] + x) < (config.bordersize-1):
                config.pos[0] += x
                config.minimap.move(config.miniplayer, x*10, 0)
                config.minimap2.move(config.miniplayer, x, 0)
            if (config.pos[1] - y) > 0 and (config.pos[1] - y) < (config.bordersize-1):
                config.pos[1] -= y
                config.minimap.move(config.miniplayer, 0, -y*10)
                config.minimap2.move(config.miniplayer, 0, -y)
            config.player.grid(column=config.pos[0],row=config.pos[1])    
            time.sleep(.001)
                
    #Bind movements
    config.root.bind_all("<Up>", lambda event, x=0,y=1: move(x,y))
    config.root.bind_all("<Down>", lambda event, x=0,y=-1: move(x,y))
    config.root.bind_all("<Left>", lambda event, x=-1,y=0: move(x,y))
    config.root.bind_all("<Right>", lambda event, x=1,y=0: move(x,y))

##    #Bind wall maker
##    config.playground.bind("<1>",addwall)

    config.root.bind_all("<F11>",fullscreen)

    
