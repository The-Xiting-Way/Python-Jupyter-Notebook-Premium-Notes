from tkinter import *

root = Tk()
root.title('Welcome to the end of matrix')
root.iconbitmap(r"C:\Users\aryan\Downloads\6avRYXESjCnOlJCZAu2d_w8aJSGO5syVmd13N.ico")

root.geometry('900x600')

aframe = Frame(root, width=600, height=400)
alabel = Label(aframe, image =r"C:\Users\aryan\Downloads\the-matrix-wallpaper-preview.png")

aframe.grid(row=0,column=1)

x1 = Button(root,text='move',padx=39,pady=20)
x1.grid(row=1,column=1)
x2 = Button(root,text='move',padx=39,pady=20)
x1.grid(row=1,column=1)

root.mainloop()
