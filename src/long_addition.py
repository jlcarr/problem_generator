"""
A Python module for generating long addition problems in LaTex
"""

import subprocess


def gen_long_additon(input1, input2):
	"""
	Given two integers this function will return the LaTex code as a string describing their additon
	"""
	output = input1 + input2

	# ensure correct orientation
	if input2>input1:
		temp = input1
		input1 = input2
		input2 = temp
	
	input1 = list(str(input1))
	input2 = list(str(input2))
	output = list(str(output))

	max_len = max(len(input1), len(input2), len(output))

	doc = ""
	doc += "\\documentclass{article}\n"
	doc += "\\usepackage{array,mathtools}\n"
	
	doc += "\\begin{document}\n"
	doc += "\\begin{equation*}\n"

	doc += "\\setlength\\arraycolsep{1pt}\n"
	doc += "\\begin{array}{*{"+str(max_len)+"}{c}}\n"


	input1_latex = " \\\\\n"
	input2_latex = " \\\\\n"
	output_latex = " \\\\\n"

	carry = 0
	while input1 and input2 and output:
		digit1 = input1.pop()
		digit2 = input2.pop()
		digit3 = output.pop()

		if carry:
			input1_latex = " & \overset{" + str(carry) + "}{" + digit1 + "}" + input1_latex
		else:
			input1_latex = " & " + digit1 + input1_latex
		
		input2_latex = " & " + digit2 + input2_latex
		output_latex = " & " + digit3 + output_latex

		carry = (int(digit1)+int(digit2)+carry)//10

	while input1 and output:
		digit1 = input1.pop()
		digit3 = output.pop()

		if carry:
			input1_latex = " & \overset{" + str(carry) + "}{" + digit1 + "}" + input1_latex
		else:
			input1_latex = " & " + digit1 + input1_latex
		
		input2_latex = " & " + input2_latex
		output_latex = " & " + digit3 + output_latex
		
		carry = (int(digit1)+carry)//10

	while output:
		digit3 = output.pop()
		
		if carry:
			input1_latex = " & \overset{" + str(carry) + "}{\phantom{0}}" + input1_latex
		else:
			input1_latex = " & " + input1_latex

		input2_latex = " & " + input2_latex
		output_latex = " & " + digit3 + output_latex

	input1_latex = input1_latex[3:]
	input2_latex = input2_latex[3:]
	output_latex = output_latex[3:]


	doc += input1_latex
	doc += input2_latex
	doc += "\\hline\n"
	doc += output_latex

	doc += "\\end{array}\n"
	
	doc += "\\end{equation*}\n"
	doc += "\\end{document}"

	return doc



if __name__ == "__main__":
	file = open('../out/test.tex','w')
	file.write(gen_long_additon(9756,432))
	file.close()

	subprocess.call(["pdflatex", "-output-directory=../out", "../out/test.tex"])
