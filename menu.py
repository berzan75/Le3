from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("menu bar")

menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)
file.add_command(label="File",command=None)
file.add_command(label="New File",command=None)
file.add_command(label="Open",command=None)
file.add_separator()
file.add_command(label="Exit",command=root.destroy)

edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo",command=None)
edit.add_command(label="Redo",command=None)
edit.add_separator()
edit.add_command(label="Cut",command=None)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)


help=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help)
root.config(menu=menubar)
help.add_command(label="Welcome",command=None)
help.add_command(label="Show All Commands",command=None)
help.add_separator()
help.add_command(label="Documentation",command=None)

root.mainloop()
