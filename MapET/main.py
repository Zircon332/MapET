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
        print(self.parent)
        self.parent.title("MapET")
        self.screen_width = self.parent.winfo_screenwidth()
        self.screen_height = self.parent.winfo_screenheight()
        self.parent.geometry("%dx%d+%d+%d" % (self.screen_width,self.screen_height,0,0))
        self.parent.attributes("-fullscreen", False)
        self.creategui()

        self.movekey = 0    # initialise move key to decide which set of keys to use

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

        self.buttonframe = tk.Frame(self, bg="black", height=1920,width=100,)    # creates buttons and their frame, then place with function
        self.mapselectbtn = tk.Button(self.buttonframe,text="Play Map",
                                    command=lambda:self.fileopening("mapselect"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.mapetbtn = tk.Button(self.buttonframe,text="Map Editor",
                                    command=lambda:self.fileopening("mapeditor"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.settingsbtn = tk.Button(self.buttonframe,
                                    text="Settings",command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.tutorialbtn = tk.Button(self.buttonframe,
                                    text="Tutorial",command=lambda:self.tutorial(),
                                    width=12,padx=10,pady=20,font=("calibri",20))
        self.programexitbtn = tk.Button(self.buttonframe, text="Quit",
                                     command=root.destroy,
                                     width=12,padx=10,pady=20, font=("calibri",20))
        self.placegui()
    
    # def tutorial(self):
    #     self.buttonframe.forget()
    #     self.mapetlogo.forget()
    #     self.img = tk.PhotoImage(file="images/tutorial.gif")
    #     self.tutorialpanel = tk.Label(self.parent, image = self.img, anchor="c")
    #     self.tutorialpanel.place(relx=.5,rely=.5, anchor="c")
    #     self.backbuttonpage()

    def placegui(self):    # display main buttons
        self.mapetlogo.place(relx=.5, rely=.15, anchor="c")
        self.buttonframe.place(x=10,y=10, anchor="c", relx=0.48, rely=0.5)
        self.mapselectbtn.grid(row=0,ipadx=10,ipady=10)
        self.mapetbtn.grid(row=1,ipadx=10,ipady=10)
        self.settingsbtn.grid(row=2,ipadx=10,ipady=10)
        self.tutorialbtn.grid(row=3,ipadx=10,ipady=10)
        self.programexitbtn.grid(row=4,ipadx=10,ipady=10)

    
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
            self.cm = choosemap.ChooseMap(self, file, self.movekey) #calls choosemap

    # Hides Settings buttons and display Main buttons
    def settingback(self):
        self.fullscreenbtn.grid_forget()
        self.movecontrols.grid_forget()
        self.backbtn.grid_forget()
        self.placegui()

    def changecontrol(self):
        if self.movekey == 0:
            self.movecontrols.config(text="Move controls\n(W A S D)")
            self.movekey = 1
        elif self.movekey == 1:
            self.movecontrols.config(text="Move controls\n(↑W ↓S ←A →D)")
            self.movekey = 2
        elif self.movekey == 2:
            self.movecontrols.config(text="Move controls\n(↑ ↓ ← →)")
            self.movekey = 0
            
    # display Settings button
    def settings(self):
        self.fullscreenbtn = tk.Button(self.buttonframe,text="Toggle Fullscreen",
                                    command=self.parent.attributes("-fullscreen", not self.parent.attributes('-fullscreen')),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.fullscreenbtn.grid(row=0,ipadx=10,ipady=10,columnspan=2)
        self.movecontrols =  tk.Button(self.buttonframe,text="Move controls\n(↑ ↓ ← →)",
                                    command=lambda:self.changecontrol(),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.movecontrols.grid(row=1,ipadx=10,ipady=10,column=0)
        self.backbtn = tk.Button(self.buttonframe, text="Back",
                                    command=lambda:self.settingback(),
                                    width=12,padx=10,pady=10, font=("calibri",20))
        self.backbtn.grid(row=3,ipadx=10,ipady=10,columnspan=2)

    def backbuttonpage(self,frame):
        self.backbtn = tk.Button(self.parent, text="Back", command=lambda:deleteall(frame),
                                width=12,padx=3,pady=3, font=("calibri",15))
        self.backbtn.place(anchor="nw", relx=0.02, rely=0.02)
        def deleteall(frame):
            frame.destroy()
            self.backbtn.destroy()
            self.placegui()

# Start the program
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
