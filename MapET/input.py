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
        self.parent.bind_all("<Shift_L>", lambda event, x=1,y=0: self.move(x,y))

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
    def __init__(self,parent,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor,gridaxisx,gridaxisy,xshift,yshift,pix,end1,end2):
        # Carry over data
        self.parent = parent
        self.gridsize = gridsize
        self.objectcoord = objectcoord
        self.objectcolor = objectcolor
        self.objecttypes = objecttypes
        self.objecttypecolor = objecttypecolor
        self.gridaxisx = gridaxisx
        self.gridaxisy = gridaxisy
        self.xshift = xshift
        self.yshift = yshift
        
        self.pix = pix
        self.end1 = end1
        self.end2 = end2
        self.cameracoord = [0,0]
        self.color = "white"             # Default chosen color

        self.parent.bind_all("<Up>", lambda event, x=0,y=-1: self.shiftmap(x,y))
        self.parent.bind_all("<Down>", lambda event, x=0,y=1: self.shiftmap(x,y))
        self.parent.bind_all("<Left>", lambda event, x=-1,y=0: self.shiftmap(x,y))
        self.parent.bind_all("<Right>", lambda event, x=1,y=0: self.shiftmap(x,y))

        # Opens menu for going back
        self.parent.bind_all("<Escape>", self.backmenu)

        # Undo bind
        self.parent.bind_all("<Control-z>", lambda event, x=1,y=0: self.shiftmap(x,y))
        
        # Bind clicks to grid
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.pix[x,y].bind("<1>",lambda event, x=x,y=y: self.togglewall(x,y))


    def backmenu(self,key):
        print()
##        self.frame.destroy()
##        self.showcoord.destroy()
##        self.typeframe.destroy()
##        self.btnframe.destroy()


    # shift the coords of the grid
    def shiftmap(self,x,y):
        if self.xshift+x >= 0 and self.yshift+y >= 0:
            self.xshift += x
            self.yshift += y
            # update the axes numbers
            for i in range(len(self.gridaxisx)):
                self.gridaxisx[i].config(text=i+self.xshift)
                self.gridaxisy[i].config(text=i+self.yshift)
            # Changing size of the axes
            if self.xshift + self.gridsize == 100:
                for i in self.gridaxisx:
                    i.config(font=("arial",6))
            elif self.xshift + self.gridsize == 99:
                for i in self.gridaxisx:
                    i.config(font=("arial",8))
            # keep track of clicked grid after moving
            self.end1[0] -= x
            self.end1[1] -= y
            self.end2[0] -= x
            self.end2[1] -= y
            # update map on screen
            self.updatescreenmap(x,y)

    def updatescreenmap(self,x,y):
        self.cameracoord[0] += x
        self.cameracoord[1] += y
            
        # clear the screen
        self.clearscreen()   

        # display new walls
        for walls in self.objectcoord:
            if walls[0]-self.cameracoord[0] >= 0 and walls[0]-self.cameracoord[0] < 20 and walls[1]-self.cameracoord[1] >= 0 and walls[1]-self.cameracoord[1] < 20:
                self.pix[walls[0]-self.cameracoord[0],walls[1]-self.cameracoord[1]].config(bg=self.color)

    # makes every grid white (doesn't delete coords)
    def clearscreen(self):
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.pix[x,y].config(bg="white")
                

    # Create or remove grid when clicked
    def togglewall(self,x,y):
        self.end2 = self.end1
        self.end1 = [x,y]
        if self.color != "white":
            if self.pix[x,y].cget("bg") == self.color:
                self.wallcoord.remove([x+self.xshift,y+self.yshift])
                self.pix[x,y].config(bg="white")
            elif self.pix[x,y].cget("bg") == "white":
                self.wallcoord.append([x+self.xshift,y+self.yshift])
                self.pix[x,y].config(bg=self.color)
            elif self.pix[x,y].cget("bg") != "white":
                self.pix[x,y].config(bg=self.color)
        else:
            if self.pix[x,y].cget("bg") != "white":
                self.wallcoord.remove([x+self.xshift,y+self.yshift])
                self.pix[x,y].config(bg=self.color)
            
    # Create a line between last two points if they are on the same line
    def createline(self):
        # Finding out which row
        if self.end1[0] == self.end2[0]:
            if self.end1[1] < self.end2[1]:
                while self.end2[1]-1 > self.end1[1]:
                    self.end2[1] -= 1                                                                        # one end gets closer to the other end
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":  # if white is chosen
                        self.wallcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])           # remove the pix
                    else:                                                                                    # if the color chosen isnt white
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":                        # and if the pix in between are white
                            self.wallcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])       # appends all the coords in between (therefore, only empty pix are appended)
                    if self.end2[1] >= 0 and self.end2[1] < 20:                                              # shows only the ones within the frame
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)
            elif self.end1[1] > self.end2[1]:
                while self.end2[1]+1 < self.end1[1]:
                    self.end2[1] += 1
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":  # if white is chosen
                        self.wallcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])           # remove the pix
                    else:
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":
                            self.wallcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                    if self.end2[1] >= 0 and self.end2[1] < 20:
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)        
        elif self.end1[1] == self.end2[1]:
            if self.end1[0] < self.end2[0]:
                while self.end2[0]-1 > self.end1[0]:
                    self.end2[0] -= 1
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":  # if white is chosen
                        self.wallcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])           # remove the pix
                    else:
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":
                            self.wallcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                    if self.end2[0] >= 0 and self.end2[0] < 20:
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)
            if self.end1[0] > self.end2[0]:
                while self.end2[0]+1 < self.end1[0]:
                    self.end2[0] += 1
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":  # if white is chosen
                        self.wallcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])           # remove the pix
                    else:
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":
                            self.wallcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                    if self.end2[0] >= 0 and self.end2[0] < 20:
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)

