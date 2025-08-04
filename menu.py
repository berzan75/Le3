from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("menu bar")

menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)


edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)


help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
root.config(menu=menubar)
root.mainloop()