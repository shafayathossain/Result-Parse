
class Information:
    def __init__(self):
        self.__name = 0
        self.__registrationNumber = 0
        self.__session = 0
        self.__semester = 0
        self.__subjects = []
        self.__results = []
        self.__collegeCode = 0
        self.__collegeName = 0
        self.gpaByGrade = {'A+':4.0, 'A':3.75, 'A-':3.50, 'B+':3.25, 'B':3.0, 'B-':2.75, 'C+':2.50, 'C':2.25, 'D':2.0, 'F':0.0, 'NA':0.0, 'WM':0.0}

    def getName(self):
        return self.__name

    def getRegistrationNumber(self):
        return self.__registrationNumber

    def getSession(self):
        return self.__session

    def getSemester(self):
        return self.__semester

    def getResults(self):
        return self.__results

    def getSubjects(self):
        return self.__subjects

    def getCollegeName(self):
        return self.__collegeName

    def getCollegeCode(self):
        return self.__collegeCode

    def setName(self, studentName):
        self.__name = studentName

    def setRegistrationNumber(self, registrationNumber):
        self.__registrationNumber = registrationNumber

    def setSession(self, session):
        self.__session = session

    def setSemester(self, semester):
        self.__semester = semester

    def setSubjects(self, subjects):
        self.__subjects = subjects

    def setRrsults(self, results):
        self.__results = results

    def setCollegeName(self, collegeName):
        self.__collegeName = collegeName

    def setCollegeCode(self, collegeCode):
        self.__collegeCode = collegeCode

    def getCGPA(self, credits):
        cgpa = 0
        totalCredit = 0
        for credit, result in zip(credits, self.__results):
            if self.gpaByGrade.get(result) is not None:
                cgpa = cgpa + credit*self.gpaByGrade[result]
            totalCredit = totalCredit + credit
        cgpa = cgpa / totalCredit
        return cgpa

    def getGrade(self, cgpa):
        if(cgpa == 4.0):
            return 'A+'
        elif(cgpa >= 3.75):
            return 'A-'
        elif(cgpa >= 3.25):
            return 'B+'
        elif(cgpa >= 3.00):
            return 'B'
        elif(cgpa >= 2.75):
            return 'B-'
        elif(cgpa >= 2.50):
            return 'C+'
        elif(cgpa >= 2.25):
            return 'C'
        elif(cgpa >= 2.00):
            return 'D'
        else:
            return 'F'

