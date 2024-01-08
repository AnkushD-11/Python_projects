# SIMPLE CALCULATOR

from tkinter import *
import tkinter as tk
import tkinter.messagebox

guiWindow = tk.Tk()
guiWindow.geometry("400x400+500+300")  
guiWindow.title('Calculator-Ankush')
Calc = tk.Frame(master=guiWindow, bg="BlanchedAlmond", padx=6)
Calc.pack()
entry = tk.Entry(master=Calc, borderwidth=5, width=60)
entry.grid(row=0, column=0, columnspan=3, ipady=3, pady=3)

def clk(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)
    
#numeric buttons

button1 = tk.Button(master=Calc, text='1', padx=20, pady=5, width=10, command=lambda: clk(1))
button1.grid(row=1, column=0, pady=2)
button2 = tk.Button(master=Calc, text='2', padx=20, pady=5, width=10, command=lambda: clk(2))
button2.grid(row=1, column=1, pady=2)
button3 = tk.Button(master=Calc, text='3', padx=20, pady=5, width=10, command=lambda: clk(3))
button3.grid(row=1, column=2, pady=2)
button4 = tk.Button(master=Calc, text='4', padx=20, pady=5, width=10, command=lambda: clk(4))
button4.grid(row=2, column=0, pady=2)
button5 = tk.Button(master=Calc, text='5', padx=20, pady=5, width=10, command=lambda: clk(5))
button5.grid(row=2, column=1, pady=2)
button6 = tk.Button(master=Calc, text='6', padx=20, pady=5, width=10, command=lambda: clk(6))
button6.grid(row=2, column=2, pady=2)
button7 = tk.Button(master= Calc, text='7', padx=20, pady=5, width=10, command=lambda: clk(7))
button7.grid(row=3, column=0, pady=2)
button8 = tk.Button(master=Calc, text='8', padx=20, pady=5, width=10, command=lambda: clk(8))
button8.grid(row=3, column=1, pady=2)
button9 = tk.Button(master= Calc, text='9', padx=20, pady=5, width=10, command=lambda: clk(9))
button9.grid(row=3, column=2, pady=2)
button0 = tk.Button(master= Calc, text='0', padx=20, pady=5, width=10, command=lambda: clk(0))
button0.grid(row=4, column=1, pady=2)

#Functional buttons

add_but = tk.Button(master= Calc, text="+", padx=20, pady=5, width=10, command=lambda: clk('+'))
add_but.grid(row=5, column=0, pady=2)
 
subtract_but= tk.Button(master= Calc, text="-", padx=15, pady=5, width=10, command=lambda: clk('-'))
subtract_but.grid(row=5, column=1, pady=2)
 
multiply_but= tk.Button( master= Calc, text="*", padx=8, pady=5, width=10, command=lambda: clk('*'))
multiply_but.grid(row=5, column=2, pady=2)
 
divison_but= tk.Button(master=Calc, text="/", padx=15, pady=5, width=10, command=lambda: clk('/'))
divison_but.grid(row=6, column=0, pady=2)
 
clr_but = tk.Button(master=Calc, text="clear", padx=5, pady=5, width=10, command=clear)
clr_but.grid(row=6, column=2, columnspan=2, pady=2)
 
equalbut = tk.Button(master=Calc, text="=", padx=15, pady=5, width=10, command= equal)
equalbut.grid(row=6, column=0, columnspan=3, pady=2)

expobut = tk.Button(master=Calc, text="^", padx=15, pady = 5, width= 10, command = lambda: clk('**'))
expobut.grid(row = 4, column= 0, columnspan = 1 , pady=2)

point = tk.Button(master= Calc, text = ".", padx = 15, pady =5, width = 10, command = lambda: clk("."))
point.grid(row = 4, column = 2, padx = 1, pady = 2)

guiWindow.mainloop()
