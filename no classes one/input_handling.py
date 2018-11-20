import tkinter as tk
import pickle
import os

# Controls for Map Play
def __init__(self,parent,screen,player,playercoord,speedmult,bordersize,zoomsize,camcoord,wallcoord,screenwallcoord,follow):
    # Carry over data
     parent = parent
     playercoord = playercoord
     speedmult = speedmult
     bordersize = bordersize
     zoomsize = zoomsize
     camcoord = camcoord
     wallcoord = wallcoord
     screenwallcoord = screenwallcoord
     follow = follow
     screen = screen
     player = player
    
    #Bind movements
     parent.bind_all("<Up>", lambda event, x=0,y=-1:  move(x,y))
     parent.bind_all("<Down>", lambda event, x=0,y=1:  move(x,y))
     parent.bind_all("<Left>", lambda event, x=-1,y=0:  move(x,y))
     parent.bind_all("<Right>", lambda event, x=1,y=0:  move(x,y))
     parent.bind_all("<Shift_L>", lambda event, x=1,y=0:  move(x,y))

# move the player according to input
def move(self, x, y):
     x,  y = x, y
    # Increase speed with multiplier, if any
     x *=  speedmult
     y *=  speedmult
    # test if where ur going is a wall
     test_x =  playercoord[0] +  x
     test_y =  playercoord[1] +  y
    if [ test_x, test_y] not in  wallcoord:            
        if  test_x > 0 and  test_x < ( bordersize-1):
             playercoord[0] +=  x
             camcoord[0] +=  x
            if  follow == 0:                            # normal moving
                 screen.move( player,  x*10, 0)
            else:                                           # cam follow move
                 cammove()
        if  test_y > 0 and  test_y < ( bordersize-1):
             playercoord[1] +=  y
             camcoord[1] += y
            if  follow == 0:                            # normal moving
                 screen.move( player, 0,  y*10)
            else:                                           # cam follow move
                 cammove()
     screen.update_idletasks()

# append everything that will be shown in screen into a list
def cammove(self):
    for i in  wallcoord:
         screenx = i[0] -  camcoord[0] 
         screeny = i[1] -  camcoord[1]
        if  screenx >= 0 and  screenx <=  zoomsize and  screeny >= 0 and  screeny <=  zoomsize:
             screenwallcoord.append([ screenx, screeny])
    # update screen in camfollow mode
     zoomratio = 10 *  bordersize /  zoomsize
     screen.delete(tk.ALL)      #Delete previous things in screen
    #Create player at center
     player =  screen.create_rectangle( zoomsize/2* zoomratio, zoomsize/2* zoomratio, zoomsize/2* zoomratio+ zoomratio, zoomsize/2* zoomratio+ zoomratio,fill="red")
    #Set then clear the wall coordinates on the screen
    for i in  screenwallcoord:
         screen.create_rectangle(i[0]* zoomratio,i[1]* zoomratio,i[0]* zoomratio+ zoomratio,i[1]* zoomratio+ zoomratio,fill="grey",outline="grey")
    del  screenwallcoord[:]


# Controls for MapEdit
def __init__(self,parent,gridsize,objectcoord,objectcolor,objecttypes,objecttypecolor,gridaxisx,gridaxisy,xshift,yshift,pix,end1,end2):
    # Carry over data
     parent = parent
     gridsize = gridsize
     objectcoord = objectcoord
     objectcolor = objectcolor
     objecttypes = objecttypes
     objecttypecolor = objecttypecolor
     gridaxisx = gridaxisx
     gridaxisy = gridaxisy
     xshift = xshift
     yshift = yshift
    
     pix = pix
     end1 = end1
     end2 = end2
     cameracoord = [0,0]
     color = "grey"             # Default chosen color

     parent.bind_all("<Up>", lambda event, x=0,y=-1:  shiftmap(x,y))
     parent.bind_all("<Down>", lambda event, x=0,y=1:  shiftmap(x,y))
     parent.bind_all("<Left>", lambda event, x=-1,y=0:  shiftmap(x,y))
     parent.bind_all("<Right>", lambda event, x=1,y=0:  shiftmap(x,y))

    # Opens menu for going back
     parent.bind_all("<Escape>",  backmenu)

    # Undo bind
     parent.bind_all("<Control-z>", lambda event, x=1,y=0:  shiftmap(x,y))
    
    # Bind clicks to grid
    for x in range( gridsize):
        for y in range( gridsize):
             pix[x,y].bind("<1>",lambda event, x=x,y=y:  toggleobjects(x,y))


def backmenu(self,key):
    print()
##         frame.destroy()
##         showcoord.destroy()
##         typeframe.destroy()
##         btnframe.destroy()


# shift the coords of the grid
def shiftmap(self,x,y):
    if  xshift+x >= 0 and  yshift+y >= 0:
         xshift += x
         yshift += y
        # update the axes numbers
        for i in range(len( gridaxisx)):
             gridaxisx[i].config(text=i+ xshift)
             gridaxisy[i].config(text=i+ yshift)
        # Changing size of the axes
        if  xshift +  gridsize == 100:
            for i in  gridaxisx:
                i.config(font=("arial",6))
        elif  xshift +  gridsize == 99:
            for i in  gridaxisx:
                i.config(font=("arial",8))
        # keep track of clicked grid after moving
         end1[0] -= x
         end1[1] -= y
         end2[0] -= x
         end2[1] -= y
        # update map on screen
         updatescreenmap(x,y)

def updatescreenmap(self,x,y):
     cameracoord[0] += x
     cameracoord[1] += y
        
    # clear the screen
     clearscreen()  

    # display new walls
    for objects in  objectcoord:
        if objects[0]- cameracoord[0] >= 0 and objects[0]- cameracoord[0] < 20 and objects[1]- cameracoord[1] >= 0 and objects[1]- cameracoord[1] < 20:
            print( objectcolor,x,y)
             pix[objects[0]- cameracoord[0],objects[1]- cameracoord[1]].config(bg= objectcolor[objects[0],objects[1]])

# makes every grid white (doesn't delete coords)
def clearscreen(self):
    for x in range( gridsize):
        for y in range( gridsize):
             pix[x,y].config(bg="white")
            

# Create or remove grid when clicked
def toggleobjects(self,x,y):
     end2 =  end1
     end1 = [x,y]
    if  color != "white":
        if  pix[x,y].cget("bg") ==  color:
             objectcoord.remove([x+ xshift,y+ yshift])      # remove coord
            del  objectcolor[x+ xshift,y+ yshift]           # remove object color at that coord
             pix[x,y].config(bg="white")                            # remove display on that grid
        elif  pix[x,y].cget("bg") == "white":
             objectcoord.append([x+ xshift,y+ yshift])      # add coord
             objectcolor[x+ xshift,y+ yshift] =  color  # add object color at that coord
             pix[x,y].config(bg= color)                         # Display color at that grid
        elif  pix[x,y].cget("bg") != "white":
             objectcolor[x+ xshift,y+ yshift] =  color  # changed object color at that coord
             pix[x,y].config(bg= color)                         # Display color at that grid
    else:
        if  pix[x,y].cget("bg") != "white":
             objectcoord.remove([x+ xshift,y+ yshift])        # remove coord
            del  objectcolor[x+ xshift,y+ yshift]           # remove object color at that coord
             pix[x,y].config(bg= color)                         # Display color at that grid
        
# Create a line between last two points if they are on the same line
def createline(self):
    # Finding out which row
    if  end1[0] ==  end2[0]:
        if  end1[1] <  end2[1]:
            while  end2[1]-1 >  end1[1]:
                 end2[1] -= 1                                                                        # one end gets closer to the other end
                if  color == "white" and  pix[ end2[0], end2[1]].cget("bg") != "white":  # if white is chosen and the tile isnt white
                     objectcoord.remove([ end2[0]+ xshift, end2[1]+ yshift])         # remove the pix
                    del  objectcolor[ end2[0]+ xshift, end2[1]+ yshift]              # remove object color at that coord
                else:                                                                                    # if the color chosen isnt white
                    if  pix[ end2[0], end2[1]].cget("bg") == "white":                        # and if the pix in between are white
                         objectcoord.append([ end2[0]+ xshift, end2[1]+ yshift])     # appends all the coords in between (only empty pix are appended)
                         objectcolor[ end2[0]+ xshift, end2[1]+ yshift] =  color # add object color at that coord
                if  end2[1] >= 0 and  end2[1] < 20:                                              # shows only the ones within the frame
                     pix[ end2[0], end2[1]].config(bg= color)
        elif  end1[1] >  end2[1]:
            while  end2[1]+1 <  end1[1]:
                 end2[1] += 1
                if  color == "white" and  pix[ end2[0], end2[1]].cget("bg") != "white":
                     objectcoord.remove([ end2[0]+ xshift, end2[1]+ yshift])
                    del  objectcolor[ end2[0]+ xshift, end2[1]+ yshift]
                else:
                    if  pix[ end2[0], end2[1]].cget("bg") == "white":
                         objectcoord.append([ end2[0]+ xshift, end2[1]+ yshift])
                         objectcolor[ end2[0]+ xshift, end2[1]+ yshift] =  color
                if  end2[1] >= 0 and  end2[1] < 20:
                     pix[ end2[0], end2[1]].config(bg= color)        
    elif  end1[1] ==  end2[1]:
        if  end1[0] <  end2[0]:
            while  end2[0]-1 >  end1[0]:
                 end2[0] -= 1
                if  color == "white" and  pix[ end2[0], end2[1]].cget("bg") != "white":
                     objectcoord.remove([ end2[0]+ xshift, end2[1]+ yshift])
                    del  objectcolor[ end2[0]+ xshift, end2[1]+ yshift]
                else:
                    if  pix[ end2[0], end2[1]].cget("bg") == "white":
                         objectcoord.append([ end2[0]+ xshift, end2[1]+ yshift])
                         objectcolor[ end2[0]+ xshift, end2[1]+ yshift] =  color
                if  end2[0] >= 0 and  end2[0] < 20:
                     pix[ end2[0], end2[1]].config(bg= color)
        if  end1[0] >  end2[0]:
            while  end2[0]+1 <  end1[0]:
                 end2[0] += 1
                if  color == "white" and  pix[ end2[0], end2[1]].cget("bg") != "white":
                     objectcoord.remove([ end2[0]+ xshift, end2[1]+ yshift])
                    del  objectcolor[ end2[0]+ xshift, end2[1]+ yshift]
                else:
                    if  pix[ end2[0], end2[1]].cget("bg") == "white":
                         objectcoord.append([ end2[0]+ xshift, end2[1]+ yshift])
                         objectcolor[ end2[0]+ xshift, end2[1]+ yshift] =  color
                if  end2[0] >= 0 and  end2[0] < 20:
                     pix[ end2[0], end2[1]].config(bg= color)

