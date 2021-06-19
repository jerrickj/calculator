from tkinter import *
import tkinter.font as font
import math

#Master window definitions
root = Tk()
root.title("Jerrick's Calculator")
root.geometry("320x550")
root.configure(bg = "gray26",)
root.iconbitmap("calculator_logo.ico")

#configure rows and columns for dynamic resizing of buttons in window
Grid.columnconfigure(root, 0, weight = 1)
Grid.columnconfigure(root, 1, weight = 1)
Grid.columnconfigure(root, 2, weight = 1)
Grid.columnconfigure(root, 3, weight = 1)
Grid.rowconfigure(root, 0, weight = 5)
Grid.rowconfigure(root, 1, weight = 0)
Grid.rowconfigure(root, 2, weight = 1)
Grid.rowconfigure(root, 3, weight = 1)
Grid.rowconfigure(root, 4, weight = 1)
Grid.rowconfigure(root, 5, weight = 1)
Grid.rowconfigure(root, 6, weight = 1)

#defines font variable for resizing
myFont = font.Font(size=25, name="arial", weight = "bold")
myFont_small = font.Font(size=15)

#Variables for adjusting button padding
pad_x = 1
pad_y = 1

#variables for adjustable button borders
bd = 0
bdw = 1

#global variables
input_1 = 0
input_2 = 0
input_symbol = ""
memory = []

#functions that add clicked entries to output field
def button_click(number):
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + str(number))

def decimal():
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + ".")

#Functions for math
def clear_entry():
    output["state"] = NORMAL
    output.delete(0, END)

def clear():
    global input_1
    global input_2
    global input_symbol

    output["state"] = NORMAL
    output.delete(0, END)
    input_1 = 0
    input_2 = 0
    input_symbol = ""

def add():
    global input_1
    global input_2
    global input_symbol
    if input_1 != 0:
        equals()
        input_symbol = "+"
    else:
        input_1 = output.get()
        output.delete(0, END)
        input_symbol = "+"
        input_2 = 0

def subtract():
    global input_1
    global input_2
    global input_symbol
    if input_1 != 0:
        equals()
        input_symbol = "-"
    else:
        input_1 = output.get()
        output.delete(0, END)
        input_symbol = "-"
        input_2 = 0

def multiply():
    global input_1
    global input_2
    global input_symbol
    if input_1 != 0:
        equals()
        input_symbol = "*"
    else:
        input_1 = output.get()
        output.delete(0, END)
        input_symbol = "*"
        input_2 = 0

def divide():
    global input_1
    global input_2
    global input_symbol
    if input_1 != 0:
        equals()
        input_symbol = "/"
    else:
        input_1 = output.get()
        output.delete(0, END)
        input_symbol = "/"
        input_2 = 0

def equals():
    global input_1
    global input_2
    global input_symbol
    input_2 = output.get()
    output.delete(0, END)
    if input_symbol == "+":
        output.insert(0, float(input_1) + float(input_2))
    elif input_symbol == "-":
        output.insert(0, float(input_1) - float(input_2))
    elif input_symbol == "*":
        output.insert(0, float(input_1) * float(input_2))
    elif input_symbol == "/":
        if input_2 == 0 or input_2 == "0":
            output.insert(0, "Error, divide by 0")
            output["state"] = DISABLED
        else:
            output.insert(0, float(input_1) / float(input_2))  

def negative():
    current = float(output.get())
    output.delete(0, END)
    output.insert(0, -current)

def backspace():
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current[0:-1]))

def squared():
    current = output.get()
    output.delete(0, END)
    output.insert(0, float(current) * float(current))

def percentage():
    input_2 = output.get()
    output.delete(0, END)
    value = float(input_1) * float(input_2) / 100
    if input_symbol == "+":
        output.insert(0, float(input_1) + value)
    elif input_symbol == "-":
        output.insert(0, float(input_1) - value)
    elif input_symbol == "*":
        output.insert(0, float(input_1) * value)
    elif input_symbol == "/":
        output.insert(0, float(input_1) / value)

def sq_root():
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(math.sqrt(float(current))))

def inversed():
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(1/float(current)))

#define menubar
menubar = Menu(root, bg = "gray16", fg = "blue")

#outermost layer of options
file = Menu(menubar, tearoff=False, background = "gray80")
history = Menu(menubar, tearoff=False, background = "gray80")

#adds submenu's
file.add_command(label="New", command = clear)
file.add_command(label="Exit", command= root.quit)
history.add_command(label="View")
history.add_command(label="Clear")

# Display the file and edit declared in previous step
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="History", menu=history)

root.configure(menu = menubar)

#Text field for entering numbers, also displays selected numbers
output = Entry(root, width = 50, borderwidth = bdw, border = bd, bg = "gray26", fg = "White", justify = RIGHT, font = myFont)
output.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10, sticky=NSEW)

#define number buttons
button_1 =    Button(root, text = "1",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(1))
button_2 =    Button(root, text = "2",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(2))
button_3 =    Button(root, text = "3",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(3))
button_4 =    Button(root, text = "4",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(4))
button_5 =    Button(root, text = "5",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(5))
button_6 =    Button(root, text = "6",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(6))
button_7 =    Button(root, text = "7",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(7))
button_8 =    Button(root, text = "8",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(8))
button_9 =    Button(root, text = "9",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(9))
button_0 =    Button(root, text = "0",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White", command = lambda: button_click(0))

#define math symbol buttons
button_add =         Button(root, text = "+",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = add)
button_subtract =    Button(root, text = "-",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = subtract)
button_multiply =    Button(root, text = "×",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = multiply)
button_divide =      Button(root, text = "÷",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = divide)
   #clear_e clears all memory and everything, while clear just deletes current output window
button_clear_e =     Button(root, text = "CE",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "OrangeRed",    bg = "gray15",      fg = "White", command = clear_entry)
button_clear =       Button(root, text = "C",    borderwidth= bdw, border = bd, font = myFont_small, activebackground = "OrangeRed",    bg = "gray15",      fg = "White", command = clear)
button_decimal =     Button(root, text = ".",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "DeepSkyBlue2", bg = "gray3",       fg = "White", command = decimal)
button_negative =    Button(root, text = "+/-",  borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray3",       fg = "White", command = negative)
button_equals =      Button(root, text = "=",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "OrangeRed",    bg = "DodgerBlue3", fg = "White", command = equals)
button_back_space =  Button(root, text = "⌫",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = backspace)
button_square =      Button(root, text = "x²",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = squared)
button_percent =     Button(root, text = "%",    borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = percentage)
button_square_root = Button(root, text = "√",    borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = sq_root)
button_inverse =     Button(root, text = "¹⁄x",  borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = inversed)

#Put number buttons on grid on screen
button_1.grid(row = 5, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_2.grid(row = 5, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_3.grid(row = 5, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_4.grid(row = 4, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_5.grid(row = 4, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_6.grid(row = 4, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_7.grid(row = 3, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_8.grid(row = 3, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_9.grid(row = 3, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_0.grid(row = 6, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)

#put math selector buttons on grid
button_add.grid(        row = 5, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_subtract.grid(   row = 4, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_multiply.grid(   row = 3, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_divide.grid(     row = 2, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_decimal.grid(    row = 6, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_clear.grid(      row = 1, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_clear_e.grid(    row = 1, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_negative.grid(   row = 6, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_equals.grid(     row = 6, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_back_space.grid( row = 1, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_square.grid(     row = 2, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_percent.grid(    row = 1, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_square_root.grid(row = 2, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_inverse.grid(    row = 2, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)

#end master window
root.mainloop()
