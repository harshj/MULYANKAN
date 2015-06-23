# Module to allot roll numbers to students. i/p = student info and centre
# info excel sheets, o/p = roll no. info excel sheet.

import xlrd   #To read document
import xlwt	#To write to the document
import os
from random import shuffle
from xlutils.copy import copy	#To write to an existing document
from roll_gen import gen_roll_nos
from constants import SYS_ROOT

def allocate():
	success = False
	path = SYS_ROOT + os.sep + "system" + os.sep + "data" + os.sep 
	student = xlrd.open_workbook(path + "Student Information.xls" , formatting_info = True)
	student_sh = student.sheet_by_index(0)

	total_cand = student_sh.nrows - 1
	roll_nos = gen_roll_nos(total_cand)
	shuffle(roll_nos)

	ROLL_COL_NO = student_sh.ncols

	student = copy(student)    #To write to an existing document.
	student_sh = student.get_sheet(0)
	student_sh.write(0 , ROLL_COL_NO , "Allotted Roll No.")
	for i in range(total_cand):
	    student_sh.write(i+1 , ROLL_COL_NO , roll_nos[i])
	
	student.save(path + "Roll Number Information.xls")
	success = True
	return success
