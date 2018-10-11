import tkinter as tk

number = 0
botadd = 0
plus = 0
globalplus = 0

def botaddition(winpoint):
    global number
    global botadd
    botadd = winpoint - number
    if botadd > 10:
        botadd = 1
    number += botadd

#The game itself
def game():
    global playerturn
    global number
    global botadd
    global plus
    global botadd
    if number < 100:
        if number < 12:
            botaddition(12)
        elif number < 23:
            botaddition(23)
        elif number < 34:
            botaddition(34)
        elif number < 45:
            botaddition(45)
        elif number < 56:
            botaddition(56)
        elif number < 67:
            botaddition(67)
        elif number < 78:
            botaddition(78)
        elif number < 89:
            botaddition(89)
        elif number < 100:
            botaddition(100)
        if number == 100:
            print("You Lose")
    elif number == 100:
        print("You Win!")
    shownumber.config(text=str(number))
    showplus.config(text=str(globalplus))
    showbotadd.config(text=str(botadd))
def add(plus):
    global globalplus
    global botadd
    global number
    number += plus
    globalplus = plus
    shownumber.config(text=str(number))
    showplus.config(text=str(plus))
    showbotadd.config(text=str(botadd))
    game()
def botstart():
    global botadd
    global number
    if number == 0:
        botadd = 5
        number = botadd
    shownumber.config(text=str(number))
    showbotadd.config(text=str(botadd))
def restart():
    global number
    global globalplus
    global botadd
    number = 0
    globalplus = 0
    botadd = 0
    shownumber.config(text=str(number))
    showplus.config(text=str(plus))
    showbotadd.config(text=str(botadd))

        
#Main app thing
root = tk.Tk()
root.geometry("800x200")

#frame for buttons
buttons = tk.Frame(root)
buttons.place(y=30)

#the buttons with commands
add1 = tk.Button(buttons,text="+1",fg="black",command=lambda:add(1),height=2,width=5)
add2 = tk.Button(buttons,text="+2",fg="black",command=lambda:add(2),height=2,width=5)
add3 = tk.Button(buttons,text="+3",fg="black",command=lambda:add(3),height=2,width=5)
add4 = tk.Button(buttons,text="+4",fg="black",command=lambda:add(4),height=2,width=5)
add5 = tk.Button(buttons,text="+5",fg="black",command=lambda:add(5),height=2,width=5)
add6 = tk.Button(buttons,text="+6",fg="black",command=lambda:add(6),height=2,width=5)
add7 = tk.Button(buttons,text="+7",fg="black",command=lambda:add(7),height=2,width=5)
add8 = tk.Button(buttons,text="+8",fg="black",command=lambda:add(8),height=2,width=5)
add9 = tk.Button(buttons,text="+9",fg="black",command=lambda:add(9),height=2,width=5)
add10 = tk.Button(buttons,text="+10",fg="black",command=lambda:add(10),height=2,width=5)
restartbutton = tk.Button(buttons,text="Restart",command=lambda:restart(),height=2,width=5)
botstartbutton = tk.Button(buttons,text="Let the bot go first",command=lambda:botstart(),height=2,width=15)


#placing(gridding) the buttons
add1.grid(column=0,row=1)
add2.grid(column=1,row=1)
add3.grid(column=2,row=1)
add4.grid(column=3,row=1)
add5.grid(column=4,row=1)
add6.grid(column=5,row=1)
add7.grid(column=6,row=1)
add8.grid(column=7,row=1)
add9.grid(column=8,row=1)
add10.grid(column=9,row=1)
restartbutton.grid(column=10,row=0)
botstartbutton.place(x=0,y=0)

intro = tk.Label(root, text="Each player chooses a number that is added together, first to get to reach 100 wins")
shownumber = tk.Label(root, text=number)
showplus = tk.Label(root, text=plus, fg="blue",bg="white")
showbotadd = tk.Label(root, text=botadd,fg="red",bg="white")
addsymbol = tk.Label(root, text="+")
win = tk.Label(root,text="")

intro.place(x=0,y=0)
showplus.place(x=20,y=150)
showbotadd.place(x=60,y=150)
addsymbol.place(x=40,y=150)
shownumber.place(x=300,y=150)
win.place(x=300,y=200)

#the end
root.mainloop()
