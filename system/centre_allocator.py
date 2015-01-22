# Module to allot roll numbers to students. i/p = student info and centre
# info excel sheets, o/p = roll no. info excel sheet.

import xlrd   #To read document
import xlwt	#To write to the document
from random import shuffle
from xlutils.copy import copy	#To write to an existing document
from roll_gen import gen_roll_nos

centre = xlrd.open_workbook("Centre Information.xls" , formatting_info = True)
student = xlrd.open_workbook("Student Information.xls" , formatting_info = True)
student_sh = student.sheet_by_index(0)
centre_sh = centre.sheet_by_index(0)

#app_no = list()
#for i in range(1 , student_sh.nrows):
 #   app_no.append(int(student_sh.cell_value(i , 0)))
#random.shuffle(app_no)
#print app_no


 

total_cand = student_sh.nrows - 1
roll_nos = gen_roll_nos(total_cand)
shuffle(roll_nos)

ROLL_COL_NO = student_sh.ncols

student = copy(student)    #To write to an existing document.
student_sh = student.get_sheet(0)
student_sh.write(0 , ROLL_COL_NO , "Allotted Roll No.")
for i in range(total_cand):
    student_sh.write(i+1 , ROLL_COL_NO , roll_nos[i])

student.save("Roll Number Information.xls")

