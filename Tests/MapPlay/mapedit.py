#Create and edit maps

import tkinter as tk
import config

def mapedit():
    def togglewall(i):
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
                while xi >= 20:
                    xi -= 20
                    yi += 1
                coord = [int(xi),int(yi)]
                tempwallcoord.append(coord)
        config.wallcoord = tempwallcoord
        print(config.wallcoord)
        showcoord.config(text=config.wallcoord)
                
    #Shows existing walls
    def setwall():
        for walls in config.wallcoord:
            index = walls[0] + (20 * walls[1])
            pix[index].config(bg="grey")

    def switchplay():
        mapapp.withdraw()
        config.root.deiconify()
        
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

    mapapp.mainloop()
