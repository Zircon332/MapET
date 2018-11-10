import tkinter as tk
import pickle
import os

# Controls for Map Play
class SetPlayControls():
    def __init__(self,parent,screen,player,playercoord,speedmult,bordersize,zoomsize,camcoord,wallcoord,screenwallcoord,follow):
        # Carry over data
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
        self.player = player
        
        #Bind movements
        self.parent.bind_all("<Up>", lambda event, x=0,y=-1: self.movef(x,y))
        self.parent.bind_all("<Down>", lambda event, x=0,y=1: self.movef(x,y))
        self.parent.bind_all("<Left>", lambda event, x=-1,y=0: self.movef(x,y))
        self.parent.bind_all("<Right>", lambda event, x=1,y=0: self.movef(x,y))

    # move the player according to input
    def movef(self, x, y):
        self.x, self.y = x, y
        # Increase speed with multiplier, if any
        self.x *= self.speedmult
        self.y *= self.speedmult
        # test if where ur going is a wall
        self.test_x = self.playercoord[0] + self.x
        self.test_y = self.playercoord[1] + self.y
        if [self.test_x,self.test_y] not in self.wallcoord:            
            if self.test_x > 0 and self.test_x < (self.bordersize-1):
                self.playercoord[0] += self.x
                self.camcoord[0] += self.x
                if self.follow == 0:                            # normal moving
                    self.screen.move(self.player, self.x*10, 0)
                else:                                           # cam follow move
                    self.cammovef()
            if self.test_y > 0 and self.test_y < (self.bordersize-1):
                self.playercoord[1] += self.y
                self.camcoord[1] += y
                if self.follow == 0:                            # normal moving
                    self.screen.move(self.player, 0, self.y*10)
                else:                                           # cam follow move
                    self.cammovef()
        self.screen.update_idletasks()

    # append everything that will be shown in screen into a list
    def cammovef(self):
        for i in self.wallcoord:
            self.screenx = i[0] - self.camcoord[0] 
            self.screeny = i[1] - self.camcoord[1]
            if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                self.screenwallcoord.append([self.screenx,self.screeny])
        # update screen in camfollow mode
        self.zoomratio = 10 * self.bordersize / self.zoomsize
        self.screen.delete(tk.ALL)      #Delete previoius things in screen
        #Create player at center
        self.player = self.screen.create_rectangle(self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,fill="red")
        #Set then clear the wall coordinates on the screen
        for i in self.screenwallcoord:
            self.screen.create_rectangle(i[0]*self.zoomratio,i[1]*self.zoomratio,i[0]*self.zoomratio+self.zoomratio,i[1]*self.zoomratio+self.zoomratio,fill="grey",outline="grey")
        del self.screenwallcoord[:]


# Controls for MapEdit
class SetEditControls:
    def __init__(self,parent):
        self.parent = parent
