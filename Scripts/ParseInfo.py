import re
from Scripts import Information
from Scripts.Database import databaseActivity

semester = 0
collegeName = 0
collegeCode = 0
subjectCodeList = []

def process(line):
    #print(line)

    '''
    :param line:
    To avoid initialization every time, initialized globally. To use that global variables, declare those by 'global variable_name'

    We split every line into list of strings(:var listOfString) by [ ]*[|][ ]* to get result easily.
    If the word 'SEMESTER' found, then index(40th) character is the number of semester.
    If the word 'College' found, then substring[9:13] will be college code and substring[15:end] will be college name.
    If :var listOfString has more than 4 elements, then it must be a line from result table. So:
        If listOfString[1] consists of 'ROLL NO' then it is the attribute name line of the table.
            Get the subject code list from there. Sublist[5:end] will be subject code list
        Else that line consists of result of a information.
            Get registration number from index(2) of listOfString
            Get session from index(3) of listOfString
            Get information's name from index(4) of listOfString
            Get information's grade list from sublist of listOfString[5:end]


    :return:
    '''
    global collegeName
    global collegeCode
    global semester
    global subjectCodeList

    registrationNumber = 0
    studentName = 0
    session = 0
    gradeList = []
    information = Information.Information()

    listOfStrings = re.split('[ ]*[|][ ]*', line)
    if str(line).find('SEMESTER') != -1:
        semester = line[40:41]
    elif str(line).find('College') == 0:
        collegeCode = line[9:13]
        collegeName = line[15:-1]
    elif len(listOfStrings) > 4:
        if str(listOfStrings[1]) == 'ROLL NO':
            if not len(subjectCodeList)>0:
                for eachSubjectCode in listOfStrings[5:-1]:
                    subjectCodeList.append(int(eachSubjectCode))
        else:
            registrationNumber = listOfStrings[2]
            session = listOfStrings[3]
            studentName = listOfStrings[4]
            for eachGrade in listOfStrings[5:-1]:
                gradeList.append(eachGrade)
            if(studentName == ''):
                studentName = "NO NAME"
            information.setName(studentName)
            information.setRegistrationNumber(registrationNumber)
            information.setSession(session)
            information.setSemester(semester)
            information.setSubjects(subjectCodeList)
            information.setRrsults(gradeList)
            information.setCollegeCode(collegeCode)
            information.setCollegeName(collegeName)
            if(len(gradeList) == len(subjectCodeList)):
                databaseActivity(information)
            print(information.getName())

