import tkinter as tk
from tkinter import filedialog
import choosemap
import play
import mapet
import pickle

universalfont = ("calibri",20)

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

    def creategui(self):    # Creates logo, menubar and buttons
        # MapET Logo Banner
        self.logoimg = tk.PhotoImage(file="images/logo.gif")
        self.mapetlogo =  tk.Label(self.parent, image=self.logoimg,anchor = "c")
        self.mapetlogo.image = self.logoimg

        self.buttonframe = tk.Frame(self, bg="black", height=1920,width=100,)    # creates buttons and their frame, then place with function
        self.mapselectbtn = tk.Button(self.buttonframe,text="Play Map",
                                    command=lambda:self.fileopening("mapselect"),
                                    width=12,padx=10,pady=20,font=(universalfont))
        self.mapetbtn = tk.Button(self.buttonframe,text="Map Editor",
                                    command=lambda:self.fileopening("mapeditor"),
                                    width=12,padx=10,pady=20,font=(universalfont))
        self.settingsbtn = tk.Button(self.buttonframe,
                                    text="Settings",command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=(universalfont))
        self.tutorialbtn = tk.Button(self.buttonframe,
                                    text="Tutorial",command=lambda:print("test"),
                                    width=12,padx=10,pady=20,font=(universalfont))
        self.programexitbtn = tk.Button(self.buttonframe, text="Quit",
                                     command=root.destroy,
                                     width=12,padx=10,pady=20, font=(universalfont))
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
        self.settingsbtn = tk.Button(self.buttonframe,text="Settings",    #2
                                    command=lambda:self.fileopening("settings"),
                                    width=12,padx=10,pady=20,font=(universalfont))
        if file == "settings":
            self.fullscreenbtn = tk.Button(self.buttonframe,text="Toggle Fullscreen",
                                    command=lambda:self.parent.attributes("-fullscreen", not self.parent.attributes('-fullscreen')), #Toggles Fullscreen
                                    width=12,padx=10,pady=10, font=(universalfont))
            self.fullscreenbtn.grid(row=0,ipadx=10,ipady=10)
            self.backbtn = tk.Button(self.buttonframe, text="Back",
                                    command=lambda:self.settingback(),
                                    width=12,padx=10,pady=10, font=(universalfont))
            self.backbtn.grid(row=3,ipadx=10,ipady=10)

        else: #3
            self.mapetlogo.place_forget() #fix this
            self.buttonframe.place_forget()
            self.cm = choosemap.ChooseMap(self, file) #calls choosemap

    # Hides Settings buttons and display Main buttons
    def settingback(self):
        self.fullscreenbtn.grid_forget()
        self.backbtn.grid_forget()
        self.placegui()

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
