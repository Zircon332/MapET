import tkinter as tk

#camera is always at center
camera = [0,0]
playerpos = [0,0]
block1 = [160,100]
block2 = [20,0]
x = 100
y =100
block1_screen = [block1[0],block1[1]]
block2_screen = [block2[0],block2[1]]

def up(i):
    global x
    global y
    y -= 20
    camera[0] = x
    camera[1] = y
    find_screen()
    update_map()
def down(i):
    global x
    global y
    y += 20
    camera[0] = x
    camera[1] = y
    find_screen()
    update_map()
def left(i):
    global x
    global y
    x -= 20
    camera[0] = x
    camera[1] = y
    find_screen()
    update_map()
def right(i):
    global x
    global y
    x += 20
    camera[0] = x
    camera[1] = y
    find_screen()
    update_map()
    
def find_screen():
    block1_screen[0] = block1[0] - camera[0] 
    block1_screen[1] = block1[1] - camera[1]
    block2_screen[0] = block2[0] - camera[0] 
    block2_screen[1] = block2[1] - camera[1]
    
    
def update_map():
    cell1.place(x=block1_screen[0], y=block1_screen[1])    
    cell2.place(x=block2_screen[0], y=block2_screen[1])    

root = tk.Tk()
root.geometry("400x400+1+1")

frame = tk.Frame(root,height=220,width=220,bg="white")
frame.grid(column=0,row=0)
frame.grid_propagate(False)

player = tk.Label(frame,height=1,width=2, bg="red")
player.place(x=100, y=100)
cell1 = tk.Label(frame,height=1,width=2, bg="blue")
cell1.place(x=block1[0], y=block1[1])
cell2 = tk.Label(frame,height=1,width=2, bg="black")
cell2.place(x=block2[0], y=block2[1])

frame.focus_set()
frame.bind("<Up>",up)
frame.bind("<Down>",down)
frame.bind("<Left>",left)
frame.bind("<Right>",right)

root.mainloop()
