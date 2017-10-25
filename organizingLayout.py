from tkinter import *
'''
from tkinter import *
root = Tk()
.
.
.
root.mainloop()

This is basic layout for any GUI application.
'''
root = Tk()

topFrame = Frame(root)
#Frame() is used to create a frame, a kind of invisible rectangle where we can put out widgets.

topFrame.pack()
#Anytime we want anything to be displayed, we need to pack() it.

bottomFrame = Frame(root)
#This is a bottom frame, another invisible container for widgets.

bottomFrame.pack(side = BOTTOM)
#side = BOTTOM is used to explicitly set the frame to BOTTOM end.

button1 = Button(topFrame,text = "SUBMIT", fg = "green")
#Creating a button with Button Object.

button2 = Button(topFrame,text = "DISPLAY", fg = "blue")

button3 = Button(bottomFrame,text = "RESET", fg = "red")

#To display the buttons, we need to pack() them.
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = BOTTOM)


root.mainloop()
