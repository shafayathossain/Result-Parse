import os
from Scripts import ParseInfo
from Scripts.Database import databaseClose

f = open(os.path.join('../ResultFiles/result.txt'), 'r')
for lines in f.readlines():
    line = lines.strip();
    if len(line)>0:
        ParseInfo.process(line)
databaseClose()




'''
    semester name will initialize once
    list of subject_code initialize once
    
    if college_name found:
        update college_name
        update college_code
    from every_line :
        update registration_number
        update name
        update session
        update list_of_result
    
    
'''