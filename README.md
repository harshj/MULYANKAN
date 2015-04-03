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
  6.Contact No
  
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
system and key file (.txt format)(optional) which contains the correct answers to the questions according to the 
question paper set. The contents of the key.txt file may look like as mentioned below:

A123442413241342314234213
B134132432413224132243423
C243142313341324132413243
D434134132413231324213134

# Development
This system is developed in PYTHON v2.7 and the GUI is web based and provided with help of Django(v1.6) framework.
Additionally xlrd and xlwt packages have been used for reading and writing to the Excel spreadsheets (primarily due
to which the system reads and creates .xls files and not .xlsx files).
The operating systems used for development and testing are Windows 8.1 and Linux Mint 17 and thus this system works 
well in both these environments and though not tested it is also beleived to work on Mac OS.
