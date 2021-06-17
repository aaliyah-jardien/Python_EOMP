from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()

root.geometry('450x500')
root.title('LOTTO!!!')


class Loot:
    results = StringVar()
    list1var = StringVar()
    list2var = StringVar()
    list3var = StringVar()

    # lists for lotto guesses
    list1 = []
    list2 = []
    list3 = []

    def __init__(self, master):
        # labels and displays
        self.num_lab = Label(master, text='Lucky Numbers:').place(x=50, y=200)
        self.num_res = Label(master, text='', textvariable=self.results).place(x=200, y=200)
        self.list1_lab = Label(master, text='', textvariable=self.list1var).place(x=200, y=350)
        self.list2_lab = Label(master, text='', textvariable=self.list2var).place(x=200, y=400)
        self.list3_lab = Label(master, text='', textvariable=self.list3var).place(x=200, y=450)

        # lotto buttons
        self.num1 = Button(master, text='1', width=1, command=lambda: self.lottery(1)).place(x=10, y=10)
        self.num2 = Button(master, text='2', width=1, command=lambda: self.lottery(2)).place(x=50, y=10)
        self.num3 = Button(master, text='3', width=1, command=lambda: self.lottery(3)).place(x=90, y=10)
        self.num4 = Button(master, text='4', width=1, command=lambda: self.lottery(4)).place(x=130, y=10)
        self.num5 = Button(master, text='5', width=1, command=lambda: self.lottery(5)).place(x=170, y=10)
        self.num6 = Button(master, text='6', width=1, command=lambda: self.lottery(6)).place(x=210, y=10)
        self.num7 = Button(master, text='7', width=1, command=lambda: self.lottery(7)).place(x=250, y=10)
        self.num8 = Button(master, text='8', width=1, command=lambda: self.lottery(8)).place(x=290, y=10)
        self.num9 = Button(master, text='9', width=1, command=lambda: self.lottery(9)).place(x=330, y=10)
        self.num10 = Button(master, text='10', width=1, command=lambda: self.lottery(10)).place(x=370, y=10)
        self.num11 = Button(master, text='11', width=1, command=lambda: self.lottery(11)).place(x=410, y=10)
        self.num12 = Button(master, text='12', width=1, command=lambda: self.lottery(12)).place(x=10, y=50)
        self.num13 = Button(master, text='13', width=1, command=lambda: self.lottery(13)).place(x=50, y=50)
        self.num14 = Button(master, text='14', width=1, command=lambda: self.lottery(14)).place(x=90, y=50)
        self.num15 = Button(master, text='15', width=1, command=lambda: self.lottery(15)).place(x=130, y=50)
        self.num16 = Button(master, text='16', width=1, command=lambda: self.lottery(16)).place(x=170, y=50)
        self.num17 = Button(master, text='17', width=1, command=lambda: self.lottery(17)).place(x=210, y=50)
        self.num18 = Button(master, text='18', width=1, command=lambda: self.lottery(18)).place(x=250, y=50)
        self.num19 = Button(master, text='19', width=1, command=lambda: self.lottery(19)).place(x=290, y=50)
        self.num20 = Button(master, text='20', width=1, command=lambda: self.lottery(20)).place(x=330, y=50)
        self.num21 = Button(master, text='21', width=1, command=lambda: self.lottery(21)).place(x=370, y=50)
        self.num22 = Button(master, text='22', width=1, command=lambda: self.lottery(22)).place(x=410, y=50)
        self.num23 = Button(master, text='23', width=1, command=lambda: self.lottery(23)).place(x=10, y=90)
        self.num24 = Button(master, text='24', width=1, command=lambda: self.lottery(24)).place(x=50, y=90)
        self.num25 = Button(master, text='25', width=1, command=lambda: self.lottery(25)).place(x=90, y=90)
        self.num26 = Button(master, text='26', width=1, command=lambda: self.lottery(26)).place(x=130, y=90)
        self.num27 = Button(master, text='27', width=1, command=lambda: self.lottery(27)).place(x=170, y=90)
        self.num28 = Button(master, text='28', width=1, command=lambda: self.lottery(28)).place(x=210, y=90)
        self.num29 = Button(master, text='29', width=1, command=lambda: self.lottery(29)).place(x=250, y=90)
        self.num30 = Button(master, text='30', width=1, command=lambda: self.lottery(30)).place(x=290, y=90)
        self.num31 = Button(master, text='31', width=1, command=lambda: self.lottery(31)).place(x=330, y=90)
        self.num32 = Button(master, text='32', width=1, command=lambda: self.lottery(32)).place(x=370, y=90)
        self.num33 = Button(master, text='33', width=1, command=lambda: self.lottery(33)).place(x=410, y=90)
        self.num34 = Button(master, text='34', width=1, command=lambda: self.lottery(34)).place(x=10, y=130)
        self.num35 = Button(master, text='35', width=1, command=lambda: self.lottery(35)).place(x=50, y=130)
        self.num36 = Button(master, text='36', width=1, command=lambda: self.lottery(36)).place(x=90, y=130)
        self.num37 = Button(master, text='37', width=1, command=lambda: self.lottery(37)).place(x=130, y=130)
        self.num38 = Button(master, text='38', width=1, command=lambda: self.lottery(38)).place(x=170, y=130)
        self.num39 = Button(master, text='39', width=1, command=lambda: self.lottery(39)).place(x=210, y=130)
        self.num40 = Button(master, text='40', width=1, command=lambda: self.lottery(40)).place(x=250, y=130)
        self.num41 = Button(master, text='41', width=1, command=lambda: self.lottery(41)).place(x=290, y=130)
        self.num42 = Button(master, text='42', width=1, command=lambda: self.lottery(42)).place(x=330, y=130)
        self.num43 = Button(master, text='43', width=1, command=lambda: self.lottery(43)).place(x=370, y=130)
        self.num44 = Button(master, text='44', width=1, command=lambda: self.lottery(44)).place(x=410, y=130)
        self.num45 = Button(master, text='45', width=1, command=lambda: self.lottery(45)).place(x=10, y=170)
        self.num46 = Button(master, text='46', width=1, command=lambda: self.lottery(46)).place(x=50, y=170)
        self.num47 = Button(master, text='47', width=1, command=lambda: self.lottery(47)).place(x=90, y=170)
        self.num48 = Button(master, text='48', width=1, command=lambda: self.lottery(48)).place(x=130, y=170)
        self.num49 = Button(master, text='49', width=1, command=lambda: self.lottery(49)).place(x=170, y=170)

        # buttons
        self.gen_btn = Button(root, text='Generate', command=self.gen_num).place(x=200, y=250)
        self.clr_btn = Button(root, text='Clear', command=self.clear).place(x=230, y=300)
        self.exit = Button(root, text='Exit', command=self.kill).place(x=130, y=300)
        self.prize = Button(root, text='prize', command=self.lotto_draw1).place(x=130, y=400)

    def gen_num(self):
        x = 0
        list_1 = []
        while x < 6:
            r = random.randint(1, 49)
            if r not in list_1:
                list_1.append(r)
                x = x + 1
        else:  # the reason for adding the else statement is coz when it runs the 6th time and the number is the same,
            x = x - 1  # it just prints 5 numbers
        list_1.sort()
        self.results.set(list_1)

    def lottery(self, num):
        if len(self.list1) < 6 and num not in self.list1:
            self.list1.append(num)
            self.list1var.set(self.list1)

        elif len(self.list1) == 6 and len(self.list2) < 6 and num not in self.list2:
            self.list2.append(num)
            self.list2var.set(self.list2)

        elif len(self.list2) == 6 and len(self.list3) < 6 and num not in self.list3:
            self.list3.append(num)
            self.list3var.set(self.list3)

    def lotto_draw1(self):
        global win
        y = 0
        list_1 = []
        while y < 6:
            r = random.randint(1, 49)
            if r not in list_1:
                list_1.append(r)
                x = y + 1
        else:  # the reason for adding the else statement is coz when it runs the 6th time and the number is the same,
            x = y - 1  # it just prints 5 numbers
        list_1.sort()
        self.results.set(list_1)
        if self.list1[x] == list_1[x]:
            y += 1
        if y == 6:
            win = 10000000
        elif y == 5:
            win = 8584
        elif y == 4:
            win = 2384
        elif y == 3:
            win = 100.50
        elif y == 2:
            win = 20
        elif y < 2:
            win = 0
        messagebox.showinfo("Status", "Set had: " + str(y))
        messagebox.showinfo("Lotto", "Numbers are: " + str(list_1))
        messagebox.showinfo("Winnings", "You have won R" + str(win))

    def kill(self):
        root.destroy()

    def clear(self):
        self.results.set('')


a = Loot(root)
root.mainloop()
