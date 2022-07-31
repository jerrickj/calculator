from tkinter import *
import tkinter.font as font
import math


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Jerrick's Calculator")
        self.root.geometry("350x550")
        self.root.configure(
            bg="gray26",
        )
        # root.iconbitmap("calculator_logo.ico")

        # define font variable for resizing
        self.font = font.Font(size=25, name="arial", weight="bold")
        self.font_small = font.Font(size=15)
        self.help_font = font.Font(size=12)

        # Variables for adjusting button padding
        self.pad_x = 1
        self.pad_y = 1

        # variables for adjustable button borders
        self.border = 0
        self.border_width = 1

        # global variables
        self.input_1 = 0
        self.input_2 = 0
        self.input_symbol = ""
        self.memory = []

        # Text field for entering numbers, also displays selected numbers
        self.output = Entry(
            self.root,
            width=50,
            borderwidth=self.border_width,
            border=self.border,
            bg="gray26",
            fg="White",
            justify=RIGHT,
            font=self.font,
        )
        self.output.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=NSEW)

        self.configure_columns()

        self.create_menu()

        self.define_buttons()

        self.grid_buttons()

        self.root.mainloop()

    # functions to configure the UI screen
    def configure_columns(self):
        # configure rows and columns for dynamic resizing of buttons in window
        Grid.columnconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 1, weight=1)
        Grid.columnconfigure(self.root, 2, weight=1)
        Grid.columnconfigure(self.root, 3, weight=1)
        Grid.rowconfigure(self.root, 0, weight=5)
        Grid.rowconfigure(self.root, 1, weight=0)
        Grid.rowconfigure(self.root, 2, weight=1)
        Grid.rowconfigure(self.root, 3, weight=1)
        Grid.rowconfigure(self.root, 4, weight=1)
        Grid.rowconfigure(self.root, 5, weight=1)
        Grid.rowconfigure(self.root, 6, weight=1)

    def create_menu(self):
        # define menubar object
        self.menubar = Menu(self.root, bg="gray16", fg="blue")

        # define outermost layer of manubar options (always displayed)
        self.options = Menu(self.menubar, tearoff=False, background="gray80")
        self.history = Menu(self.menubar, tearoff=False, background="gray80")
        self.help_menu = Menu(self.menubar, tearoff=False, background="gray80")

        # adds submenu's to menubar
        self.options.add_command(label="New", command=self.clear)
        self.options.add_command(label="Exit", command=self.root.quit)
        self.history.add_command(label="View", command=self.calc_history)
        self.history.add_command(label="Clear", command=self.clear_history)
        self.help_menu.add_command(label="%", command=lambda: self.help("%"))
        self.help_menu.add_command(label="CE", command=lambda: self.help("CE"))
        self.help_menu.add_command(label="C", command=lambda: self.help("C"))
        self.help_menu.add_command(label="⌫", command=lambda: self.help("⌫"))
        self.help_menu.add_command(label="¹⁄ₓ", command=lambda: self.help("¹⁄ₓ"))
        self.help_menu.add_command(label="x²", command=lambda: self.help("x²"))
        self.help_menu.add_command(label="√", command=lambda: self.help("√"))
        self.help_menu.add_command(label="+/-", command=lambda: self.help("+/-"))

        # Display the outermost layer options on menubar
        self.menubar.add_cascade(label="Options", menu=self.options)
        self.menubar.add_cascade(label="History", menu=self.history)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        # add menubar to root window
        self.root.configure(menu=self.menubar)

    def define_buttons(self):
        # define number buttons
        self.button_1 = Button(
            self.root,
            text="1",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(1),
        )
        self.button_2 = Button(
            self.root,
            text="2",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(2),
        )
        self.button_3 = Button(
            self.root,
            text="3",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(3),
        )
        self.button_4 = Button(
            self.root,
            text="4",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(4),
        )
        self.button_5 = Button(
            self.root,
            text="5",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(5),
        )
        self.button_6 = Button(
            self.root,
            text="6",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(6),
        )
        self.button_7 = Button(
            self.root,
            text="7",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(7),
        )
        self.button_8 = Button(
            self.root,
            text="8",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(8),
        )
        self.button_9 = Button(
            self.root,
            text="9",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(9),
        )
        self.button_0 = Button(
            self.root,
            text="0",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="SkyBlue1",
            bg="gray3",
            fg="White",
            command=lambda: self.button_click(0),
        )

        # define math symbol buttons
        self.button_add = Button(
            self.root,
            text="+",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.add,
        )
        self.button_subtract = Button(
            self.root,
            text="-",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.subtract,
        )
        self.button_multiply = Button(
            self.root,
            text="×",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.multiply,
        )
        self.button_divide = Button(
            self.root,
            text="÷",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.divide,
        )

        # clear clears all memory and everything, while clear_e (or clear entry) just deletes current output window
        self.button_clear_e = Button(
            self.root,
            text="CE",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="OrangeRed",
            bg="gray15",
            fg="White",
            command=self.clear_entry,
        )
        self.button_clear = Button(
            self.root,
            text="C",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="OrangeRed",
            bg="gray15",
            fg="White",
            command=self.clear,
        )
        self.button_decimal = Button(
            self.root,
            text=".",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="DeepSkyBlue2",
            bg="gray3",
            fg="White",
            command=self.decimal,
        )
        self.button_negative = Button(
            self.root,
            text="+/-",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="DeepSkyBlue2",
            bg="gray3",
            fg="White",
            command=self.negative,
        )
        self.button_equals = Button(
            self.root,
            text="=",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font,
            activebackground="OrangeRed",
            bg="DodgerBlue3",
            fg="White",
            command=self.equals,
        )
        self.button_back_space = Button(
            self.root,
            text="⌫",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="OrangeRed",
            bg="gray15",
            fg="White",
            command=self.backspace,
        )
        self.button_square = Button(
            self.root,
            text="x²",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.squared,
        )
        self.button_percent = Button(
            self.root,
            text="%",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.percentage,
        )
        self.button_square_root = Button(
            self.root,
            text="√",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.sq_root,
        )
        self.button_inverse = Button(
            self.root,
            text="¹⁄ₓ",
            borderwidth=self.border_width,
            border=self.border,
            font=self.font_small,
            activebackground="DeepSkyBlue2",
            bg="gray15",
            fg="White",
            command=self.inversed,
        )

    def grid_buttons(self):
        # Put number buttons on grid on screen
        self.button_1.grid(
            row=5, column=0, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_2.grid(
            row=5, column=1, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_3.grid(
            row=5, column=2, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_4.grid(
            row=4, column=0, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_5.grid(
            row=4, column=1, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_6.grid(
            row=4, column=2, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_7.grid(
            row=3, column=0, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_8.grid(
            row=3, column=1, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_9.grid(
            row=3, column=2, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_0.grid(
            row=6, column=1, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        # put math selector buttons on grid
        self.button_add.grid(
            row=5, column=3, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_subtract.grid(
            row=4, column=3, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_multiply.grid(
            row=3, column=3, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_divide.grid(
            row=2, column=3, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_decimal.grid(
            row=6, column=2, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_clear.grid(
            row=1, column=2, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_clear_e.grid(
            row=1, column=1, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_negative.grid(
            row=6, column=0, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_equals.grid(
            row=6, column=3, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_back_space.grid(
            row=1, column=3, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_square.grid(
            row=2, column=1, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_percent.grid(
            row=1, column=0, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_square_root.grid(
            row=2, column=2, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )
        self.button_inverse.grid(
            row=2, column=0, sticky=NSEW, padx=self.pad_x, pady=self.pad_y
        )

    # functions that add clicked entries to output field
    def button_click(self, number):
        current = self.output.get()
        self.output.delete(0, END)
        self.output.insert(0, str(current) + str(number))

    def decimal(self):
        current = self.output.get()
        self.output.delete(0, END)
        self.output.insert(0, f"{str(current)}.")

    # Functions for math
    def clear_entry(self):
        self.output["state"] = NORMAL
        self.output.delete(0, END)

    def clear(self):
        self.output["state"] = NORMAL
        self.output.delete(0, END)
        self.input_1 = 0
        self.input_2 = 0
        self.input_symbol = ""

    def add(self):  # sourcery skip: class-extract-method
        if self.input_1 != 0:
            self.equals()
        else:
            self.input_1 = self.output.get()
            self.output.delete(0, END)
            self.input_2 = 0

        self.input_symbol = "+"

    def subtract(self):
        if self.input_1 != 0:
            self.equals()
        else:
            self.input_1 = self.output.get()
            self.output.delete(0, END)
            self.input_2 = 0

        self.input_symbol = "-"

    def multiply(self):
        if self.input_1 != 0:
            self.equals()
        else:
            self.input_1 = self.output.get()
            self.output.delete(0, END)
            self.input_2 = 0

        self.input_symbol = "*"

    def divide(self):
        if self.input_1 != 0:
            self.equals()
        else:
            self.input_1 = self.output.get()
            self.output.delete(0, END)
            self.input_2 = 0

        self.input_symbol = "/"

    def equals(self):
        self.input_2 = self.output.get()
        self.output.delete(0, END)

        if type(self.input_1) == str:
            if "." in self.input_1:
                first_number = float(self.input_1)
            else:
                first_number = int(self.input_1)
        else:
            first_number = self.input_1

        if type(self.input_2) == str:
            if "." in self.input_2:
                second_number = float(self.input_2)
            else:
                second_number = int(self.input_2)
        else:
            second_number = self.input_2

        if self.input_symbol == "+":
            ans = first_number + second_number
            self.output.insert(0, ans)

        elif self.input_symbol == "-":
            ans = first_number - second_number
            self.output.insert(0, ans)

        elif self.input_symbol == "*":
            ans = first_number * second_number
            self.output.insert(0, ans)

        elif self.input_symbol == "/":
            if self.input_2 in [0, "0"]:
                self.output.insert(0, "Error, divide by 0")
                self.output["state"] = DISABLED
            else:
                ans = first_number / second_number
                self.output.insert(0, ans)

        self.memory.append(f"{self.input_1} {self.input_symbol} {self.input_2} = {ans}")
        self.input_1 = 0

    def negative(self):
        current = (
            float(self.output.get())
            if "." in self.output.get()
            else int(self.output.get())
        )
        self.output.delete(0, END)
        self.output.insert(0, -current)

    def backspace(self):
        current = self.output.get()
        self.output.delete(0, END)
        self.output.insert(0, str(current[:-1]))

    def squared(self):
        current = self.output.get()
        self.output.delete(0, END)
        self.output.insert(0, float(current) ** 2)

    def percentage(self):
        self.input_2 = self.output.get()
        self.output.delete(0, END)
        if type(self.input_1) == str:
            self.input_1 = float(self.input_1)
        if type(self.input_2) == str:
            self.input_2 = float(self.input_2)
        value = self.input_1 * self.input_2 / 100
        self.output.insert(0, value)

    def sq_root(self):
        current = float(self.output.get())
        self.output.delete(0, END)
        if current < 0:
            self.output.insert(0, "< 0 have no Sq. Root")
        else:
            self.output.insert(0, str(math.sqrt(current)))

    def inversed(self):
        current = self.output.get()
        self.output.delete(0, END)
        self.output.insert(0, str(1 / float(current)))

    # History and Help functions
    def calc_history(self):
        user_history = [
            f"\n{mem_counter}-- {x}"
            for mem_counter, x in enumerate(self.memory, start=1)
        ]

        calc_history = Tk()
        calc_history.title("History of answers")
        calc_history.geometry("300x200")
        calc_history.configure(bg="gray26")
        display = Label(calc_history, text=user_history)
        display.pack()
        calc_history.mainloop()

    def clear_history(self):
        self.memory = []

    def help(self, symbol):
        # define help window for when menu is clicked
        self.calc_help = Tk()
        self.calc_help.title("Calculator Help")
        self.calc_help.geometry("300x300")
        self.calc_help.configure(bg="gray16")

        # define help display output
        self.help_display = Label(
            self.calc_help,
            text="Old Text",
            justify=LEFT,
            wraplength=300,
            bg="gray16",
            fg="White",
            font=self.help_font,
        )

        # 'if' statements for changing window contents based on user help choice
        if symbol == "%":
            percent_symbol = """% : Percent function.\n 
        To use this, first input a starting number (x for this example), 
        then specify whether you want to add, subtract, multiply, or divide by the second number. 
        Input second number (y for this example) and then press percent.\n The program will then output a number that is y percent of x. 
        You may then press equals (=) to add, subtract, multiply, or divide this output from your first input, x. \n 
        x +-*/ (x * y / 100)"""
            self.help_display["text"] = percent_symbol

        elif symbol == "CE":
            clear_entry_symbol = """CE : Clear Entry. \n 
        This button will clear the currently displayed numbers, but will remember your other inputs, if any. 
        Akin to using 'Backspace' to clear window."""
            self.help_display["text"] = clear_entry_symbol

        elif symbol == "C":
            clear_all_symbol = """C : Clear. \n
        Will clear all previous inputs to the calculator, including current displayed calculations.
        Does not delete user history."""
            self.help_display["text"] = clear_all_symbol

        elif symbol == "⌫":
            backspace_symbol = """⌫ : Backspace. \n
        Will delete last character displayed for each click."""
            self.help_display["text"] = backspace_symbol

        elif symbol == "¹⁄ₓ":
            inverse_symbol = """¹⁄ₓ : Reciprocal function. \n
        Also called multiplicative inverse, this function will output a number (x) that when multiplied by your input, will be 1. \n
        x * (Your Number) = 1. """
            self.help_display["text"] = inverse_symbol

        elif symbol == "x²":
            squared_symbol = """x² : Square function. \n
        This function multiplies your input number by itself to give you an output, x. \n
        Your Number * Your Number = x """
            self.help_display["text"] = squared_symbol

        elif symbol == "√":
            square_root_symbol = """√ : Square root function.
        Outputs a number (x) that, when multiplied by itself, is equal to your input. \n
        x * x = Your Number"""
            self.help_display["text"] = square_root_symbol

        elif symbol == "+/-":
            pos_neg_symbol = """+/- : Positive/Negative \n
        Changes sign of input from positve to negative, or from negative to positive.
        Will not work if no numbers have been entered into the current field yet. \n
        x = -x or -x = x"""
            self.help_display["text"] = pos_neg_symbol

        self.help_display.pack()
        # end help window
        self.calc_help.mainloop()


if __name__ == "__main__":
    Calculator()
