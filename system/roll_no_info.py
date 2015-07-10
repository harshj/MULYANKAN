# This module returns the contents of file "Roll Number Info.xls" along with
# a boolean flag "success" and the list of "errors".
# It does not takes any arguments.

import xlrd
import os
from constants import SYS_ROOT

def show():
	path = SYS_ROOT + os.sep + 'system' + os.sep + 'data' + os.sep + 'Roll Number Information.xls'
	errors = []
	if os.path.exists(path): 
		wb = xlrd.open_workbook(path)
		sh = wb.sheet_by_index(0)
		data = []
		row = []
		numbers = []
		strings = []
		
		# The values read are float by default, we need to change them to int.
		for i in xrange(0 , sh.ncols):
			col_name = sh.cell_value(0,i)
			if col_name in ["Application #" , "Allotted Roll No." , "Program Code"] :
				numbers.append(i)
			else:
				strings.append(i)
				
		for i in xrange(0,sh.nrows):
			for j in xrange(0 , sh.ncols):
				temp = sh.cell_value(i,j)
				if i > 0:				
					if j in numbers:
						temp=int(temp)
					else:
						temp = str(temp)
				row.append(temp)		
			data.append(row)
			row = []
		success	= True	

	else:
		errors.append("File Not Found.")
		success = False

	return data , success , errors
