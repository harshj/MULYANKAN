# Module to save the data received into the excel sheet.

import xlrd
import xlwt
import os
from xlutils.copy import copy	#Tools for copying xlrd.Book objects to xlwt.Workbook objects.

def save(name,fname,mname,address,contact):
	errors = []
	path = os.curdir + os.sep + "system" + os.sep + "Student Information.xls"
	if(os.path.exists(path)):
		student = xlrd.open_workbook(path , formatting_info = True)
		student_sh = student.sheet_by_index(0)

		for i in range(student_sh.ncols):
			col_name = student_sh.cell_value(0,i)
			if(col_name == 'Application #'):
				APP_COL_NO = i
			elif(col_name == 'Name'):
				NAME_COL_NO = i
			elif(col_name == "Father's Name"):
				FNAME_COL_NO = i
			elif(col_name == "Mother's Name"):
				MNAME_COL_NO = i
			elif(col_name == "Address"):
				ADD_COL_NO = i
			elif(col_name == "Contact No."):
				CON_COL_NO = i
		
		row = student_sh.nrows
		app_no = student_sh.cell_value(row-1 , APP_COL_NO) + 1
		student = copy(student) 
		student_sh = student.get_sheet(0)
		
		student_sh.write(row , APP_COL_NO , app_no)
		student_sh.write(row , NAME_COL_NO , name)
		student_sh.write(row , FNAME_COL_NO , fname)
		student_sh.write(row , MNAME_COL_NO , mname)
		student_sh.write(row , ADD_COL_NO , address)
		student_sh.write(row , CON_COL_NO , contact)
		
		student.save(path)
	else:
		errors.append("File Not Found")
	
	return True,errors
