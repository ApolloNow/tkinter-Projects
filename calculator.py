from tkinter import *
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from typing import Match
root = Tk()
root['bg'] = 'red'
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, pady=10)
#e.insert(0, "")

def func_button_click(number):
    current = e.get()
    e.delete(0, END)    
    e.insert(0, str(current)+str(number))
def func_button_clear():
    e.delete(0, END)
def func_button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)

    e.delete(0, END)

def func_button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    e.delete(0, END)

def func_button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    e.delete(0, END)

def func_button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0, END)

def func_button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        num = float(f_num) + float(second_number)
        if int(num) == num:
            num = int(num)
        e.insert(0, num)
    elif math == 'subtraction':
        num = float(f_num) - float(second_number)
        if int(num) == num:
            num = int(num)
        e.insert(0, num)
    elif math == 'multiplication':
        num = float(f_num) * float(second_number)
        if int(num) == num:
            num = int(num)
        e.insert(0, num)
    elif math == 'division':
        num = float(f_num) / float(second_number)
        if int(num) == num:
            num = int(num)
        e.insert(0, num)
    


    

#define the buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: func_button_click(1), bg='black', fg='white')
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: func_button_click(2), bg='black', fg='white')
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: func_button_click(3), bg='black', fg='white')
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: func_button_click(4), bg='black', fg='white')
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: func_button_click(5), bg='black', fg='white')
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: func_button_click(6), bg='black', fg='white')
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: func_button_click(7), bg='black', fg='white')
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: func_button_click(8), bg='black', fg='white')
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: func_button_click(9), bg='black', fg='white')
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: func_button_click(0), bg='black', fg='white')
button_add = Button(root, text="+", padx=39, pady=20, command=func_button_add, bg='black', fg='white')
button_subtract = Button(root, text="-", padx=41, pady=20, command=func_button_subtract, bg='black', fg='white')
button_multiply = Button(root, text="*", padx=41, pady=20, command=func_button_multiply, bg='black', fg='white')
button_divide = Button(root, text="/", padx=41, pady=20, command=func_button_divide, bg='black', fg='white')

button_equal = Button(root, text="=", padx=39, pady=20, command=func_button_equal, bg='green', fg='white')
button_clear = Button(root, text="Clear", padx=85, pady=20, command=func_button_clear, bg='green', fg='white')

button_decimal = Button(root, text='.', padx=43, pady=23, command=lambda: func_button_click('.'), bg='black', fg='white')


# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=6, column=1, columnspan=2)
button_add.grid(row=5, column=1)
button_equal.grid(row=6, column=0)
button_decimal.grid(row=5, column=0)

button_subtract.grid(row=5, column=2)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)








root.mainloop()
