import string
import xlwt

from data import get_data
from result import get_result

#ROLL_SIZE = 13

def evaluate():  
	wb = xlwt.Workbook()
	ws = wb.add_sheet('result')
	i = 0
	ws.write(i,0,'Roll No.')
	ws.write(i,1,'Correct')
	ws.write(i,2,'Incorrect')
	ws.write(i,3,'Missed')
	ws.write(i,4,'Marks Obtained')

	f = open ("TEST1.txt")

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
	wb.save("Result.xls")
evaluate()
