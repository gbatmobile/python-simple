from tkinter import *


def showMsg():
        global nclicks
        nclicks = nclicks + 1
        lbl['text'] = str(nclicks)

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=showMsg)
btn.grid(column=1, row=0)

nclicks = 0

window.mainloop()