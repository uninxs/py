from tkinter import*
from tkinter import messagebox
top=Tk()
def helloCallBack():
    messagebox.showinfo("Hello Python","Hello World")
B=Button(top,text="hello",command=helloCallBack)
B.pack()
top.mainloop()
