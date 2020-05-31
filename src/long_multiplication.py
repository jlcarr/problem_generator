"""
A Python module for generating long multiplication problems in LaTex
"""

def gen_long_multiplication(input1, input2, steps='all'):
	"""
	Given two integers this function will return the LaTex code as a string describing their multiplication
	"""
	# ensure correct orientation
	if input2>input1:
		temp = input1
		input1 = input2
		input2 = temp
	
	# Perorm the actual calculation
	output = input1 * input2
	
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
	sub_outputs = [[] for digit in input2]
	output_latex = []

	# Output will always be equal or longer than inputs
	carry = 0
	for i_digit2, digit2 in enumerate(input2[::-1]):
		carry = 0
		sub_outputs[i_digit2] = ["0"]*i_digit2
		for i_digit1, digit1 in enumerate(input1[::-1]):
			sub_result = int(digit1) * int(digit2) + carry
			digit = sub_result%10
			carry = sub_result//10
			sub_outputs[i_digit2].insert(0, str(digit))
		sub_outputs[i_digit2].insert(0, str(carry))
		sub_outputs[i_digit2] = ['']*(max_len-len(sub_outputs[i_digit2])) + sub_outputs[i_digit2]

	# Remove initial " & "
	input1_latex = ['']*(max_len-len(input1)) + input1
	input2_latex = ['']*(max_len-len(input2)) + input2
	output_latex = ['']*(max_len-len(output)) + output
	input1_latex.insert(0, '')
	input2_latex.insert(0, '\\times')
	for row in sub_outputs:
		row.insert(0, '')
	output_latex.insert(0, '')

	input1_latex = ' & '.join(input1_latex)
	input2_latex = ' & '.join(input2_latex)
	sub_outputs_latex = list(map(lambda row: ' & '.join(row), sub_outputs))
	output_latex = ' & '.join(output_latex)

	input1_latex += " \\\\\n"
	input2_latex += " \\\\\n"
	sub_outputs_latex = list(map(lambda row: row + " \\\\\n", sub_outputs_latex))
	output_latex += " \\\\\n"

	# Complete the document
	doc += input1_latex
	doc += input2_latex
	doc += "\\hline\n"
	for row in sub_outputs_latex:
		doc += row
	doc += "\\hline\n"
	doc += output_latex
	
	doc += "\\end{array}\n"
	doc += "\\end{equation*}\n"
	print doc

	return doc

