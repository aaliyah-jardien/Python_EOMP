
# coded by Uthmaan Breda.

from tkinter import *
import random

root = Tk()
root.geometry('450x500')
root.title('LOGIN')

# StringVar
result = StringVar()


Label(root, text='Name:').place(x=10, y=30)
user_ent = Entry(root)
user_ent.place(x=150, y=30)
user_ent.focus()
Label(root, text='Email:').place(x=10, y=80)
email_ent = Entry(root)
email_ent.place(x=150, y=80)
Label(root, text='ID Number:').place(x=10, y=130)
id_ent = Entry(root)
id_ent.place(x=150, y=130)
results = Label(root, text='', textvariable=result).place(x=150, y=230)


def login():
    f = open('details.txt', 'w')
    f.write(user_ent.get())
    f.write('\n')
    f.write(email_ent.get())
    f.write('\n')
    f.write(id_ent.get())

    # function to generate random numbers without repeating
    def gen_num():
        x = 0
        list_1 = []
        while x < 6:
            r = random.randint(1, 42)
            if r not in list_1:
                list_1.append(r)
                x = x + 1
        else:  # the reason for adding the else statement is coz when it runs the 6th time and the number is the same,
            x = x - 1  # it just prints 5 numbers
        list_1.sort()
        f.write(str(list_1))


def kill():
    root.destroy()


def clear():
    user_ent.delete(0, END)
    email_ent.delete(0, END)
    id_ent.delete(0, END)
    result.set('')


Button(root, text='Login', command=login).place(x=150, y=180)
Button(root, text='Exit', command=kill).place(x=130, y=280)
Button(root, text='Clear', command=clear).place(x=230, y=280)

root.mainloop()


# show='\u2022'
