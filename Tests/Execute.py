import tkinter as tk

def run():
    try:
        script = entry1.get() +"\n"+ entry2.get() +"\n"+ entry3.get() +"\n"+ entry4.get() +"\n"+ entry5.get() +"\n"+ entry6.get()
        exec(script)
    except:
        print("Error")
        
#Main app thing
root = tk.Tk()
root.title("Scripter")
root.geometry("1500x1000")
root.config(bg="dark grey")
#frame
frame_entry = tk.Frame(root,borderwidth=1)
frame_button = tk.Frame(root)
frame_playground = tk.Frame(root,height=600,width=1200,bg="white",borderwidth=1)
frame_info = tk.Frame(root,height=600,width=200,bg="dark grey")
frame_entry.grid(row=1,column=0,padx=5,pady=5)
frame_button.grid(row=1,column=1,padx=5,pady=5)
frame_playground.grid(row=0,column=0,padx=5,pady=5)
frame_info.grid(row=0,column=1,padx=5,pady=5)

#buttons
button1 = tk.Button(frame_button,text="Run",command=lambda:run(),width=10)

#entries
entry1 = tk.Entry(frame_entry,width=200)
entry2 = tk.Entry(frame_entry,width=200)
entry3 = tk.Entry(frame_entry,width=200)
entry4 = tk.Entry(frame_entry,width=200)
entry5 = tk.Entry(frame_entry,width=200)
entry6 = tk.Entry(frame_entry,width=200)

#placing buttons
button1.grid(row=0,column=0)

#placing entries
entry1.grid(row=0,column=0)
entry2.grid(row=1,column=0)
entry3.grid(row=2,column=0)
entry4.grid(row=3,column=0)
entry5.grid(row=4,column=0)
entry6.grid(row=5,column=0)

#the end
root.mainloop()
