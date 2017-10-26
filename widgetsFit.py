from tkinter import  *

root = Tk()
root.title(string = "Widgets")

one = Label(root,text = "Welcome", bg = "cyan", fg = "red")
one.pack()

two = Label(root, text = "You're inside Tkinter", bg = "grey", fg = "blue")
two.pack(fill = X)
#fill = X will fill the label to full X axis.

three = Label(root, text = "Left Widget", bg = "yellow", fg = "green")
three.pack(side = LEFT, fill = Y)

root.mainloop()