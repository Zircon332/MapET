import tkinter as tk
import pickle
import os

# Controls for Map Play
class SetPlayControls():
    def __init__(self,parent,screen,player,playercoord,speedmult,bordersize,zoomsize,camcoord,objectcoord,objectcolor,objecttypes,objecttypecolor,screenobjectcoord,follow):
        # Carry over data
        self.parent = parent
        self.playercoord = playercoord
        self.speedmult = speedmult
        self.bordersize = bordersize
        self.zoomsize = zoomsize
        self.camcoord = camcoord
        self.objectcoord = objectcoord
        self.objectcolor = objectcolor
        self.objecttypes = objecttypes
        self.objecttypecolor = objecttypecolor
        self.screenobjectcoord = screenobjectcoord
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
        # test if where ur going is a object
        self.test_x = self.playercoord[0] + self.x
        self.test_y = self.playercoord[1] + self.y
        if [self.test_x,self.test_y] not in self.objectcoord:            
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
        for i in self.objectcoord:
            self.screenx = i[0] - self.camcoord[0] 
            self.screeny = i[1] - self.camcoord[1]
            if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                self.screenobjectcoord.append([self.screenx,self.screeny])
        # update screen in camfollow mode
        self.zoomratio = 10 * self.bordersize / self.zoomsize
        self.screen.delete(tk.ALL)      #Delete previous things in screen
        #Create player at center
        self.player = self.screen.create_rectangle(self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,self.zoomsize/2*self.zoomratio+self.zoomratio,fill="red")
        #Set then clear the object coordinates on the screen
        for i in self.screenobjectcoord:
            color = self.objectcolor[i[0]+self.camcoord[0],i[1]+self.camcoord[1]]
            self.screen.create_rectangle(i[0]*self.zoomratio,i[1]*self.zoomratio,i[0]*self.zoomratio+self.zoomratio,i[1]*self.zoomratio+self.zoomratio,fill=color,outline=color)
        del self.screenobjectcoord[:]


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
        self.color = "grey"             # Default chosen color

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
                self.pix[x,y].bind("<1>",lambda event, x=x,y=y: self.toggleobjects(x,y))


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

        # display new objects
        for objects in self.objectcoord:
            if objects[0]-self.cameracoord[0] >= 0 and objects[0]-self.cameracoord[0] < 20 and objects[1]-self.cameracoord[1] >= 0 and objects[1]-self.cameracoord[1] < 20:
                self.pix[objects[0]-self.cameracoord[0],objects[1]-self.cameracoord[1]].config(bg=self.objectcolor[objects[0],objects[1]])

    # makes every grid white (doesn't delete coords)
    def clearscreen(self):
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.pix[x,y].config(bg="white")
                

    # Create or remove grid when clicked
    def toggleobjects(self,x,y):
        self.end2 = self.end1
        self.end1 = [x,y]
        if self.color != "white":
            if self.pix[x,y].cget("bg") == self.color:
                self.objectcoord.remove([x+self.xshift,y+self.yshift])      # remove coord
                del self.objectcolor[x+self.xshift,y+self.yshift]           # remove object color at that coord
                self.pix[x,y].config(bg="white")                            # remove display on that grid
            elif self.pix[x,y].cget("bg") == "white":
                self.objectcoord.append([x+self.xshift,y+self.yshift])      # add coord
                self.objectcolor[x+self.xshift,y+self.yshift] = self.color  # add object color at that coord
                self.pix[x,y].config(bg=self.color)                         # Display color at that grid
            elif self.pix[x,y].cget("bg") != "white":
                self.objectcolor[x+self.xshift,y+self.yshift] = self.color  # changed object color at that coord
                self.pix[x,y].config(bg=self.color)                         # Display color at that grid
        else:
            if self.pix[x,y].cget("bg") != "white":
                self.objectcoord.remove([x+self.xshift,y+self.yshift])        # remove coord
                del self.objectcolor[x+self.xshift,y+self.yshift]           # remove object color at that coord
                self.pix[x,y].config(bg=self.color)                         # Display color at that grid
            
    # Create a line between last two points if they are on the same line
    def createline(self):
        # Finding out which row
        if self.end1[0] == self.end2[0]:
            if self.end1[1] < self.end2[1]:
                while self.end2[1]-1 > self.end1[1]:
                    self.end2[1] -= 1                                                                        # one end gets closer to the other end
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":  # if white is chosen and the tile isnt white
                        self.objectcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])         # remove the pix
                        del self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift]              # remove object color at that coord
                    else:                                                                                    # if the color chosen isnt white
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":                        # and if the pix in between are white
                            self.objectcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])     # appends all the coords in between (only empty pix are appended)
                            self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift] = self.color # add object color at that coord
                    if self.end2[1] >= 0 and self.end2[1] < 20:                                              # shows only the ones within the frame
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)
            elif self.end1[1] > self.end2[1]:
                while self.end2[1]+1 < self.end1[1]:
                    self.end2[1] += 1
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":
                        self.objectcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                        del self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift]
                    else:
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":
                            self.objectcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                            self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift] = self.color
                    if self.end2[1] >= 0 and self.end2[1] < 20:
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)        
        elif self.end1[1] == self.end2[1]:
            if self.end1[0] < self.end2[0]:
                while self.end2[0]-1 > self.end1[0]:
                    self.end2[0] -= 1
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":
                        self.objectcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                        del self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift]
                    else:
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":
                            self.objectcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                            self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift] = self.color
                    if self.end2[0] >= 0 and self.end2[0] < 20:
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)
            if self.end1[0] > self.end2[0]:
                while self.end2[0]+1 < self.end1[0]:
                    self.end2[0] += 1
                    if self.color == "white" and self.pix[self.end2[0],self.end2[1]].cget("bg") != "white":
                        self.objectcoord.remove([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                        del self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift]
                    else:
                        if self.pix[self.end2[0],self.end2[1]].cget("bg") == "white":
                            self.objectcoord.append([self.end2[0]+self.xshift,self.end2[1]+self.yshift])
                            self.objectcolor[self.end2[0]+self.xshift,self.end2[1]+self.yshift] = self.color
                    if self.end2[0] >= 0 and self.end2[0] < 20:
                        self.pix[self.end2[0],self.end2[1]].config(bg=self.color)

