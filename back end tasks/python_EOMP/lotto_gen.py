from tkinter import *
from tkinter import ttk
import random

root = Tk()

root.geometry('450x500')
root.title('LOTTO!!!')


class Loot:
    results = StringVar()

    def __init__(self, master):
        # labels and displays
        self.num_lab = Label(root, text='Lucky Numbers:').place(x=50, y=200)
        self.num_res = Label(root, text='', textvariable=self.results).place(x=200, y=200)



        # buttons
        self.gen_btn = Button(root, text='Generate', command=self.gen_num).place(x=200, y=250)
        self.clr_btn = Button(root, text='Clear', command=self.clear).place(x=230, y=300)
        self.exit = Button(root, text='Exit', command=self.kill).place(x=130, y=300)

    def gen_num(self):
        x = 0
        list_1 = []
        while x < 6:
            r = random.randint(1, 51)
            if r not in list_1:
                list_1.append(r)
                x = x + 1
        else:  # the reason for adding the else statement is coz when it runs the 6th time and the number is the same,
            x = x - 1  # it just prints 5 numbers
        list_1.sort()
        self.results.set(list_1)

    def kill(self):
        root.destroy()

    def clear(self):
        self.results.set('')


a = Loot(root)
root.mainloop()
