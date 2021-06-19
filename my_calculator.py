from tkinter import *
import tkinter.font as font
import math

#Master window definitions
root = Tk()
root.title("Jerrick's Calculator")
root.geometry("350x550")
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
myFont = font.Font(size = 25, name = "arial", weight = "bold")
myFont_small = font.Font(size = 15)
help_font = font.Font(size = 12)

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

#Text field for entering numbers, also displays selected numbers
output = Entry(root, width = 50, borderwidth = bdw, border = bd, bg = "gray26", fg = "White", justify = RIGHT, font = myFont)
output.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10, sticky=NSEW)

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

    con_in1 = float(input_1) if '.' in input_1 else int(input_1)
    con_in2 = float(input_2) if '.' in input_2 else int(input_2)

    if input_symbol == "+":
        ans = con_in1 + con_in2
        output.insert(0, ans)

    elif input_symbol == "-":
        ans = con_in1 - con_in2
        output.insert(0, ans)

    elif input_symbol == "*":
        ans = con_in1 * con_in2
        output.insert(0, ans)

    elif input_symbol == "/":
        if input_2 == 0 or input_2 == "0":
            output.insert(0, "Error, divide by 0")
            output["state"] = DISABLED
        else:
            ans = con_in1 / con_in2
            output.insert(0, ans) 

    memory.append(ans)
    input_1 = 0

def negative():
    current = float(output.get()) if '.' in output.get() else int(output.get())
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
    input_1_1 = float(input_1) if '.' in input_1 else int(input_1)
    input_2_2 = float(input_2) if '.' in input_2 else int(input_2)
    value = input_1_1 * input_2_2 / 100
    output.insert(0, value)

def sq_root():
    current = float(output.get())
    output.delete(0, END)
    if current < 0:
        output.insert(0, "< 0 have no Sq. Root")
    else:
        output.insert(0, str(math.sqrt(current)))

def inversed():
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(1/float(current)))

def calc_history():
    global memory
    user_history = []
    mem_counter = 1
    for x in memory:
        user_history.append(str(mem_counter) + "-- " + str(x))
        mem_counter += 1 
    calc_history = Tk()
    calc_history.title("History of answers")
    calc_history.geometry("300x200")
    calc_history.configure(bg = "gray26")
    display = Label(calc_history, text = user_history)
    display.pack()
    calc_history.mainloop()

def clear_history():
    global memory
    memory = []

def help(symbol):

    #variables for text output from help menu
    percent_symbol = """% : Percent function.\n 
    To use this, first input a starting number (x for this example), 
    then specify whether you want to add, subtract, multiply, or divide by the second number. 
    Input second number (y for this example) and then press percent.\n The program will then output a number that is y percent of x. 
    You may then press equals (=) to add, subtract, multiply, or divide this output from your first input, x. \n 
    x +-*/ (x * y / 100)"""

    clear_entry_symbol = """CE : Clear Entry. \n 
    This button will clear the currently displayed numbers, but will remember your other inputs, if any. 
    Akin to using 'Backspace' to clear window."""

    clear_all_symbol = """C : Clear. \n
    Will clear all previous inputs to the calculator, including current displayed calculations.
    Does not delete user history."""

    backspace_symbol = """⌫ : Backspace. \n
    Will delete last character displayed for each click."""

    inverse_symbol = """¹⁄ₓ : Reciprocal function. \n
    Also called multiplicative inverse, this function will output a number (x) that when multiplied by your input, will be 1. \n
    x * (Your Number) = 1. """

    squared_symbol = """x² : Square function. \n
    This function multiplies your input number by itself to give you an output, x. \n
    Your Number * Your Number = x """

    square_root_symbol = """√ : Square root function.
    Outputs a number (x) that, when multiplied by itself, is equal to your input. \n
    x * x = Your Number"""

    pos_neg_symbol = """+/- : Positive/Negative \n
    Changes sign of input from positve to negative, or from negative to positive.
    Will not work if no numbers have been entered into the current field yet. \n
    x = -x or -x = x"""

    #define help window
    calc_help = Tk()
    calc_help.title("Calculator Help")
    calc_help.geometry("300x300")
    calc_help.configure(bg = "gray16")
    
    #define help display output
    help_display = Label(calc_help, text = "Old Text", justify = LEFT, wraplength = 300, bg = "gray16", fg = "White", font = help_font)
    help_display.pack()
 
    #if statements for changing window contents based on user help choice
    if symbol == "%":
        help_display["text"] = percent_symbol
    elif symbol == "CE":
        help_display["text"] = clear_entry_symbol
    elif symbol == "C":
        help_display["text"] = clear_all_symbol
    elif symbol == "⌫":
        help_display["text"] = backspace_symbol
    elif symbol == "¹⁄ₓ":
        help_display["text"] = inverse_symbol
    elif symbol == "x²":
        help_display["text"] = squared_symbol
    elif symbol == "√":
        help_display["text"] = square_root_symbol
    elif symbol == "+/-":
        help_display["text"] = pos_neg_symbol

    #end help window
    calc_help.mainloop()

#define menubar object
menubar = Menu(root, bg = "gray16", fg = "blue")

#define outermost layer of options (always displayed)
options = Menu(menubar, tearoff = False, background = "gray80")
history = Menu(menubar, tearoff = False, background = "gray80")
help_menu = Menu(menubar, tearoff = False, background = "gray80")

#adds submenu's
options.add_command(label = "New", command = clear)
options.add_command(label = "Exit", command = root.quit)

history.add_command(label = "View", command = calc_history)
history.add_command(label = "Clear", command = clear_history)

help_menu.add_command(label = "%", command = lambda: help("%"))
help_menu.add_command(label = "CE", command = lambda: help("CE"))
help_menu.add_command(label = "C", command = lambda: help("C"))
help_menu.add_command(label = "⌫", command = lambda: help("⌫"))
help_menu.add_command(label = "¹⁄ₓ", command = lambda: help("¹⁄ₓ"))
help_menu.add_command(label = "x²", command = lambda: help("x²"))
help_menu.add_command(label = "√", command = lambda: help("√"))
help_menu.add_command(label = "+/-", command = lambda: help("+/-"))

# Display the outermost layer options on menubar
menubar.add_cascade(label = "Options", menu = options)
menubar.add_cascade(label = "History", menu = history)
menubar.add_cascade(label = "Help", menu = help_menu)

#adds menubar to root window
root.configure(menu = menubar)


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

#clear clears all memory and everything, while clear_e (or clear entry) just deletes current output window
button_clear_e =     Button(root, text = "CE",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "OrangeRed",    bg = "gray15",      fg = "White", command = clear_entry)
button_clear =       Button(root, text = "C",    borderwidth= bdw, border = bd, font = myFont_small, activebackground = "OrangeRed",    bg = "gray15",      fg = "White", command = clear)
button_decimal =     Button(root, text = ".",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "DeepSkyBlue2", bg = "gray3",       fg = "White", command = decimal)
button_negative =    Button(root, text = "+/-",  borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray3",       fg = "White", command = negative)
button_equals =      Button(root, text = "=",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "OrangeRed",    bg = "DodgerBlue3", fg = "White", command = equals)
button_back_space =  Button(root, text = "⌫",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "OrangeRed",    bg = "gray15",      fg = "White", command = backspace)
button_square =      Button(root, text = "x²",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = squared)
button_percent =     Button(root, text = "%",    borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = percentage)
button_square_root = Button(root, text = "√",   borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2",  bg = "gray15",      fg = "White", command = sq_root)
button_inverse =     Button(root, text = "¹⁄ₓ",  borderwidth= bdw, border = bd, font = myFont_small, activebackground = "DeepSkyBlue2", bg = "gray15",      fg = "White", command = inversed)

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
