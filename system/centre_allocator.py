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
	CCODE_COL_NO = ROLL_COL_NO + 1
	CNAME_COL_NO = CCODE_COL_NO + 1
	CADD_COL_NO = CNAME_COL_NO + 1
	
	for i in xrange(student_sh.ncols) :
		if student_sh.cell_value(0 , i) == 'Program Code':
			PROGRAM_COL_NO = i

	student = copy(student)    #To write to an existing document.
	student_wsh = student.get_sheet(0)
	student_wsh.write(0 , ROLL_COL_NO , "Allotted Roll No.")
	student_wsh.write(0 , CCODE_COL_NO , "Centre Code")
	student_wsh.write(0 , CNAME_COL_NO , "Centre Name")
	student_wsh.write(0 , CADD_COL_NO , "Centre Address")
	
	
	for i in range(total_cand):
	    roll = int( str (int(student_sh.cell_value(i+1 , PROGRAM_COL_NO))) + roll_nos[i][0] )
	    student_wsh.write(i+1 , ROLL_COL_NO , roll )
	    student_wsh.write(i+1 , CCODE_COL_NO , roll_nos[i][1])
	    student_wsh.write(i+1 , CNAME_COL_NO , roll_nos[i][2])
	    student_wsh.write(i+1 , CADD_COL_NO , roll_nos[i][3])    
	
	student.save(path + "Roll Number Information.xls")
	success = True
	return success
