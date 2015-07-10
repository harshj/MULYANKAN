# Module to generate roll numbers according to the capacity of the centres.
#This module works in combination with centre_allocator module.

import xlrd
import os
from constants import SYS_ROOT


def gen_roll_nos(total):
	path = SYS_ROOT + os.sep + "system" + os.sep + "data" + os.sep + "Centre Information.xls"
	centre = xlrd.open_workbook(path)
	centre_sh = centre.sheet_by_index(0)

	for i in range(centre_sh.ncols):
        
		if(centre_sh.cell_value(0,i) == 'Capacity'):
			CAP_COL_NO = i
            
		elif(centre_sh.cell_value(0,i) == 'Centre Code'):
			CODE_COL_NO = i
		
		elif(centre_sh.cell_value(0,i) == 'Centre Name'):
			NAME_COL_NO = i
		
		elif(centre_sh.cell_value(0,i) == 'Centre Address'):
			ADD_COL_NO = i

	rolls = [ [] for i in xrange(total) ]
	centre_no = 1
	rolls_allotted = 0
	while(rolls_allotted < total):
		centre_code = int (centre_sh.cell_value(centre_no , CODE_COL_NO))
		centre_name = centre_sh.cell_value(centre_no , NAME_COL_NO)
		centre_add = centre_sh.cell_value(centre_no , ADD_COL_NO)
		centre_capacity = int (centre_sh.cell_value(centre_no , CAP_COL_NO))
	
		if(total - rolls_allotted > centre_capacity):
			allot = centre_capacity
		else:
			allot = total - rolls_allotted

		for i in xrange(allot):
			roll_prog = str(rolls_allotted + 1).zfill(len(str(total)))
			#roll = int( str(centre_code) + roll_prog )
			rolls[rolls_allotted].append(roll_prog)
			rolls[rolls_allotted].append( centre_code )
			rolls[rolls_allotted].append( centre_name )
			rolls[rolls_allotted].append( centre_add )
			rolls_allotted = rolls_allotted + 1

		#rolls_allotted = rolls_allotted + allot
		centre_no = centre_no + 1
		
	return rolls
 
