#  Module to extract metadata from supplied string

from constants import ROLL_SIZE

def get_data(line):
    #global app_no, qpset ,response
    roll_no = line[0 : ROLL_SIZE]      # get roll. no.
    qpset = line[ROLL_SIZE]         # get set   
    response = line[ROLL_SIZE + 1 : ] # get response
    return roll_no , qpset , response
