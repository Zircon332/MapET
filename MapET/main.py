import tkinter as tk
from tkinter import filedialog
import choosemap
import play
import mapet
import pickle

# Start the program
root = tk.Tk()

# Main menu and Map selection menu
mainmenu = choosemap.MainApplication(root)
mainmenu.pack(side="top", fill="both", expand=True)

root.mainloop()
