from tkinter import *

root = Tk()


var1=Label(root, text='hello world!')
var2=Label(root, text='iam aryainguz')
var3=Label(root, text='')

# var1.pack()    # we can use grid or pack , we prefer using grid(rows,coloumns) instead of pack (gives output as it is written)
var1.grid(row=0,column=0)
var2.grid(row=1,column=0)
var3.grid(row=2,column=0)

root.mainloop()
