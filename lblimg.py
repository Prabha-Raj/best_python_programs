import tkinter
from tkinter import *
from PIL import ImageTk, Image
def click():
	img=Image.open("temp.png")
	test = ImageTk.PhotoImage(img)
	lbl2.config(image=test)
	lbl2.img=test

root=Tk()
root.geometry("800x800")
root.resizable(False,False)
lbl1=Frame(root,bg="red",height="800",width="400")
lbl1.place(x=0,y=0) 

btn=Button(root,bg="black" ,text="Click Me",fg="white",width="15",font="arial 10 bold",command=click)
btn.place(x=20,y=50)

lbl2=Label(root,bg="green",height="800",width="400")
lbl2.place(x=400,y=0) 

root.mainloop()