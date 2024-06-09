#Frame

from tkinter import *
root=Tk()
root.geometry("500x400")
frame1=Frame(root,bg="yellow",height="400",width="250")
frame1.place(x=0,y=0)
lbl1=Label(root,font=("Arial 10 bold"),width="10",text="Frame",fg="red")
lbl1.place(x=0,y=0)

root.mainloop()