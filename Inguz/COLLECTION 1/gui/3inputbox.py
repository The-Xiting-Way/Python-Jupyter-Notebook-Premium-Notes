from tkinter import *

root = Tk()
root.title('Aryainguz')   # this is for title

e = Entry(root,width=30,fg='blue',bg='yellow',borderwidth='5')   # we enter root to tell we want the widget/button on GUI wingow
e.pack()
e.insert(0, 'enter your name: ')

def myClick():
    hello='hello ' + e.get()               # get() stores or gets whatever entered preivously
                                           # this way we make a button do work
    var=Label(root,text=hello )
    var.pack()

x=Button(root, text='enter your name',padx=5,pady=5, command=myClick, fg='white',bg='black')  

# command helps recall a funct. NOTE-: domn't use () with fuunc in command 
# fg changes colour of the button 

x.pack()

root.mainloop()