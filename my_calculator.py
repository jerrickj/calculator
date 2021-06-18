from tkinter import *
import tkinter.font as font

#Master window definitions
root = Tk()
root.title("Simple Calculator")
root.geometry("300x600")
#root.iconbitmap("calculator_logo.ico")

#configure rows and columns for dynamic resizing of buttons in window
Grid.columnconfigure(root, 0, weight = 1, minsize=30)
Grid.rowconfigure(root, 0, weight = 2,)
Grid.columnconfigure(root, 1, weight = 1, minsize=30)
Grid.rowconfigure(root, 1, weight = 1, minsize=30)
Grid.columnconfigure(root, 2, weight = 1, minsize=30)
Grid.rowconfigure(root, 2, weight = 1, minsize=30)
Grid.columnconfigure(root, 3, weight = 1, minsize=30)
Grid.rowconfigure(root, 3, weight = 1, minsize=30)
Grid.rowconfigure(root, 4, weight = 1, minsize=30)
Grid.rowconfigure(root, 5, weight = 1, minsize=30)

#defines font variable for resizing
myFont = font.Font(size=25)

#Text field for entering numbers, also displays selected numbers
output = Entry(root, width = 50, borderwidth = 5, border = 4, font = myFont)
output.grid(row = 0, column = 0, columnspan=4, padx = 10, pady = 10, sticky=NSEW)

#global variables
input_1 = 0
input_2 = 0
input_symbol = ""

#functions that add clicked entries to output field
def button_click(number):
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + str(number))

def button_decimal():
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + ".")

#Functions for math
def button_clear():
    output.delete(0, END)

def button_add():
    global input_1
    global input_symbol
    input_1 = output.get()
    output.delete(0, END)
    input_symbol = "+"

def button_subtract():
    global input_1
    global input_symbol
    input_1 = output.get()
    output.delete(0, END)
    input_symbol = "-"

def button_multiply():
    global input_1
    global input_symbol
    input_1 = output.get()
    output.delete(0, END)
    input_symbol = "*"

def button_divide():
    global input_1
    global input_symbol
    input_1 = output.get()
    output.delete(0, END)
    input_symbol = "/"

def button_equals():
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
        output.insert(0, float(input_1) / float(input_2))  

#define number buttons
button_1 = Button(root, text = "1", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(1))
button_2 = Button(root, text = "2", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(2))
button_3 = Button(root, text = "3", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(3))
button_4 = Button(root, text = "4", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(4))
button_5 = Button(root, text = "5", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(5))
button_6 = Button(root, text = "6", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(6))
button_7 = Button(root, text = "7", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(7))
button_8 = Button(root, text = "8", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(8))
button_9 = Button(root, text = "9", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(9))
button_0 = Button(root, text = "0", borderwidth= 2, border = 8, font = myFont, activebackground = "Blue", command = lambda: button_click(0))


#define math symbol buttons
add =      Button(root, text = "+", borderwidth= 2, border = 8, font = myFont, activebackground = "Purple", command = button_add)
subtract = Button(root, text = "-", borderwidth= 2, border = 8, font = myFont, activebackground = "Purple", command = button_subtract)
multiply = Button(root, text = "*", borderwidth= 2, border = 8, font = myFont, activebackground = "Purple", command = button_multiply)
divide =   Button(root, text = "/", borderwidth= 2, border = 8, font = myFont, activebackground = "Purple", command = button_divide)
clear =    Button(root, text = "C", borderwidth= 2, border = 8, font = myFont, activebackground = "Red", command = button_clear)
equals =   Button(root, text = "=", borderwidth= 2, border = 8, font = myFont, activebackground = "Red", command = button_equals)
decimal =  Button(root, text = ".", borderwidth= 2, border = 8, font = myFont, activebackground = "Purple", command = button_decimal)


#Put number buttons on grid on screen
button_1.grid(row =3, column =0, sticky=NSEW)
button_2.grid(row =3, column =1, sticky=NSEW)
button_3.grid(row =3, column =2, sticky=NSEW)
button_4.grid(row =2, column =0, sticky=NSEW)
button_5.grid(row =2, column =1, sticky=NSEW)
button_6.grid(row =2, column =2, sticky=NSEW)
button_7.grid(row =1, column =0, sticky=NSEW)
button_8.grid(row =1, column =1, sticky=NSEW)
button_9.grid(row =1, column =2, sticky=NSEW)
button_0.grid(row =4, column =0, sticky=NSEW)

#put math selector buttons on grid
add.grid(row = 1, column = 3, sticky=NSEW)
subtract.grid(row = 2, column = 3, sticky=NSEW)
multiply.grid(row = 3, column = 3, sticky=NSEW)
divide.grid(row = 4, column = 3, sticky=NSEW)
clear.grid(row = 4, column = 2, sticky=NSEW)
equals.grid(row = 5, column = 0, columnspan= 4, sticky=NSEW)
decimal.grid(row = 4, column = 1, sticky=NSEW)

#end master window
root.mainloop()

#testing/learning code not needed for program

#create list of all buttons
#button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0, add, subtract, multiply, divide, clear, equals, decimal]

#loop for configuring all buttons to dynamically resize
#number_of_rows = 5
#number_of_columns = 5
#column_counter = 0
#row_counter = 0
#for button in button_list:
#    if column_counter < number_of_columns:
#        Grid.columnconfigure(root, index = column_counter, weight = 1)
#    if row_counter < number_of_rows:
#        Grid.rowconfigure(root, index = row_counter, weight = 1)
#    column_counter += 1
#    row_counter += 1


#improved (simpler) version of above loop with similar result
#column_counter = 0
#row_counter = 0
#for x in range(0,5):
#    Grid.columnconfigure(root, index = column_counter, weight = 1)
#    Grid.rowconfigure(root, index = row_counter, weight = 1)
#    column_counter += 1
#    row_counter += 1

#pads for number selector buttons
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 
#padx = 20, pady = 20, 

#pads for math selector buttons
#padx = 19, pady = 20,
#padx = 21, pady = 20,
#padx = 21, pady = 20,
#padx = 21, pady = 20,
#padx = 20, pady = 20,
#padx = 19, pady = 20,
#padx = 21, pady = 20,
