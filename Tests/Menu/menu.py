import tkinter as tk

def create_gui():
    gui = tk.Frame(height=1000,width=1000)
    gui.place(x=0,y=0)

    mapselect = tk.Button(gui,text="Map Selection",command=print("test1"))
    mapselect.place(x=100,y=0)
    mapet = tk.Button(gui,text="Map Editor",command=print("test2"))
    mapet.place(x=100,y=30)
    settings = tk.Button(gui,text="Settings",command=print("test3"))
    settings.place(x=50,y=60)
    exit = tk.Button(gui,text="Exit",command=print("test4"))
    exit.place(x=100,y=90)
#Main app thing
root = tk.Tk()
root.geometry("400x400")
create_gui()
#frame for buttons
buttons = tk.Frame(root)
buttons.place(y=30)


root.mainloop()