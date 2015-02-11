# Module to evaluate results and save them to Result.xls 
import string
import xlwt
import xlrd
import os

from data import get_data
from result import get_result

#ROLL_SIZE = 13

def evaluate():
	success = False  
	errors = []
	wb = xlwt.Workbook()
	ws = wb.add_sheet('result')
	i = 0
	ws.write(i,0,'Roll No.')
	ws.write(i,1,'Correct')
	ws.write(i,2,'Incorrect')
	ws.write(i,3,'Missed')
	ws.write(i,4,'Marks Obtained')
	
	try:
		path = os.curdir + os.sep + 'system' + os.sep
		f = open (path + 'TEST1.txt' )
	except IOError:
		errors.append("File not found error!!!")
		return False,errors

	for line in f :
	    i += 1
	    j = 5
	    data = line[84:]
	    roll_no , qpset , response = get_data(data)
	    correct , wrong , missed , score = get_result(qpset , response)
	    ws.write(i,0,roll_no)
    	    ws.write(i,1,correct)
   	    ws.write(i,2,wrong)
            ws.write(i,3,missed)
            ws.write(i,4,score)

	f.close()
	wb.save(path + "Result.xls")
	success = True
	
	return success , errors

#show function returns a list of list which contains all the data of Result.xls
def show():
	path = os.curdir + os.sep + 'system' + os.sep + 'Result.xls'
	errors = []
	if(os.path.exists(path)):
		wb = xlrd.open_workbook(path)
		sh = wb.sheet_by_index(0)
		data = []
		row = []
		for i in xrange(0,sh.nrows):
			for j in xrange(0,sh.ncols):
				temp  = sh.cell_value(i,j)				
				if i > 0 :
					temp = int(temp)
				
				row.append(temp)
			data.append(row)
			row = []
		
		success = True
					
				
	else:
		errors.append("File Not Found!!!")
		success = False
	
	return data,success,errors

#save function to save the incoming file to appropriate directories.
#def save(f):
