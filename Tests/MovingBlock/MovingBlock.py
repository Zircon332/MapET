import tkinter as tk

#initial position
posx = 300
posy = 250

def move(x, y):
    global posx
    global posy
    posx += x
    posy -= y
    player.place(x=posx,y=posy)
    
def printxy():
    global posx
    global posy
    print(posx, posy)

#moving with keys
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

#Main app thing
root = tk.Tk()
root.geometry("800x700")

#frame for buttons
buttons = tk.Frame(root)
buttons.grid(row=30,column=20)

#the buttons with commands
leftb = tk.Button(buttons,text="LEFT",fg="black",command=(lambda:move(-10,0)),height=2,width=5)
upb = tk.Button(buttons,text="UP",fg="black",command=(lambda:move(0,10)),height=2,width=5)
downb = tk.Button(buttons,text="DOWN",fg="black",command=(lambda:move(0,-10)),height=2,width=5)
rightb = tk.Button(buttons,text="RIGHT",fg="black",command=(lambda:move(10,0)),height=2,width=5)
printb = tk.Button(root,text="PrintCoords",fg="black",command=lambda: printxy(),height=2,width=10)

#placing the buttons
leftb.grid(row=2, column=0)
upb.grid(row=1,column=1)
downb.grid(row=2,column=1)
rightb.grid(row=2,column=2)
printb.place(x=700,y=50)

#This black box thingy(a frame for you to live in)
playground = tk.Frame(root, height=500, width=600, bd=1, bg="black")
playground.grid(row=0,column=0, padx=5,pady=5)

#Key binding
frame = tk.Frame(root, width=100, height=100,bg="blue")
frame.bind("<Key>", key)
frame.bind("<Up>", lambda event, x=0,y=10: move(x,y))
frame.bind("<Down>", lambda event, x=0,y=-10: move(x,y))
frame.bind("<Left>", lambda event, x=-10,y=0: move(x,y))
frame.bind("<Right>", lambda event, x=10,y=0: move(x,y))
frame.grid(row=10,column=0)
frame.focus_set()

#Hey it's you
photo = tk.PhotoImage(file="boi.gif")
player = tk.Label(playground,image=photo,width=5,height=5)
player.place(x=posx,y=posy)

#the end
root.mainloop()
