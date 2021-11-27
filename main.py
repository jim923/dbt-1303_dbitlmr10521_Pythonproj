from tkinter import *
import datetime
from tkinter.messagebox import *
from tkinter.ttk import *
import pywhatkit  as kit

obj = Tk()
obj.geometry("400x400")


def alarm():
    if c1.get() == "AM":
        x = int(e1.get())
        y = int(e2.get())
    if c1.get() == "PM":
        x = int(e1.get()) + 12
        y = int(e2.get())
    showinfo("notification", "alarm has been set")
    while True:
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
            for i in range(0, 1):
                kit.playonyt("https://www.youtube.com/watch?v=KnJ0d63Fi0c")
            break


l1 = Label(obj, text="HOURS:")
l2 = Label(obj, text="MINUTES:")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1 = Entry(obj)
e2 = Entry(obj)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b1 = Button(obj, text="SET ALARM", command=alarm)
b1.grid(row=2, column=1)
c1 = Combobox(obj, values=["AM", "PM"])
c1.grid(row=0, column=2)
l3 = Label(obj, text="AM OR PM")
l3.grid(row=0, column=3)
obj.mainloop()
