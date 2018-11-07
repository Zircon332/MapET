import tkinter as tk
import pickle
import os


class set_controls():
    def __init__(self,parent,screen,playercoord,speedmult,bordersize,zoomsize,camcoord,wallcoord,screenwallcoord,follow):
        self.parent = parent
        self.playercoord = playercoord
        self.speedmult = speedmult
        self.bordersize = bordersize
        self.zoomsize = zoomsize
        self.camcoord = camcoord
        self.wallcoord = wallcoord
        self.screenwallcoord = screenwallcoord
        self.follow = follow
        self.screen = screen

        #Bind movements
        self.parent.bind_all("<Up>", lambda event, x=0,y=-1: move(x,y))
        self.parent.bind_all("<Down>", lambda event, x=0,y=1: move(x,y))
        self.parent.bind_all("<Left>", lambda event, x=-1,y=0: move(x,y))
        self.parent.bind_all("<Right>", lambda event, x=1,y=0: move(x,y))

        
    def set_map_follow():
        self.zoomratio = 10 * self.bordersize / self.zoomsize
        self.screen.delete(tk.ALL)
        self.player = self.screen.create_rectangle(self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,self.zoomsize/2*zoomratio+self.zoomratio,fill="red")
        for i in self.screen_wallcoord:
            self.screen.create_rectangle(i[0]*self.zoomratio,i[1]*self.zoomratio,i[0]*self.zoomratio+self.zoomratio,i[1]*self.zoomratio+self.zoomratio,fill="grey",outline="grey")
        del self.screen_wallcoord[:]
                
    def move(x,y):
        self.x *= self.speed_mult
        self.y *= self.speed_mult
        self.test_x = self.playercoord[0] + x
        self.test_y = self.playercoord[1] + y
        if [self.test_x,self.test_y] not in self.wallcoord:            
            if self.test_x > 0 and self.test_x < (self.bordersize-1):
                self.playercoord[0] += self.x
                self.camcoord[0] += self.x
                if self.follow == 0:
                    self.screen.move(self.player, self.x*10, 0)
                else:
                    for i in self.wallcoord:
                        self.screenx = i[0] - self.camcoord[0] 
                        self.screeny = i[1] - self.camcoord[1]
                        if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                            self.screen_wallcoord.append([self.screenx,self.screeny])
                    self.set_map_follow()
            if self.test_y > 0 and self.test_y < (self.bordersize-1):
                self.playercoord[1] += self.y
                self.camcoord[1] += y
                if self.follow == 0:
                    self.screen.move(self.player, 0, self.y*10)
                else:
                    for i in self.wallcoord:
                        self.screenx = i[0] - self.camcoord[0] 
                        self.screeny = i[1] - self.camcoord[1]
                        if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= zoomsize:
                            self.screen_wallcoord.append([self.screenx,self.screeny])
                    self.set_map_follow()

    
