import tkinter as tk
import pickle
import os


def set_controls(self,playercoord,speedmult,bordersize,zoomsize,camcoord,wallcoord,screenwallcoord,follow):
    def set_map_follow(bordersize,zoomsize):
        zoomratio = 10 * bordersize / zoomsize
        screen.delete(tk.ALL)
        player = screen.create_rectangle(zoomsize/2*zoomratio,zoomsize/2*zoomratio,zoomsize/2*zoomratio+zoomratio,zoomsize/2*zoomratio+zoomratio,fill="red")
        for i in screen_wallcoord:
            screen.create_rectangle(i[0]*zoomratio,i[1]*zoomratio,i[0]*zoomratio+zoomratio,i[1]*zoomratio+zoomratio,fill="grey",outline="grey")
        del screen_wallcoord[:]
                
    def move(x,y,speedmult):
        x *= speed_mult
        y *= speed_mult
        test_x = pos[0] + x
        test_y = pos[1] + y
        if [test_x,test_y] not in wallcoord:            
            if test_x > 0 and test_x < (bordersize-1):
                pos[0] += x
                camcoord[0] += x
                if follow == 0:
                    screen.move(player, x*10, 0)
                else:
                    for i in wallcoord:
                        screenx = i[0] - camcoord[0] 
                        screeny = i[1] - camcoord[1]
                        if screenx >= 0 and screenx <= zoomsize and screeny >= 0 and screeny <= zoomsize:
                            screen_wallcoord.append([screenx,screeny])
                    set_map_follow()
            if test_y > 0 and test_y < (bordersize-1):
                pos[1] += y
                camcoord[1] += y
                if follow == 0:
                    screen.move(player, 0, y*10)
                else:
                    for i in wallcoord:
                        screenx = i[0] - camcoord[0] 
                        screeny = i[1] - camcoord[1]
                        if screenx >= 0 and screenx <= zoomsize and screeny >= 0 and screeny <= zoomsize:
                            screen_wallcoord.append([screenx,screeny])
                    set_map_follow()

    #Bind movements
    self.parent.bind_all("<Up>", lambda event, x=0,y=-1: move(x,y))
    self.parent.bind_all("<Down>", lambda event, x=0,y=1: move(x,y))
    self.parent.bind_all("<Left>", lambda event, x=-1,y=0: move(x,y))
    self.parent.bind_all("<Right>", lambda event, x=1,y=0: move(x,y))
