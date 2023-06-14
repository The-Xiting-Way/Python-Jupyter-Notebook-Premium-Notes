from tkinter import *

root = Tk()

e = Entry(root,width='55',borderwidth='5') 
e.grid(row=0,column=0,columnspan=3,padx=20,pady=15)
e.insert(0,1)
def x(number):
    a=e.get()
    # e.delete(0,END)
    e.insert(0,str(a)+str(number))

xi = Button(root,text='2',padx=40,pady=20,command=lambda: x(2))
xi.grid(row=1,column=0)

root.mainloop()
