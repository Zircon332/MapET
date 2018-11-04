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
