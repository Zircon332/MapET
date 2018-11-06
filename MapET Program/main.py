import tkinter as tk
from tkinter import filedialog
import config  
import input 
import play
import mapet
import pickle
#Unfinished Things
#Center buttons
#menu bar functions
class MainApplication(tk.Frame):
    #Variables
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+%d+%d" % (self.screen_width,self.screen_height,0,0))
        self.parent.attributes("-fullscreen", False)
        self.createguif()

    def createguif(self):
        self.menubar = tk.Menu(self.parent)
        # create a pulldown menu, and add it to the menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=lambda:self.filedialogf())
        self.filemenu.add_command(label="Save", command=print("test"))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # create more pulldown menus
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=print("test"))
        self.editmenu.add_command(label="Copy", command=print("test"))
        self.editmenu.add_command(label="Paste", command=print("test"))
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=print("test"))
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # display the menu
        self.parent.config(menu=self.menubar)

        self.framebtn = tk.Frame(self, bg="black", height=100,width=100)
        self.framebtn.place(x=10,y=10)
        self.mapselectbtn = tk.Button(self.framebtn,text="Map Selection",command=lambda:self.fileopeningf("mapselect"),width=12)
        self.mapselectbtn.grid(row=0)
        self.mapetbtn = tk.Button(self.framebtn,text="Map Editor",command=lambda:self.fileopeningf("mapeditor"),width=12)
        self.mapetbtn.grid(row=1)
        self.settingsbtn = tk.Button(self.framebtn,text="Settings",command=lambda:self.fileopeningf("settings"),width=12)
        self.settingsbtn.grid(row=2)
        self.programexitbtn = tk.Button(self.framebtn, text="Quit", command=root.destroy,width=12)
        self.programexitbtn.grid(row=3)
    
    def fileopeningf(self,file):
        self.mapselectbtn.grid_forget()
        self.mapetbtn.grid_forget()
        self.settingsbtn.grid_forget()
        self.programexitbtn.grid_forget()
        if file == "mapselect":
            playgame = play.PlayGame
        elif file == "mapeditor":
            mapet.mapeditorf()
        elif file == "settings":
            self.settingsf()

    def settingsf(self):
        self.fullscreenbtn = tk.Button(self.framebtn,text="Toggle Fullscreen",command=lambda:self.fullscreenf(),width=12)
        self.fullscreenbtn.grid(row=0)
        self.mapetbtn = tk.Button(self.framebtn,text="Map Editor",command=lambda:self.fileopeningf("mapeditor"),width=12,padx=10,pady=10)
        self.mapetbtn.grid(row=1)
        self.settingsbtn = tk.Button(self.framebtn,text="Settings",command=lambda:self.fileopeningf("settings"),width=12)
        self.settingsbtn.grid(row=2)
        self.programexitbtn = tk.Button(self.framebtn, text="Quit", command=root.destroy,width=12)
        self.programexitbtn.grid(row=3)

    def fullscreenf(self):
        self.parent.attributes("-fullscreen", not self.parent.attributes('-fullscreen'))
    
    def filedialogf(self):
        self.filedialogthing = filedialog.askopenfilename()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
