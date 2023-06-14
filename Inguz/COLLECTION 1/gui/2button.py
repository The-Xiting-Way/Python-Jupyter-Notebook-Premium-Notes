from tkinter import *

root = Tk()     

def myClick():              # this way we make a button do work
    var=Label(root,text='look! i clicked a button! ')
    var.pack()

x=Button(root, text='click me! ',padx=5,pady=5, command=myClick, fg='white',bg='black')  
# we use root as argument here to tell which window the widget needs to be on

# command helps recall a funct. NOTE-: domn't use () with fuunc in command 
# fg changes colour of the button 

x.pack()

root.mainloop()