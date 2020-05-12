import re

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


def f_op(to_calc):

	if "+" or "-" or "x" or "/" in to_calc:

		to_calc = re.split('([^\d\.])', to_calc)
		print(to_calc)

		while len(to_calc) > 2:

			a = to_calc[0]
			b = to_calc[2]

			if to_calc[1] == "+":
				c = float(a) + float(b)
			elif to_calc[1] == "-":
				c = float(a) - float(b)
			elif to_calc[1] == "x":
				c = float(a) * float(b)
			elif to_calc[1] == "/":
				c = float(a) / float(b)
			elif to_calc[1] == "%":
				c = float(a) / 100
				return c

			del to_calc[0:3]
			to_calc.insert(0, c)
			print(to_calc)

	
	return to_calc[0]