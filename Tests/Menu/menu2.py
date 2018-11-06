import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_gui()

    def create_gui(self):
        mapselect = tk.Button(self,text="Map Selection",command=lambda:fileopening("mapselect"),width=12)
        mapselect.place(x=350,y=200)
        mapet = tk.Button(self,text="Map Editor",command=lambda:fileopening("mapeditor"),width=12)
        mapet.place(x=350,y=230)
        settings = tk.Button(self,text="Settings",command=lambda:fileopening("settings"),width=12)
        settings.place(x=350,y=260)
        programexit = tk.Button(self, text="Quit", command=root.destroy,width=12)
        programexit.place(x=350,y=290)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
