import tkinter as tk

posx = 0
posy = 0
root = tk.Tk()

def key(event):
    if repr(event.char) == "' '":
        print("Jumped")
    if repr(event.char) == "'w'":
        print("Up")
    if repr(event.char) == "'s'":
        print("Down")
    if repr(event.char) == "'a'":
        print("Left")
    if repr(event.char) == "'d'":
        print("Right")
        
def move(x, y):
    global posx
    global posy
        posx += x
    posy += y
    print(posx, " ", posy)

frame = tk.Frame(root, width=100, height=100,bg="blue")
frame.bind("<Key>", key)
frame.bind("<Up>", lambda event, x=0,y=1: move(x,y))
frame.bind("<Down>", lambda event, x=0,y=-1: move(x,y))
frame.bind("<Left>", lambda event, x=-1,y=0: move(x,y))
frame.bind("<Right>", lambda event, x=1,y=0: move(x,y))
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
