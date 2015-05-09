# Module to find the number of correct, wrong and missed responses and the
# final score from the passed response string.
import os
import xlrd , xlwt
from xlutils.copy import copy

CORRECT_MARKS = 3
INCORRECT_MARKS = -1
 

#Module to calculate result for each candidate and returns the correct# , wrong# , missed# , total score and student wise analysis of questions.
def get_result(qpset , NO_OF_QUESTIONS , response , questions) :

    path = os.curdir + os.sep + 'system' + os.sep + 'data' + os.sep
    correct = wrong = missed = invalid = 0
    f1 = open(path + 'key.txt')

    key = f1.readline()
    while key[0] != qpset :
        key = f1.readline()
    key = key[1:NO_OF_QUESTIONS + 1]
    key = key.rstrip('\n\r')				#To remove trailing \r and \n 
    response = response.rstrip('\n\r')		#To remove trailing \r and \n
    stats = ['-' for i in key]		#Maintain question wise stats.
    i = 1
    for word in key :
		if i not in questions:    #Check question is to be evaluated
			
			if response[ i - 1] != '*':			# Check Invalid response
				
				if response[ i-1 ] != ' ' :		#Check question not missed
					
					if response[ i-1 ] == word :	
						correct+=1			#Correct response
						stats[ i-1 ] = 'c'
					
					else :
						wrong+=1			#Incorrect response
						stats[ i-1 ] = 'w'
				
				else:
					missed += 1
					stats[ i-1 ] = 'm'
			
			else:
				stats[ i - 1] = '*'
				invalid += 1
		
		i += 1

    score = CORRECT_MARKS * correct + INCORRECT_MARKS * wrong
    f1.close()
    return correct , wrong , missed , invalid , score , stats
	
#Module to carry out quetion wise analysis of results.
def analyze():
	path = os.curdir + os.sep + 'system' + os.sep + 'data' + os.sep
	errors = []
	path = path + "Result.xls" 
	if(os.path.exists(path)):
		read_result = xlrd.open_workbook(path)
		result_sh = read_result.sheet_by_index(0)
	else:
		errors.append("Result file not found!")
		return errors

	write_result = copy(read_result)
	analysis_sh = write_result.add_sheet('Analysis')
	
	analysis_sh.write(0 , 0 , "Question#")
	analysis_sh.write(0 , 1 , "Correct#")
	analysis_sh.write(0 , 2 , "Wrong#")
	analysis_sh.write(0 , 3 , "Missed#")
	
	for i in xrange(5 , result_sh.ncols):
		correct = wrong = missed = 0
		for j in xrange(1,result_sh.nrows):
			value = result_sh.cell_value(j,i)
			
			if value == 'c':
				correct += 1
			
			elif value == 'w':
				wrong += 1
				
			elif value == 'm':
				missed += 1
			
			else:
				def_msg = "Question Not Evaluated"
				break
		
		if correct == 0 and wrong == 0 and missed == 0:
			analysis_sh.write(i - 4 , 0 , "Q%d"%(i - 4))
			analysis_sh.write(i - 4 , 1 , def_msg)
			analysis_sh.write(i - 4 , 2 , def_msg)
			analysis_sh.write(i - 4 , 3 , def_msg)
		else:
			analysis_sh.write(i - 4 , 0 , "Q%d"%(i - 4))
			analysis_sh.write(i - 4 , 1 , correct)
			analysis_sh.write(i - 4 , 2 , wrong)
			analysis_sh.write(i - 4 , 3 , missed)

		
	
	write_result.save(path)
		
