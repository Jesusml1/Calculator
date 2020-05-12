# ENDOGENIC CALULATOR V1.0

from tkinter import *
import re

# OPERATIONS FUNTION

def op(to_calc):

	if "+" or "-" or "x" or "/" in to_calc:

		to_calc = re.split("(\D)",to_calc)

		while len(to_calc) > 2:

			a = to_calc[0]
			b = to_calc[2]

			if to_calc[1] == "+":
				c = int(a) + int(b)
			elif to_calc[1] == "-":
				c = int(a) - int(b)
			elif to_calc[1] == "x":
				c = int(a) * int(b)
			elif to_calc[1] == "/":
				c = int(a) / int(b)
			elif to_calc[1] == "%":
				c = int(a) / 100
				return c

			del to_calc[0:3]
			to_calc.insert(0, c)
			print(to_calc)

	

	return to_calc[0]

#FUNCTION PER BOTTOM

def clear():
	display_entry.delete(0, END)
	display_result.configure(text = "")

def calc():
	to_calc = display_entry.get()
	display_result.configure(text = str(op(to_calc)))

# TKINTER WINDOW 

window = Tk()
window.title("Calculator v1.0")
window.resizable(width = False, height = False)

display_entry = Entry(window, text = "", justify = 'left')
display_entry.grid(column = 0, row = 0, padx = 5, pady = 20, columnspan = 4)
# display_entry.insert="grey")

display_result = Label(window, text = "", )
display_result.grid(column = 2, row = 1, padx = 5, pady = 10, columnspan = 2)

clear_button = Button(text = "      C      ", command = clear)
clear_button.grid(column = 0, row = 2, pady = 5, columnspan = 2)

result_button = Button(text = "      =      ", command = calc)
result_button.grid(column = 2, row = 2, pady = 5, columnspan = 2)
window.bind('<Return>', calc)

zero_button = Button(text = "0", command = lambda: display_entry.insert(END, "0"))
zero_button.grid(column = 0, row = 6, padx = 5, pady = 5)

one_button = Button(text = "1", command = lambda: display_entry.insert(END, "1"))
one_button.grid(column = 0, row = 5, padx = 5, pady = 5)

two_button = Button(text = "2", command = lambda: display_entry.insert(END, "2"))
two_button.grid(column = 1, row = 5, padx = 5, pady = 5)

three_button = Button(text = "3", command = lambda: display_entry.insert(END, "3"))
three_button.grid(column = 2, row = 5, padx = 5, pady = 5)

four_button = Button(text = "4", command = lambda: display_entry.insert(END, "4"))
four_button.grid(column = 0, row = 4, padx = 5, pady = 5)

five_button = Button(text = "5", command = lambda: display_entry.insert(END, "5"))
five_button.grid(column = 1, row = 4, padx = 5, pady = 5)

six_button = Button(text = "6", command = lambda :display_entry.insert(END, "6"))
six_button.grid(column = 2, row = 4, padx = 5, pady = 5)

seven_button = Button(text = "7", command = lambda :display_entry.insert(END, "7"))
seven_button.grid(column = 0, row = 3, padx = 5, pady = 5)

eight_button = Button(text = "8", command = lambda: display_entry.insert(END, "8"))
eight_button.grid(column = 1, row = 3, padx = 5, pady = 5)

nine_button = Button(text = "9", command = lambda: display_entry.insert(END, "9"))
nine_button.grid(column = 2, row = 3, padx = 5, pady = 5)

sum_button = Button(text = "+", command = lambda: display_entry.insert(END, "+"))
sum_button.grid(column = 3, row = 3, padx = 5, pady = 5)

sub_button = Button(text = "-", command = lambda: display_entry.insert(END, "-"))
sub_button.grid(column = 3, row = 4, padx = 5, pady = 5)

mul_button = Button(text = "x", command = lambda: display_entry.insert(END, "x"))
mul_button.grid(column = 3, row = 5, padx = 5, pady = 5)

div_button = Button(text = "/", command = lambda: display_entry.insert(END, "/"))
div_button.grid(column = 3, row = 6, padx = 5, pady = 5)

comma_button = Button(text = ".", command = lambda: display_entry.insert(END, "."))
comma_button.grid(column = 1, row = 6, padx = 5, pady = 5)

perc_button = Button(text = "%", command = lambda: display_entry.insert(END, "%"))
perc_button.grid(column = 2, row = 6, padx = 5, pady = 5)

window.mainloop()