#Create and edit maps
import tkinter as tk
import config
end1 = end2 = 0
def mapedit():
    
    
    def togglewall(i):
        global end1
        global end2
        end2 = end1
        end1 = i
        if pix[i].cget("bg") == "grey":
            pix[i].config(bg="white")
        else:
            pix[i].config(bg="grey")

    #Update the new map into the list config.wallcoord
    def updatemap():
        tempwallcoord = []
        for i in range(config.bordersize**2):
            if pix[i].cget("bg") == "grey":
                xi = i
                yi = 0
                while xi >= config.bordersize:
                    xi -= config.bordersize
                    yi += 1
                coord = [int(xi),int(yi)]
                tempwallcoord.append(coord)
        config.wallcoord = tempwallcoord
        print(config.wallcoord)
        showcoord.config(text=config.wallcoord)
                
    #Shows existing walls
    def setwall():
        for walls in config.wallcoord:
            index = walls[0] + (config.bordersize * walls[1])
            pix[index].config(bg="grey")

    def switchplay():
        mapapp.withdraw()
        config.root.deiconify()

    def create_line():
        global end1
        global end2
        #which row
        if end1//20 == end2//20:
            if end1 < end2:
                while end2-1 > end1:
                    end2 -= 1
                    pix[end2].config(bg="grey")
            if end1 > end2:
                while end2+1 < end1:
                    end2 += 1
                    pix[end2].config(bg="grey")        
        elif str(end1)[-1] == str(end2)[-1]:
            if end1 < end2:
                while end2-20 > end1:
                    end2 -= 20
                    pix[end2].config(bg="grey")
            if end1 > end2:
                while end2+20 < end1:
                    end2 += 20
                    pix[end2].config(bg="grey")
        

    mapapp = tk.Tk()
    mapapp.title("MapEditor")
    mapapp.geometry("800x700+0+0")

    showcoord = tk.Label(mapapp,text=config.wallcoord)
    showcoord.place(x=10,y=10)

    frame = tk.Frame(mapapp)
    frame.place(x=0,y=100)

    c=0
    pix=[]
    for y in range(config.bordersize):
        for x in range(config.bordersize):
            pix.append(tk.Label(frame,height=1,width=2,background="white",bd=2,relief="groove"))
            pix[c].grid(column=x,row=y)
            c = c + 1

    for i in range(config.bordersize**2):
        pix[i].bind("<1>",lambda event, i=i: togglewall(i))

    #Sets up previously created walls
    setwall()

    updatebutton = tk.Button(mapapp,text="Update new map",command=updatemap)
    updatebutton.place(x=0,y=40)

    switchbutton = tk.Button(mapapp,text="Switch to Play mode",command=switchplay)
    switchbutton.place(x=450,y=50)

    linebutton = tk.Button(mapapp,text="Make a line from last two points",command=create_line)
    linebutton.place(x=450,y=100)
    
    mapapp.mainloop()

#CamFollow
pos = [2,2]
speed_mult = 1

#Set border size
bordersize = 50
zoomsize = 10

#Camera from position of player, top left
camcoord = [pos[0]-zoomsize/2, pos[1]-zoomsize/2]
def set_map():
    config.screen.delete(tk.ALL)
    set_wall()
    for i in config.wallcoord:
        config.screen.create_rectangle(i[0]*10,i[1]*10,i[0]*10+10,i[1]*10+10,fill="grey",outline="grey")

def set_wall():
    bds = config.bordersize * 10
    border = config.screen.create_polygon([0,0,bds,0,bds,bds,0,bds,0,0,10,0,10,bds-10,bds-10,bds-10,bds-10,10,0,10],fill="grey",outline="grey")
    config.player = config.screen.create_rectangle(config.pos[0]*10,config.pos[1]*10,config.pos[0]*10+10,config.pos[1]*10+10,fill="red")

def followswitch():
    if config.follow == 0:
        config.follow = 1
        for i in config.wallcoord:
            screenx = i[0] - config.camcoord[0] 
            screeny = i[1] - config.camcoord[1]
            if screenx >= 0 and screenx <= config.zoomsize and screeny >= 0 and screeny <= config.zoomsize:
                config.screen_wallcoord.append([screenx,screeny])
        zoomratio = 10 * config.bordersize / config.zoomsize
        config.screen.delete(tk.ALL)
        config.player = config.screen.create_rectangle(config.zoomsize/2*zoomratio,config.zoomsize/2*zoomratio,config.zoomsize/2*zoomratio+zoomratio,config.zoomsize/2*zoomratio+zoomratio,fill="red")
        for i in config.screen_wallcoord:
            config.screen.create_rectangle(i[0]*zoomratio,i[1]*zoomratio,i[0]*zoomratio+zoomratio,i[1]*zoomratio+zoomratio,fill="grey",outline="grey")
        del config.screen_wallcoord[:]
    else:
        config.follow = 0
        set_map()
         
#Set map coords from file
config.wallcoord = pickle.load(open(os.path.join(os.path.expanduser('~'),'Desktop\MapET\Tests\MapPlay\data',"DamienFace.p"),"rb"))

#Application with size and position, created in config.py
config.root.geometry(config.screen_size)

#Playground
config.screen.place(x=10,y=10)
set_map()

#set key controls
kct.set_controls()

switch = tk.Button(config.root,text="Switch to Follow", command=followswitch)
switch.place(x=700,y=100)

config.root.mainloop()
