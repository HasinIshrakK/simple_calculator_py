from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.grid(row=0, column=0, columnspan=3)

def n(number):
    return

num1 = Button(root, text="1", padx=40, pady=20, command= lambda: n(1))
num2 = Button(root, text="2", padx=40, pady=20, command= lambda: n(2))
num3 = Button(root, text="3", padx=40, pady=20, command= lambda: n(3))
num4 = Button(root, text="4", padx=40, pady=20, command= lambda: n(4))
num5 = Button(root, text="5", padx=40, pady=20, command= lambda: n(5))
num6 = Button(root, text="6", padx=40, pady=20, command= lambda: n(6))
num7 = Button(root, text="7", padx=40, pady=20, command= lambda: n(7))
num8 = Button(root, text="8", padx=40, pady=20, command= lambda: n(8))
num9 = Button(root, text="9", padx=40, pady=20, command= lambda: n(9))
num0 = Button(root, text="0", padx=40, pady=20, command= lambda: n(0))
num_neg = Button(root, text="+/-", padx=34, pady=20, command= lambda: n())
num_dot = Button(root, text=".", padx=41, pady=20, command= lambda: n())

num_neg.grid(row=4, column=0)
num0.grid(row=4, column=1)
num_dot.grid(row=4, column=2)

num1.grid(row=3, column=0)
num2.grid(row=3, column=1)
num3.grid(row=3, column=2)

num4.grid(row=2, column=0)
num5.grid(row=2, column=1)
num6.grid(row=2, column=2)

num7.grid(row=1, column=0)
num8.grid(row=1, column=1)
num9.grid(row=1, column=2)

mainloop()