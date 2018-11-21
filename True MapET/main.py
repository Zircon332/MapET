import tkinter as tk
import menu
import input_handling
import process1
import process2

# Start the program
root = tk.Tk()
self = root
# Main Menu
mainmenu = menu.MainApplication(root)
mainmenu.pack(side="top", fill="both", expand=True)
print(mainmenu.buttonframe.winfo_children())

# Menu for choosing map
cm = menu.ChooseMap(mainmenu.parent, mode)



# Process

if mode == "mapselect":
    pl = play.PlayMap(menu.MainApplication.parent, menu.mapname,[],{}, menu.playercoord, menu.objecttypes, menu.objecttypecolor)
elif mode == "mapeditor":
    mp = mapet.Mapedit(menu.parent, menu.mapname, 20, [], {}, menu.objecttypes, menu.objecttypecolor)


root.mainloop()
