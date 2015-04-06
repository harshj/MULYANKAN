# Module to evaluate results and save them to Result.xls 
import string
import xlwt
import xlrd
import os
from shutil import copy	#To make backup of results

from data import get_data
from result import get_result, analyze

#ROLL_SIZE = 13
# questions: questions not to be evaluated.
NO_OF_QUESTIONS = 156
def evaluate(questions = []):
	errors = []
	temp = []
	for q in questions:
		if q != " ":
			temp.append(int(q))
	questions = temp
	wb = xlwt.Workbook()
	ws = wb.add_sheet('Result')
	i = 0
	ws.write(i,0,'Roll No.')
	ws.write(i,1,'Correct')
	ws.write(i,2,'Incorrect')
	ws.write(i,3,'Missed')
	ws.write(i,4,'Marks Obtained')
	for j in xrange(NO_OF_QUESTIONS):
		ws.write( i,j + 5,'Q%d'%(j+1) )
	
	try:
		path = os.curdir + os.sep + 'system' + os.sep + 'data' + os.sep
		f = open (path + 'response.txt' )
	except IOError:
		errors.append("File not found error!!!")
		return False,errors

	for line in f :
	    i += 1
	    j = 5
	    data = line[84:]
	    roll_no , qpset , response = get_data(data)
	    correct , wrong , missed , score , stats = get_result(qpset , response , questions)
	    ws.write(i,0,roll_no)
	    ws.write(i,1,correct)
	    ws.write(i,2,wrong)
	    ws.write(i,3,missed)
	    ws.write(i,4,score)
	    for j in xrange(NO_OF_QUESTIONS):
	        ws.write( i , j + 5 , stats[j] )
	f.close()
	
	copy(path + "Result.xls" , path + "backup" + os.sep + "Previous Result.bak")		#Make backup of previous result.
	wb.save(path + "Result.xls")
	analyze()
	return errors

#show function returns a list of list which contains all the data of Result.xls
def show(n):
	path = os.curdir + os.sep + 'system' + os.sep + 'data' + os.sep + 'Result.xls'
	errors = []
	if(os.path.exists(path)):
		wb = xlrd.open_workbook(path)
		sh = wb.sheet_by_index(n)
		data = []
		row = []
		for i in xrange(0,sh.nrows):
			for j in xrange(0,sh.ncols):
				temp  = sh.cell_value(i,j)				
				'''if i > 0 :
					temp = int(temp)		#Values read from excel sheets are in floating point.'''
				
				row.append(temp)
			data.append(row)
			row = []
		
		success = True
					
				
	else:
		errors.append("File Not Found!!!")
		success = False
	
	return data,success,errors

