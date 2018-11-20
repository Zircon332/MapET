import tkinter as tk
from tkinter import filedialog
import choosemap
import play
import mapet
import pickle

class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("MapET")
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+%d+%d" % (self.screen_width,self.screen_height,0,0))
        self.parent.attributes("-fullscreen", False)
        self.creategui()

    def creategui(self):    # Creates logo, menubar and buttons
        # MapET Logo Banner
        self.logoimg = tk.PhotoImage(file="images/logo.gif")
        self.mapetlogo =  tk.Label(self.parent, image=self.logoimg,anchor="c")
        self.mapetlogo.image = self.logoimg

        # Menu bar
        self.menubar = tk.Menu(self.parent)
        # 'File' Menu Bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=lambda:self.filedialog())
        self.filemenu.add_command(label="Save",  command=lambda:print("test"))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.buttonframe = tk.Frame(self, bg="black", height=1920,width=100)    # creates buttons and their frame, then place with function
        self.mapselectbtn = tk.Button(self.buttonframe,text="Play Map",
                                    command=lambda:self.fileopening("mapselect"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.mapetbtn = tk.Button(self.buttonframe,text="Map Editor",
                                    command=lambda:self.fileopening("mapeditor"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.settingsbtn = tk.Button(self.buttonframe,
                                    text="Settings",command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.programexitbtn = tk.Button(self.buttonframe, text="Quit",
                                     command=root.destroy,
                                     width=12,padx=10,pady=20, font=("calibri",20))
        self.placegui()

    def placegui(self):    # display main buttons
        self.mapetlogo.place(relx=.5, rely=.15, anchor="c")
        self.buttonframe.place(x=10,y=10, anchor="c", relx=0.48, rely=0.5)
        self.mapselectbtn.grid(row=0,ipadx=10,ipady=10)
        self.mapetbtn.grid(row=1,ipadx=10,ipady=10)
        self.settingsbtn.grid(row=2,ipadx=10,ipady=10)
        self.programexitbtn.grid(row=3,ipadx=10,ipady=10)

    
    def fileopening(self,file):    # #1-Hides Main buttons, #2-then display Settings buttons / #3-display Map Selection
        for child in self.buttonframe.winfo_children(): #1
            child.grid_forget()
        self.settingsbtn = tk.Button(self.buttonframe,
                                    text="Settings",    #2
                                    command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        if file == "settings":
            self.settings()
        else: #3
            self.mapetlogo.place_forget()
            self.buttonframe.place_forget()
            if file == "mapselect":
                self.backbuttonpage()
                self.cm = choosemap.ChooseMap(self.parent, file)
            elif file == "mapeditor":
                self.backbuttonpage()
                self.cm = choosemap.ChooseMap(self.parent, file)

    # Hides Settings buttons and display Main buttons
    def settingback(self):
        self.fullscreenbtn.grid_forget()
        self.backbtn.grid_forget()
        self.placegui()

    # display Settings button
    def settings(self):
        self.fullscreenbtn = tk.Button(self.buttonframe,text="Toggle Fullscreen",
                                    command=lambda:self.fullscreen(),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.fullscreenbtn.grid(row=0,ipadx=10,ipady=10)
        self.backbtn = tk.Button(self.buttonframe, text="Back",
                                    command=lambda:self.settingback(),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.backbtn.grid(row=3,ipadx=10,ipady=10)
    # Toggle Fullscreen
    def fullscreen(self):
        self.parent.attributes("-fullscreen", not self.parent.attributes('-fullscreen'))

    # Opens file dialog to choose a file
    def filedialog(self):
        self.filedialogpath = filedialog.askopenfilename()

    def backbuttonpage(self):
        self.backbtn = tk.Button(self.parent, text="Back", command=lambda:deleteall(),
                                width=12,padx=3,pady=3, font=("calibri",15))
        self.backbtn.place(anchor="nw", relx=0.02, rely=0.02)

        def deleteall():
            try:
                self.cm.mapall.destroy()
            except:
                pass

            try:
                self.cm.pl.screen.destroy()
                self.cm.pl.switch.destroy()
            except:
                pass

            try:
                self.cm.mp.mapeditframe.destroy()
            except:
                pass
            try:
                self.cm.mp.pl.screen.destroy()
                self.cm.mp.pl.switch.destroy()
            except:
                pass
            self.backbtn.destroy()
            self.placegui()

# Start the program
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
