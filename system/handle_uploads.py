# This file contains modules to handle uploaded files

import os
import xlrd
from shutil import move,copy		# To create backup files.
from constants import SYS_ROOT

path = SYS_ROOT + os.sep + 'system' + os.sep + 'data' + os.sep

# Module to handle response file from generate_result
def handle_response(response):
	errors =[]
	global path
	
	move(path + "response.txt", path + "backup" + os.sep + "response.bak")	#Create backup file.
	
	try:
		f = open(path + 'response.txt', 'w')
	except IOError	:	
		errors.append("File open failed !!!")
		return errors

	for chunks in response.chunks():
		f.write(chunks)
	f.close()
	
	if f.closed == False:
		errors.append("File not closed successfully!!!")
		
	return errors
		
# Module to handle key file from generate_result
def handle_key(key):
	errors =[]
	global path
	
	move(path + "key.txt", path + "backup" + os.sep + "key.bak")	#Create backup file.
	
	try:
		f = open(path + 'key.txt', 'w')
	except IOError	:	
		errors.append("File open failed !!!")
		return errors

	for chunks in key.chunks():
		f.write(chunks)
	f.close()
	
	if f.closed == False:
		errors.append("File not closed successfully!!!")

	return errors		
		
#Module to handle centre info file from centre_info_upload_form
def handle_centre_info(centre_info):
	errors = []
	global path
	
	move(path + "Centre Information.xls", path + "backup" + os.sep + "Centre Information.bak")	#Create backup file.

	try :
		f = open(path + "Centre Information.xls" , 'w')
	except IOError:
		errors.append("File open failed !!!")
		return errors
	
	for chunks in centre_info.chunks():		#Overwrite to existing file. 
		f.write(chunks)
	f.close()

	if f.closed == False:
		errors.append("File not closed successfully!!!")
		return errors

	temp_wb = xlrd.open_workbook(path + "Centre Information.xls")
	temp_sh = temp_wb.sheet_by_index(0)
	
	columns = []
	for i in xrange(temp_sh.ncols):
		columns.append( temp_sh.cell_value(0,i) )
	
	for i in ['Centre Code' , 'Centre Name' , 'Centre Address' , 'Capacity']:		#Check for all required columns
		if i not in columns:
			errors.append("Data Insufficient!!!")
			copy(path + "backup" + os.sep + "Centre Information.bak" , path + "Centre Information.xls")	#Restore backuped up file.
			return errors
	return errors
	
# Module to handle student info file from student_info_upload_form
def handle_student_info(student_info):
	errors = []
	global path
	
	move(path + "Student Information.xls", path + "backup" + os.sep + "Student Information.bak")	#Create backup file

	try :
		f = open(path + "Student Information.xls" , 'w')
	except IOError:
		errors.append("File open failed !!!")
		return errors
	
	for chunks in student_info.chunks():		#Overwrite to existing file.
		f.write(chunks)
	f.close()

	if f.closed == False:
		errors.append("File not closed successfully!!!")
		return errors

	
	temp_wb = xlrd.open_workbook(path + "Student Information.xls")
	temp_sh = temp_wb.sheet_by_index(0)
	
	columns = []
	for i in xrange(temp_sh.ncols):
		columns.append( temp_sh.cell_value(0,i) )
	
	for i in ['Application #' , 'Name' , "Father's Name" , "Mother's Name" , 'Address' , 'Contact No.']:	#Check for all required columns.
		if i not in columns:
			errors.append("Data Insufficient!!!")
			copy(path + "backup" + os.sep + "Student Information_backup.bak" , path + "Student Information.xls")	#Restore backedup file
			return errors
		
	return errors
