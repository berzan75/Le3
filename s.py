from tkinter import *

root=Tk()
root.geometry("150x200")

b=Label(text="berzan",
    font=50,fg="blue")

b.pack()

scrollbar= Scrollbar(root)

scrollbar.pack(side=RIGHT,
               fill=Y)

mylist=Listbox(root,yscrollcommand=scrollbar.set)

for i in range(1,35):
    mylist.insert(END,"hi"+str(i))

mylist.pack(side=LEFT,
            fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()
