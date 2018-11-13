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
        self.parent.bind_all("<Up>", lambda event, x=0,y=-1: self.move(x,y))
        self.parent.bind_all("<Down>", lambda event, x=0,y=1: self.move(x,y))
        self.parent.bind_all("<Left>", lambda event, x=-1,y=0: self.move(x,y))
        self.parent.bind_all("<Right>", lambda event, x=1,y=0: self.move(x,y))

    # move the player according to input
    def move(self, x, y):
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
                    self.cammove()
            if self.test_y > 0 and self.test_y < (self.bordersize-1):
                self.playercoord[1] += self.y
                self.camcoord[1] += y
                if self.follow == 0:                            # normal moving
                    self.screen.move(self.player, 0, self.y*10)
                else:                                           # cam follow move
                    self.cammove()
        self.screen.update_idletasks()

    # append everything that will be shown in screen into a list
    def cammove(self):
        for i in self.wallcoord:
            self.screenx = i[0] - self.camcoord[0] 
            self.screeny = i[1] - self.camcoord[1]
            if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                self.screenwallcoord.append([self.screenx,self.screeny])
        # update screen in camfollow mode
        self.zoomratio = 10 * self.bordersize / self.zoomsize
        self.screen.delete(tk.ALL)      #Delete previous things in screen
        #Create player at center
        self.player = self.screen.create_rectangle(self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,fill="red")
        #Set then clear the wall coordinates on the screen
        for i in self.screenwallcoord:
            self.screen.create_rectangle(i[0]*self.zoomratio,i[1]*self.zoomratio,i[0]*self.zoomratio+self.zoomratio,i[1]*self.zoomratio+self.zoomratio,fill="grey",outline="grey")
        del self.screenwallcoord[:]


# Controls for MapEdit
class SetEditControls:
    def __init__(self,parent,gridsize,wallcoord,gridaxisx,gridaxisy,xshift,yshift, screenwallcoord, pix):
        # Carry over data
        self.parent = parent
        self.gridsize = gridsize
        self.wallcoord = wallcoord
        self.gridaxisx = gridaxisx
        self.gridaxisy = gridaxisy
        self.xshift = xshift
        self.yshift = yshift
        self.screenwallcoord = screenwallcoord
        self.pix = pix
        self.cameracoord = [0,0]

        self.parent.bind_all("<Up>", lambda event, x=0,y=-1: self.shiftmap(x,y))
        self.parent.bind_all("<Down>", lambda event, x=0,y=1: self.shiftmap(x,y))
        self.parent.bind_all("<Left>", lambda event, x=-1,y=0: self.shiftmap(x,y))
        self.parent.bind_all("<Right>", lambda event, x=1,y=0: self.shiftmap(x,y))

        # Bind clicks to grid
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.pix[x,y].bind("<1>",lambda event, x=x,y=y: self.togglewall(x,y))


    # shift the coords of the grid
    def shiftmap(self,x,y):
        self.xshift += x
        self.yshift += y
        # update the axes numbers
        for i in range(len(self.gridaxisx)):
            self.gridaxisx[i].config(text=i+self.xshift)
            self.gridaxisy[i].config(text=i+self.yshift)
        if self.xshift + self.gridsize == 100 or self.xshift == -10:
            for i in self.gridaxisx:
                i.config(font=("arial",6))
        if self.xshift > -10 and self.xshift + self.bordersize < 100:
            for i in self.gridaxisx:
                i.config(font=("arial",8))
        self.updatescreenmap(x,y)
        
    def updatescreenmap(self,x,y):
        self.cameracoord[0] += x
        self.cameracoord[1] += y
            
        # clear the screen
        self.clearscreen()   

        # display new walls
        for walls in self.wallcoord:
            if walls[0] >= self.cameracoord[0] and walls[0] <= self.cameracoord[0]+self.gridsize:
                if walls[1] >= self.cameracoord[1] and walls[1] <= self.cameracoord[1]+self.gridsize:    
                    self.index = int(walls[0]) + (self.gridsize * walls[1])
                    if self.index >= 0 and self.index <= 400:
                        self.pix[self.index].config(bg="grey")

    def clearscreen(self):
        for x in range(self.gridsze):
            for y in range(self.gridsize):
                 self.pix[x,y].config(bg="white")

    # Create or remove grid when clicked
    def togglewall(self,x,y):
        self.end2 = self.end1
        self.end1 = [x,y]
        if self.pix[x,y].cget("bg") == "grey":
            self.pix[x,y].config(bg="white")
        else:
            self.pix[x,y].config(bg="grey")


    # Create a line between last two points if they are on the same line
    def createline(self):
        # Finding out which row
        if self.end1[0] == self.end2[0]:
            if self.end1[1] < self.end2[1]:
                while self.end2[1]-1 > self.end1[1]:
                    self.end2[1] -= 1
                    self.pix[self.end2[0],self.end2[1]].config(bg="grey")
            elif self.end1[1] > self.end2[1]:
                while self.end2[0]+1 < self.end1[0]:
                    self.end2[0] += 1
                    self.pix[self.end2[0],self.end2[1]].config(bg="grey")        
        elif self.end1[1] == self.end2[1]:
            if self.end1[0] < self.end2[0]:
                while self.end2[0]-1 > self.end1[0]:
                    self.end2[0] -= 1
                    self.pix[self.end2[0],self.end2[1]].config(bg="grey")
            if self.end1[1] > self.end2[1]:
                while self.end2[0]+1 < self.end1[0]:
                    self.end2[0] += 1
                    self.pix[self.end1[0],self.end2[1]].config(bg="grey")

        
