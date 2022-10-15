from tkinter import *
def select():
    selection="current Value= "+str(var.get())
    lbl.config(text=selection)
top=Tk()
var=DoubleVar()
myscale=Scale(top,variable=var)
myscale.pack(anchor=CENTER)
b1=Button(top,text="Click to get scale value",command=select)
b1.pack(anchor=CENTER)
lbl=Label(top)
lbl.pack()
top.mainloop()
