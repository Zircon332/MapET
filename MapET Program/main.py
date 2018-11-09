import tkinter as tk
from tkinter import filedialog
import choosemap
import play
import mapet
import pickle

#Unfinished Things
##Center buttons
##menu bar functions
class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("MapET")
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+%d+%d" % (self.screen_width,self.screen_height,0,0))
        self.parent.attributes("-fullscreen", False)
        self.createguif()

    #Creates logo, menubar and buttons
    def createguif(self):
        #Logo
        self.logoimg = tk.PhotoImage(file="images\logo.gif")
        self.mapetlogo =  tk.Label(self.parent, image=self.logoimg,anchor="c")
        self.mapetlogo.image = self.logoimg
        self.mapetlogo.place(relx=.5, rely=.2, anchor="c")
        self.menubar = tk.Menu(self.parent)
        
        #Pulldown menu, and add it to the menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=lambda:self.filedialogf())
        self.filemenu.add_command(label="Save",  command=lambda:print("test"))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        #More pulldown menus
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=lambda:print("test"))
        self.editmenu.add_command(label="Copy", command=lambda:print("test"))
        self.editmenu.add_command(label="Paste", command=lambda:print("test"))
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=lambda:print("test"))
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.parent.config(menu=self.menubar)

        #creates buttons and their frame, then place with function
        self.buttonframe = tk.Frame(self, bg="black", height=1920,width=100)
        self.mapselectbtn = tk.Button(self.buttonframe,text="Map Selection",command=lambda:self.fileopeningf("mapselect"),width=12,padx=10,pady=20,font=("arial",20))
        self.mapetbtn = tk.Button(self.buttonframe,text="Map Editor",command=lambda:self.fileopeningf("mapeditor"),width=12,padx=10,pady=20,font=("arial",20))
        self.settingsbtn = tk.Button(self.buttonframe,text="Settings",command=lambda:self.fileopeningf("settings"),width=12,padx=10,pady=20,font=("arial",20))
        self.programexitbtn = tk.Button(self.buttonframe, text="Quit", command=root.destroy,width=12,padx=10,pady=20, font=("arial",20))
        self.placeguif()

        
    # display the menu
    # Maybe use this instead
    # use winfo_rootx and winfo_rooty to get the coordinates relative to the screen. And yes, wm_geometry is the way to place a toplevel window precisely.
    def placeguif(self):
        self.buttonframe.place(x=10,y=10, anchor="c", relx=0.48, rely=0.5)
        self.mapselectbtn.grid(row=0,ipadx=10,ipady=10)
        self.mapetbtn.grid(row=1,ipadx=10,ipady=10)
        self.settingsbtn.grid(row=2,ipadx=10,ipady=10)
        self.programexitbtn.grid(row=3,ipadx=10,ipady=10)
    
    def fileopeningf(self,file):
        self.buttonframe.grid_forget()
        self.mapselectbtn.grid_forget()
        self.mapetbtn.grid_forget()
        self.settingsbtn.grid_forget()
        self.programexitbtn.grid_forget()    
        if file == "settings":
            self.settingsf()
        else:
            self.mapetlogo.place_forget()
            self.buttonframe.place_forget()
            if file == "mapselect":
                choosegui = choosemap.ChooseMap(self.parent, file)                
            elif file == "mapeditor":
               choosegui = choosemap.ChooseMap(self.parent, file)

    def settingbackf(self):
        self.fullscreenbtn.grid_forget()
        self.mapetbtn.grid_forget()
        self.settingsbtn.grid_forget()
        self.backbtn.grid_forget()
        self.placeguif()
        
    def settingsf(self):
        self.fullscreenbtn = tk.Button(self.buttonframe,text="Toggle Fullscreen",command=lambda:self.fullscreenf(),width=12,padx=10,pady=10, font=("arial",20))
        self.fullscreenbtn.grid(row=0,ipadx=10,ipady=10)
        self.mapetbtn = tk.Button(self.buttonframe,text="Map Editor",command=lambda:self.fileopeningf("mapeditor"),width=12,padx=10,pady=10, font=("arial",20))
        self.mapetbtn.grid(row=1,ipadx=10,ipady=10)
        self.settingsbtn = tk.Button(self.buttonframe,text="Settings",command=lambda:self.fileopeningf("settings"),width=12,padx=10,pady=10, font=("arial",20))
        self.settingsbtn.grid(row=2,ipadx=10,ipady=10)
        self.backbtn = tk.Button(self.buttonframe, text="Back", command=lambda:self.settingbackf(),width=12,padx=10,pady=10, font=("arial",20))
        self.backbtn.grid(row=3,ipadx=10,ipady=10)

    def fullscreenf(self):
        self.parent.attributes("-fullscreen", not self.parent.attributes('-fullscreen'))
    
    def filedialogf(self):
        self.filedialogpath = filedialog.askopenfilename()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

