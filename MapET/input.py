import tkinter as tk
import pickle
import os

# Controls for main menu
# class SetMainControl():
#     def __init__(self,parent):
#         # Going back
#         self.parent.bind_all("<Escape>", self.backmenu)

#         def backmenu(self,key):
#             print()
    ##        self.frame.destroy()
    ##        self.showcoord.destroy()
    ##        self.typeframe.destroy()
    ##        self.btnframe.destroy()


# Controls for Map Play
class SetPlayControls():
    def __init__(self,parent,playframe,screen,player,playercoord,speedmult,bordersize,zoomsize,camcoord,objectcoord,objectcolor,objecttypes,objecttypecolor,goalcoord,follow,pix,playercoordxent,playercoordyent,speedmultent,bordersizexent,bordersizeyent,zoomsizeent,pixent,movekey):
        # Carry over data
        self.parent             = parent
        self.playframe          = playframe
        self.playercoord        = playercoord
        self.speedmult          = speedmult
        self.bordersizex        = bordersize
        self.bordersizey        = bordersize
        self.zoomsize           = zoomsize
        self.camcoord           = camcoord
        self.objectcoord        = objectcoord
        self.objectcolor        = objectcolor
        self.objecttypes        = objecttypes
        self.objecttypecolor    = objecttypecolor
        self.screenobjectcoord  = []
        self.screengoalcoord    = []
        self.goalcoord          = goalcoord
        self.follow             = follow
        self.screen             = screen
        self.player             = player
        self.pix                = pix
        self.playercoordxent    = playercoordxent
        self.playercoordyent    = playercoordyent
        self.speedmultent       = speedmultent
        self.bordersizexent     = bordersizexent
        self.bordersizeyent     = bordersizeyent
        self.zoomsizeent        = zoomsizeent
        self.pixent             = pixent
        self.movekey            = movekey
        
        #Bind movements
        if self.movekey == 0 or self.movekey == 2:
            self.parent.bind_all("<Up>",    lambda event, x=0,y=-1: self.move(x,y))
            self.parent.bind_all("<Down>",  lambda event, x=0,y=1: self.move(x,y))
            self.parent.bind_all("<Left>",  lambda event, x=-1,y=0: self.move(x,y))
            self.parent.bind_all("<Right>", lambda event, x=1,y=0: self.move(x,y))
        if self.movekey == 1 or self.movekey == 2:
            self.parent.bind_all("w", lambda event, x=0,y=-1: self.move(x,y))
            self.parent.bind_all("s", lambda event, x=0,y=1: self.move(x,y))
            self.parent.bind_all("a", lambda event, x=-1,y=0: self.move(x,y))
            self.parent.bind_all("d", lambda event, x=1,y=0: self.move(x,y))
            
        self.parent.bind_all("<Return>", lambda event, key=None: self.setconfig(key))    # Also restarts the map

    # move the player according to input
    def move(self, x, y):
        self.x, self.y = x, y
        # Increase speed with multiplier, if any
        for times in range(self.speedmult):
            # test if where ur going is a object
            self.test_x = self.playercoord[0] + self.x
            self.test_y = self.playercoord[1] + self.y
            if [self.test_x,self.test_y] not in self.objectcoord:            
                if self.test_x > 0:
                    self.playercoord[0] += self.x
                    self.camcoord[0] += self.x
                    if self.follow == 0:                            # normal moving
                        self.screen.move(self.player, self.x*self.pix, 0)
                    else:                                           # cam follow move
                        self.cammove()
                if self.test_y > 0:
                    self.playercoord[1] += self.y
                    self.camcoord[1] += y
                    if self.follow == 0:                            # normal moving
                        self.screen.move(self.player, 0, self.y*self.pix)
                    else:                                           # cam follow move
                        self.cammove()
        self.screen.update_idletasks()
        self.checkgoal()
        
    # append everything that will be shown in screen into a list
    def cammove(self):
        for i in self.objectcoord:
            self.screenx = i[0] - self.camcoord[0] 
            self.screeny = i[1] - self.camcoord[1]
            if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                self.screenobjectcoord.append([self.screenx,self.screeny])
        for i in self.goalcoord:
            self.screenx = i[0] - self.camcoord[0] 
            self.screeny = i[1] - self.camcoord[1]
            if self.screenx >= 0 and self.screenx <= self.zoomsize and self.screeny >= 0 and self.screeny <= self.zoomsize:
                self.screengoalcoord.append([self.screenx,self.screeny])
        # update screen in camfollow mode
        self.zoomratiox = self.pix * self.bordersizex / self.zoomsize
        self.zoomratioy = self.pix * self.bordersizey / self.zoomsize
        self.screen.delete(tk.ALL)      #Delete previous things in screen
        #Create player at center
        self.player = self.screen.create_rectangle(self.zoomsize/2*self.zoomratiox,self.zoomsize/2*self.zoomratioy,self.zoomsize/2*self.zoomratiox+self.zoomratiox,self.zoomsize/2*self.zoomratioy+self.zoomratioy,fill="red")
        #Set then clear the object coordinates on the screen
        for i in self.screenobjectcoord:
            color = self.objectcolor[i[0]+self.camcoord[0],i[1]+self.camcoord[1]]
            self.screen.create_rectangle(i[0]*self.zoomratiox,i[1]*self.zoomratioy,i[0]*self.zoomratiox+self.zoomratiox,i[1]*self.zoomratioy+self.zoomratioy,fill=color,outline=color)
        for i in self.screengoalcoord:
            self.screen.create_rectangle(i[0]*self.zoomratiox,i[1]*self.zoomratioy,i[0]*self.zoomratiox+self.zoomratiox,i[1]*self.zoomratioy+self.zoomratioy,fill="lightgreen",outline="lightgreen")
        del self.screenobjectcoord[:]
        del self.screengoalcoord[:]
        
        
    # Check if the player is at goal position
    def checkgoal(self):
        if self.playercoord in self.goalcoord:
            self.playframe.place_forget()
            self.win= tk.Label(self.parent,text="You win", font=("windings",100))
            self.win.place(relx=.5,rely=.5,anchor='c')
            print("You Win")

    # Changes the settings, restarts the map
    def setconfig(self,key):
        try:
            self.playercoord[0] = int(self.playercoordxent.get())
            self.playercoord[1] = int(self.playercoordyent.get())
            self.speedmult      = int(self.speedmultent.get())
            self.bordersizex    = int(self.bordersizexent.get())
            self.bordersizey    = int(self.bordersizeyent.get())
            self.zoomsize       = int(self.zoomsizeent.get())
            self.pix            = int(self.pixent.get())
        except:
            print("Only integers are allowed in config. Please re-enter the value.")
            
        self.screen.focus_set()                                                             # Set focus out of entry, focus to screen
        self.screen.config(width=self.bordersizex*self.pix, height=self.bordersizey*self.pix) # Change screen size
        self.screen.delete(tk.ALL)                                                          # Clear the screen
        # create a new player
        self.player = self.screen.create_rectangle(self.playercoord[0]*self.pix,self.playercoord[1]*self.pix,self.playercoord[0]*self.pix+self.pix,self.playercoord[1]*self.pix+self.pix,fill="red")
        # create new walls
        for i in self.objectcoord:
            color = self.objectcolor[i[0],i[1]]
            self.screen.create_rectangle(i[0]*self.pix,i[1]*self.pix,i[0]*self.pix+self.pix,i[1]*self.pix+self.pix,fill=color,outline=color) 
        self.camcoord = [self.playercoord[0] - self.zoomsize/2, self.playercoord[1] - self.zoomsize/2]  # Reset camcoord
        #self.move(0,0)
        
# Controls for MapEdit
class SetEditControls:
    def __init__(self,parent,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor,goalcoord,gridaxisx,gridaxisy,xshift,yshift,pix,end1,end2,movekey):
        # Carry over data
        self.parent          =  parent
        self.gridsize        =  gridsize
        self.objectcoord     =  objectcoord
        self.objectcolor     =  objectcolor
        self.objecttypes     =  objecttypes
        self.objecttypecolor =  objecttypecolor
        self.goalcoord       =  goalcoord
        self.gridaxisx       =  gridaxisx
        self.gridaxisy       =  gridaxisy
        self.xshift          =  xshift
        self.yshift          =  yshift
        self.movekey         =  movekey
        
        self.pix            = pix
        self.end1           = end1
        self.end2           = end2
        self.cameracoord    = [0,0]
        self.color          = "grey"             # Default chosen color

        if self.movekey == 0 or self.movekey == 2:
            self.parent.bind_all("<Up>",    lambda event, x=0,y=-1: self.shiftmap(x,y))
            self.parent.bind_all("<Down>",  lambda event, x=0,y=1:  self.shiftmap(x,y))
            self.parent.bind_all("<Left>",  lambda event, x=-1,y=0: self.shiftmap(x,y))
            self.parent.bind_all("<Right>", lambda event, x=1,y=0:  self.shiftmap(x,y))
        if self.movekey == 1 or self.movekey == 2:
            self.parent.bind_all("w", lambda event, x=0,y=-1:   self.shiftmap(x,y))
            self.parent.bind_all("s", lambda event, x=0,y=1:    self.shiftmap(x,y))
            self.parent.bind_all("a", lambda event, x=-1,y=0:   self.shiftmap(x,y))
            self.parent.bind_all("d", lambda event, x=1,y=0:    self.shiftmap(x,y))

        # Bind hot keys for selecting types
        for i in range(1,len(self.objecttypecolor)+2):
            self.parent.bind_all(str(i), lambda event,i=i: self.hotkeyselect(i))
        
    def hotkeyselect(self,i):
        if i > len(self.objecttypecolor):
            self.color = "lightgreen"
        else:
            self.color = self.objecttypecolor[i-1]

        # Bind clicks to grid
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.pix[x,y].bind("<1>",lambda event, x=x,y=y: self.toggleobjects(x,y))


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
        # clear the screen
        self.clearscreen()  

        # display new objects
        for objects in self.objectcoord:
            if objects[0]-self.xshift >= 0 and objects[0]-self.xshift < 20 and objects[1]-self.yshift >= 0 and objects[1]-self.yshift < 20:
                self.pix[objects[0]-self.xshift,objects[1]-self.yshift].config(bg=self.objectcolor[objects[0],objects[1]])
        for goals in self.goalcoord:
            if goals[0]-self.xshift >= 0 and goals[0]-self.xshift < 20 and goals[1]-self.yshift >= 0 and goals[1]-self.yshift < 20:
                self.pix[goals[0]-self.xshift,goals[1]-self.yshift].config(bg="lightgreen")
                

    # makes every grid white (doesn't delete coords)
    def clearscreen(self):
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                self.pix[x,y].config(bg="white")
                

    # Create or remove grid when clicked
    def toggleobjects(self,x,y):
        self.end2 = self.end1
        self.end1 = [x,y]
        if self.color == "lightgreen":                                      # For goals
            if self.pix[x,y].cget("bg") == self.color:      
                self.goalcoord.remove([x+self.xshift,y+self.yshift])        # remove coord
                self.pix[x,y].config(bg="white")                            # remove display on that grid
            elif self.pix[x,y].cget("bg") == "white":
                self.goalcoord.append([x+self.xshift,y+self.yshift])        # add coord
                self.pix[x,y].config(bg=self.color)                         # Display color at that grid
            elif self.pix[x,y].cget("bg") != "white":
                self.objectcoord.remove([x+self.xshift,y+self.yshift])      # remove coord
                del self.objectcolor[x+self.xshift,y+self.yshift]           # remove object color at that coord
                self.pix[x,y].config(bg=self.color)                         # Display color at that grid
        elif self.color != "white":
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
        else:                                                               # When white is chosen, for removing object
            if self.pix[x,y].cget("bg") != "white":
                self.objectcoord.remove([x+self.xshift,y+self.yshift])      # remove coord
                del self.objectcolor[x+self.xshift,y+self.yshift]           # remove object color at that coord
                self.pix[x,y].config(bg=self.color)                         # Display color at that grid
            
    # Create a line between last two points if they are on the same line
    def createline(self):
        if self.color == "lightgreen":
            print("You can't make lines with goals. Do it manually.")
        else:
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

