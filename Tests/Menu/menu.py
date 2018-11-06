import tkinter as tk
import os
import pickle
def create_gui():
    gui = tk.Frame(height=800,width=800)
    gui.place(x=0,y=0)

    mapselect = tk.Button(gui,text="Map Selection",command=lambda:fileopening("mapselect"),width=12)
    mapselect.place(x=350,y=200)
    mapet = tk.Button(gui,text="Map Editor",command=lambda:fileopening("mapeditor"),width=12)
    mapet.place(x=350,y=230)
    settings = tk.Button(gui,text="Settings",command=lambda:fileopening("settings"),width=12)
    settings.place(x=350,y=260)
    programexit = tk.Button(gui, text="Quit", command=root.destroy,width=12)
    programexit.place(x=350,y=290)

def fileopening(x):
    if "mapselect":
            pickle.load(open(os.path.join(MapET/Tests/MapPlay/play.py)
        

#Main app thing
thingy = tk.Tk()
root.geometry("800x800")
create_gui()
#frame for buttons
buttons = tk.Frame(root)
buttons.place(y=30)


root.mainloop()