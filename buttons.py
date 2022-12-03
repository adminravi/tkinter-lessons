from tkinter import *
# Creating a  Label Widget
root = Tk()

def myClick():
    myLabel = Label(root, text = "Deleted")
    myLabel.pack()

myButton = Button(root, text = "Delete", command = myClick, bg = "red", fg = "white", padx = 60, pady = 30)

# Put it on the screen
myButton.pack()


root.mainloop()