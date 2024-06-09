from tkinter import *

root=Tk()
root.geometry("500x400+300+50")
root.resizable(False,False)
bg=PhotoImage(file="tkbg.png")
lbl=Label(root,image=bg)
lbl.place(x=0,y=0)


root.mainloop() 