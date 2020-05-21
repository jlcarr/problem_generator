"""
A Python module for generating long addition problems in LaTex
"""

import subprocess


def gen_long_additon(input1, input2, steps='all'):
	"""
	Given two integers this function will return the LaTex code as a string describing their additon
	"""
	# ensure correct orientation
	if input2>input1:
		temp = input1
		input1 = input2
		input2 = temp
	
	# Perorm the actual calculation
	output = input1 + input2
	
	# Set the lists of digits
	input1 = list(str(input1))
	input2 = list(str(input2))
	output = list(str(output))

	# Prepare the number of steps
	max_len = len(output)
	if steps == 'all' or steps < 0 or steps > max_len:
		steps = max_len

	# Set up the document
	doc = ""
	doc += "\\begin{equation*}\n"
	doc += "\\setlength\\arraycolsep{1pt}\n"
	doc += "\\begin{array}{*{"+str(max_len+1)+"}{c}}\n"

	# Each line ends with a new-line
	input1_latex = []
	input2_latex = []
	output_latex = []

	# Output will always be equal or longer than inputs
	carry = 0
	for step in range(max_len):
		# Obtain the digits for the column
		digit1 = input1.pop() if input1 else "\phantom{0}"
		digit2 = input2.pop() if input2 else ""
		digit3 = output.pop() if step < steps else ""

		# Draw in carry
		if carry and step-1 < steps:
			input1_latex.insert(0, " \overset{" + str(carry) + "}{" + digit1 + "}")
		else:
			input1_latex.insert(0, digit1)
		
		# draw in the rest of the column
		input2_latex.insert(0, digit2)
		output_latex.insert(0, digit3)

		# calculate the next carry
		digit1 = int(digit1) if digit1.isdigit() else 0
		digit2 = int(digit2) if digit2.isdigit() else 0
		carry = (digit1+digit2+carry)//10

	# Remove initial " & "
	input1_latex.insert(0, '')
	input2_latex.insert(0, '+')
	output_latex.insert(0, '')

	input1_latex = ' & '.join(input1_latex)
	input2_latex = ' & '.join(input2_latex)
	output_latex = ' & '.join(output_latex)

	input1_latex += " \\\\\n"
	input2_latex += " \\\\\n"
	output_latex += " \\\\\n"

	# Complete the document
	doc += input1_latex
	doc += input2_latex
	doc += "\\hline\n"
	doc += output_latex
	
	doc += "\\end{array}\n"
	doc += "\\end{equation*}\n"
	print doc

	return doc

