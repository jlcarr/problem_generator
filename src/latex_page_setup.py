"""
A Python module for generating long addition problems in LaTex
"""

import long_addition

import subprocess
import os


def gen_latex_doc(inner_latex):
	"""
	Create the latex page setup
	"""
	doc = ""
	doc += "\\documentclass{article}\n"
	doc += "\\usepackage{array,mathtools}\n"
	
	doc += "\\begin{document}\n"

	doc += inner_latex
	
	doc += "\\end{document}"

	return doc


def write_latex(latex, file_name, relative_path):
	"""
	Create the latex page setup
	"""
	path = os.path.join(relative_path, file_name)
	file = open(path, 'w')
	file.write(latex)
	file.close()

	subprocess.call(["pdflatex", "-output-directory="+relative_path, path])




if __name__ == "__main__":
	latex = gen_latex_doc(long_addition.gen_long_additon(9756, 432))
	write_latex(latex, 'test.tex', '../out')

