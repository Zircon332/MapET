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


def set_controls():
    def set_map_follow():
        zoomratio = 10 * config.bordersize / config.zoomsize
        config.screen.delete(tk.ALL)
        config.player = config.screen.create_rectangle(config.zoomsize/2*zoomratio,config.zoomsize/2*zoomratio,config.zoomsize/2*zoomratio+zoomratio,config.zoomsize/2*zoomratio+zoomratio,fill="red")
        for i in config.screen_wallcoord:
            config.screen.create_rectangle(i[0]*zoomratio,i[1]*zoomratio,i[0]*zoomratio+zoomratio,i[1]*zoomratio+zoomratio,fill="grey",outline="grey")
        del config.screen_wallcoord[:]
                
    def move(x,y):
        x *= config.speed_mult
        y *= config.speed_mult
        test_x = config.pos[0] + x
        test_y = config.pos[1] + y
        if [test_x,test_y] not in config.wallcoord:            
            if test_x > 0 and test_x < (config.bordersize-1):
                config.pos[0] += x
                config.camcoord[0] += x
                if config.follow == 0:
                    config.screen.move(config.player, x*10, 0)
                else:
                    for i in config.wallcoord:
                        screenx = i[0] - config.camcoord[0] 
                        screeny = i[1] - config.camcoord[1]
                        if screenx >= 0 and screenx <= config.zoomsize and screeny >= 0 and screeny <= config.zoomsize:
                            config.screen_wallcoord.append([screenx,screeny])
                    set_map_follow()
            if test_y > 0 and test_y < (config.bordersize-1):
                config.pos[1] += y
                config.camcoord[1] += y
                if config.follow == 0:
                    config.screen.move(config.player, 0, y*10)
                else:
                    for i in config.wallcoord:
                        screenx = i[0] - config.camcoord[0] 
                        screeny = i[1] - config.camcoord[1]
                        if screenx >= 0 and screenx <= config.zoomsize and screeny >= 0 and screeny <= config.zoomsize:
                            config.screen_wallcoord.append([screenx,screeny])
                    set_map_follow()

    #Bind movements
    config.root.bind_all("<Up>", lambda event, x=0,y=-1: move(x,y))
    config.root.bind_all("<Down>", lambda event, x=0,y=1: move(x,y))
    config.root.bind_all("<Left>", lambda event, x=-1,y=0: move(x,y))
    config.root.bind_all("<Right>", lambda event, x=1,y=0: move(x,y))
    
