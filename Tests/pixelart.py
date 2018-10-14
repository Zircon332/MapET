import tkinter as tk

#creates the artboard
def create_new():
    artboard = tk.Frame(root,height=100,width=100,bg='red')
    artboard.place(x=20,y=20)
    
    #creates a 10x10 artboard
    global pix
    c = 0
    pix = []
    for y in range(0,10):
        for x in range(0,10):
            pix.append(tk.Label(artboard,height=1,width=2,background="white",bd=2,relief="groove"))
            pix[c].grid(column=x,row=y)
            c = c + 1
            
#creates the GUI
def create_gui():
    global current
    gui = tk.Frame(height=200,width=200)
    gui.place(x=300,y=20)
    choose = tk.Label(gui,text="Choose a color and a grid")
    choose.place(x=0,y=0)
    current = tk.Label(gui,text="Currently: none")
    current.place(x=20,y=20)

    global color
    red = tk.Button(gui,text="red",command=lambda:choose_color("red"),bg="red")
    red.place(x=10,y=50)
    blue = tk.Button(gui,text="blue",command=lambda:choose_color("blue"),bg="blue")
    blue.place(x=60,y=50)
    grey = tk.Button(gui,text="grey",command=lambda:choose_color("grey"),bg="grey")
    grey.place(x=10,y=80)
    white = tk.Button(gui,text="white",command=lambda:choose_color("white"),bg="white")
    white.place(x=60,y=80)

def choose_color(new_color):
    global current
    global color
    color = new_color
    print(color)
    current.config(text="Currently: " + color, fg=color)

def set_color(i):
    global pix
    global colour
    print(i)
    pix[i].config(bg=color)

root = tk.Tk()
root.geometry("500x500")

color = "white"
create_gui()
create_new()
for i in range(100):
    pix[i].bind("<Button-1>",lambda event, i=i: set_color(i))

root.mainloop()
