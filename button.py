from tkinter import *
from tkinter import messagebox

top = Tk()

def helloCallBack():
   messagebox.showinfo("Say Hello", "Hello World")

B = Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()