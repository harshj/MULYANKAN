# MULYANKAN
Mulyanakan is a project which carries out the following tasks:-
1. Examination Roll Number Generation 
2. Centre Allocation 
3. Result Evaluation 

# Roll Number Generation and Centre Allocation
For the purpose of examination roll number generation the user needs upload two Excel(.xls) documents. First containing
the following columns :-
  1. Application #
  2. Name
  3. Father's Name
  4. Mother's Name
  5. Address
  6. Contact No
  
which is saved as Student Information.xls in the system/data directory and second containing the following columns:-
 
  1. Centre Code
  2. Centre Name
  3. Centre Address
  4. Capacity
which is saved as Centre Information in the system/data directory. The user may also append the entries one at a time 
to the above mentioned files from the system interface itself.

After all the data is uploaded to the system, the "Allocate Centres and Generate Enrollment Numbers" link will 
automatically generate the roll numbers and allocate examination centres in random fashion so that no two applicants
having consecutive application number get the same centre for examination.

The "Show Allotted Enrollment Numbers" link can than be used to view the allocated examination roll numbers 
corresponding to the application number.

# Result Evaluation
For result evaluation, the user is required to supply the raw response file (.txt format) directly from the OMR 
system(tested for Panasonic systems) and key file (.txt format)(optional) which contains the correct answers to 
the questions according to the question paper set. The contents of the key.txt file may look like as mentioned below:

  A123442413241342314234213
  B134132432413224132243423
  C243142313341324132413243
  D434134132413231324213134
  
For further details one can refer to the sample inputs provided in the 'Samples' directory.
The defaults can be changed for the result evaluation system as follows:-
	1. Number of Question to be evaluated : 
		Go to constants.py in system directory and change the constant NO_OF_QUES.
		
	2. Number of marks to be awarded for correct, incorrect , missed and invalid responses :
		Go to constants.py file in system directory and change the constants on the top to the desired values.
	
	3. The roll number size :
		Roll size is required since the system reads the lines from the response file and ignores the first few bits which
		are equal to the size of the roll number.
		Go to data.py file in system directory and change the constant ROLL_SIZE to the desired value.
	
	4. Passive data size:
		Passive data is that data which is read from the OCR such as the booklet code , name of candidate and other such 
		information which is not used in the system. These number of bits must be specified to be ignored while reading 
		response.
		To change the size of passive data go to constants.py in system directory and change the constant
		PASSIVE_DATA to the desired value.
	
	5. Booklet Code size:
		Booklet code size is required to extract booklet code from passive data incase a faulty qpset is encountered.
		To change its size goto constants.py in system directory and change the constant BOOKLET_CODE_SIZE to
		the desired value. Works only when the booklet code appears in the beginning of every response line.
		
	6. System Root Directory (SYS_ROOT):
		The Django docs suggest that one should use absolute paths in django application. The absolute path may be different
		while deploying this app for different systems, so one must set the SYS_ROOT variable in constants.py file as the absolute
		path to the root directory of the application i.e. the directory containing the manage.py file. This is set to os.cur by 
		default since it works during development and testing on various Operating Systems and must be chanaged while Deploying. 
	
# Development
This system is developed in PYTHON v2.7 and the GUI is web based and provided with help of Django(v1.6) framework.
Additionally xlrd and xlwt packages have been used for reading and writing to the Excel spreadsheets (primarily due
to which the system reads and creates .xls files and not .xlsx files).
The operating systems used for development and testing are Windows 8.1 and Linux Mint 17 and thus this system works 
well in both these environments and though not tested it is also beleived to work on Mac OS.

# Deployment
To deploy this system , the following modules are needed:
1. Python v2.7  
        sudo apt-get install python 2.7
2. Django v1.6
        sudo apt-get install python-pip
        sudo pip install Django==1.6
3. xlrd        
4. xlwt
5. xlutils
        sudo pip install xlrd xlwt xlutils

After setting up the system, cd into the root directory of the system(which contains manage.py and this readme file) and 
execute "python manage.py runserver" to deploy the system.
