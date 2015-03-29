# Module to save the data received into the excel sheet.

import xlrd
import xlwt
import os
from xlutils.copy import copy	#Tools for copying xlrd.Book objects to xlwt.Workbook objects.

def save(name,fname,mname,address,contact):
	errors = []
	path = os.curdir + os.sep + "system" + os.sep + 'data' + os.sep + "Student Information.xls"
	if(os.path.exists(path)):
		wb = xlrd.open_workbook(path , formatting_info = True)
		sheet = wb.sheet_by_index(0)

		for i in range(sheet.ncols):
			col_name = sheet.cell_value(0,i)
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
		
		row = sheet.nrows
		app_no = sheet.cell_value(row-1 , APP_COL_NO) + 1
		wb = copy(wb) 
		sheet = wb.get_sheet(0)
		
		sheet.write(row , APP_COL_NO , app_no)
		sheet.write(row , NAME_COL_NO , name)
		sheet.write(row , FNAME_COL_NO , fname)
		sheet.write(row , MNAME_COL_NO , mname)
		sheet.write(row , ADD_COL_NO , address)
		sheet.write(row , CON_COL_NO , contact)
		
		wb.save(path)
	else:
		errors.append("File Not Found")
	
	return True,errors
