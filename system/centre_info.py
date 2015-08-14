# Module to add a centre into the Centre Information.xls file
# This module handles(saves/appends) the data entered in the centre_info form

import os
import xlrd
from constants import SYS_ROOT

'''
def save(cname , caddress , capacity):
	
	path = SYS_ROOT + os.sep + 'system' + os.sep + "data" + os.sep + 'Centre Information.xls'
	errors = []

	if os.path.exists(path) :
		wb = xlrd.open_workbook(path , formatting_info = True)
		sheet = wb.sheet_by_index(0)

		for i in range(sheet.ncols):
			col_name = sheet.cell_value(0,i)
			if col_name == 'Centre Code' :
				CODE_COL_NO = i
			elif col_name == 'Centre Name' :
				CNAME_COL_NO = i
			elif col_name == 'Centre Address' :
				CADDRESS_COL_NO = i
			elif col_name == 'Capacity' :
				CAPACITY_COL_NO = i

		row = sheet.nrows
		ccode = sheet.cell_value(row-1 , CODE_COL_NO) + 1
		wb = copy(wb)
		sheet = wb.get_sheet(0)

		sheet.write(row , CODE_COL_NO , ccode)
		sheet.write(row , CNAME_COL_NO , cname)
		sheet.write(row , CADDRESS_COL_NO , caddress)
		sheet.write(row , CAPACITY_COL_NO , capacity)

		wb.save(path)
	
	else:
		errors.append("File Not Found !!!")
	
	
	return True,errors
	'''
	
#This module takes as input the student application number and returns his/her
# allotted roll number and centre details.

#Using linear search since trend in input file is unknown.

def get_centre(app_no):
	info = []
	head = []
	data = []
	numbers = []
	errors = []
	path = SYS_ROOT + os.sep + 'system' + os.sep + "data" + os.sep + 'Roll Number Information.xls'
	if os.path.exists(path):
	 	wb = xlrd.open_workbook(path)
	 	sheet = wb.sheet_by_index(0)
		 	
		for i in xrange(0 , sheet.ncols):
			col_name = sheet.cell_value(0,i)
			head.append( sheet.cell_value(0,i) )
			if col_name in ["Application #" , "Allotted Roll No." , "Program Code" , "Centre Code" ] :
				numbers.append(i)
		info.append(head)
		
		found = False
	 	for i in xrange(1,sheet.nrows):
	 		if sheet.cell_value(i,0) == int(app_no):
	 			for j in xrange(sheet.ncols):
	 				if j in numbers:
	 					data.append( int(sheet.cell_value(i,j)) )
	 				else:
	 					data.append( sheet.cell_value(i,j) )
	 			info.append(data)
	 			found = True
	 	
	 	if not found:
	 		info.append([])
	 	 
	else:
		errors.append ("404:File Not Found!!!")
	return errors,info
