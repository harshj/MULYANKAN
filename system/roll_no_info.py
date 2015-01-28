# This module returns the contents of file "Roll Number Info.xls" along with
# a boolean flag "success" and the list of "errors".
# It does not takes any arguments.

import xlrd
import os

def show():
	path = os.curdir + os.sep + 'system' + os.sep + 'Roll Number Information.xls'
	errors = []
	if os.path.exists(path): 
		wb = xlrd.open_workbook(path)
		sh = wb.sheet_by_index(0)
		data = []
		row = []
		numbers = []
		strings = []
		for i in xrange(0 , sh.ncols):
			col_name = sh.cell_value(0,i)
			if col_name in ["Application #" , "Allotted Roll No."] :
				numbers.append(i)
			else:
				strings.append(i)
		for i in xrange(1,sh.nrows):
			for j in xrange(0 , sh.ncols):
				temp = sh.cell_value(i,j)
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
