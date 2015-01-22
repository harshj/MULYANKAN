
import os
import xlrd,xlwt
from xlutils.copy import copy

def save(cname , caddress , capacity):
	
	path = os.curdir + os.sep + 'system' + os.sep + 'Centre Information.xls'
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
