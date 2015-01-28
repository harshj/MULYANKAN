# Module to generate roll numbers according to the capacity of the centres.

import xlrd
import os

path = os.curdir + os.sep + "system" + os.sep + "Centre Information.xls"
centre = xlrd.open_workbook(path)
centre_sh = centre.sheet_by_index(0)

def gen_roll_nos(total):

    for i in range(centre_sh.ncols):
        
        if(centre_sh.cell_value(0,i) == 'Capacity'):
            CAP_COL_NO = i
            
        elif(centre_sh.cell_value(0,i) == 'Centre Code'):
            CODE_COL_NO = i

    #print CAP_COL_NO, CODE_COL_NO
    rolls = list()
    centre_no = 1
    rolls_allotted = 0
    while(rolls_allotted < total):
        centre_code = int (centre_sh.cell_value(centre_no , CODE_COL_NO))
        centre_capacity = int (centre_sh.cell_value(centre_no , CAP_COL_NO))
        if(total - rolls_allotted > centre_capacity):
            allot = centre_capacity
        else:
            allot = total - rolls_allotted

        for i in range(allot):
                roll_prog = str(rolls_allotted + i + 1).zfill(len(str(total)))
                roll = int( str(centre_code) + roll_prog )
                rolls.append(roll)

        rolls_allotted = rolls_allotted + centre_capacity
        centre_no = centre_no + 1

    return rolls
 
