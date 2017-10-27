import mysql.connector
from Scripts import Information

connection = 0
cursor = 0

def executeQuery(query, tuple, cursor):
    cursor.execute(query, tuple)
    return cursor.next()[0]

def executeInsertion(insert, tuple, cursor, connection):
    cursor.execute(insert, tuple)
    connection.commit()

def databaseActivity(information):

    global connection
    global cursor
    if(connection ==0 and cursor == 0):
        connection = mysql.connector.connect(user = 'root', password = 'mysql', host='127.0.0.1', database = 'result', buffered = True)
        cursor = connection.cursor(buffered=True)

    query = ("SELECT id FROM college WHERE code = %s")
    insert = ("INSERT INTO college (name, code) VALUES (%s, %s)")
    collegeName = information.getCollegeName()
    collegeCode = information.getCollegeCode()
    collegeID = 0
    try:
        collegeID = executeQuery(query, (collegeCode,), cursor)
    except StopIteration:
        executeInsertion(insert, (collegeName, collegeCode,), cursor, connection)
        collegeID = executeQuery(query, (collegeCode,), cursor)

    query = ("SELECT id FROM student WHERE registration_number = %s")
    insert = ("INSERT INTO student (registration_number, name, session, college_id) VALUES (%s, %s, %s, %s)")
    studentName = information.getName()
    registrationNumber = information.getRegistrationNumber()
    session = information.getSession()
    studentId = 0
    try:
        studentId = executeQuery(query, (registrationNumber,), cursor)
    except StopIteration:
        executeInsertion(insert, (registrationNumber, studentName, session, collegeID,), cursor, connection)
        studentId = executeQuery(query, (registrationNumber,), cursor)

    query = ("SELECT credit FROM subject WHERE subject_code = %s")
    credits = []
    subjects = information.getSubjects()
    for subject in subjects:
        credits.append(executeQuery(query, (subject,), cursor))
    query = ("SELECT id FROM semester WHERE student_id = %s AND semester = %s")
    insert = ("INSERT INTO semester (student_id, semester, CGPA, grade) VALUES (%s, %s, %s, %s)")
    semester = information.getSemester()
    cgpa = information.getCGPA(credits)
    grade = information.getGrade(cgpa)
    semesterId = 0
    try:
        semesterId = executeQuery(query, (studentId, semester,), cursor)
        if semesterId is not None:
            newQuery = ("SELECT cgpa FROM semester WHERE student_id = %s AND semester = %s")
            currentCGPA = executeQuery(newQuery, (studentId, semester,), cursor)
            if(currentCGPA < cgpa):
                update = ("UPDATE semester SET cgpa = %s WHERE id = %s")
                executeInsertion(update, (cgpa, semesterId,), cursor, connection)
                semesterId = executeQuery(query, (studentId, semester,), cursor)
    except StopIteration:
        executeInsertion(insert, (studentId, semester, cgpa, grade,), cursor, connection)
        semesterId = executeQuery(query, (studentId, semester,), cursor)

    query = ("SELECT id FROM subject WHERE subject_code = %s")
    ids = []
    for subject in subjects:
        ids.append(executeQuery(query, (subject,), cursor))
    query = ("SELECT id FROM result WHERE subject_id = %s AND semester_id = %s")
    insert = ("INSERT INTO result (semester_id, subject_id, result) VALUES(%s, %s, %s)")
    results = information.getResults()
    for subjectId, result in zip(ids, results):
        try:
            resultId = executeQuery(query, (subjectId, semesterId,), cursor)
            if resultId is not None:
                newQuery = ("SELECT result FROM result WHERE id = %s")
                currentResult = executeQuery(newQuery, (resultId,), cursor)
                if(information.gpaByGrade[currentResult] < information.gpaByGrade[result]):
                    update = ("UPDATE result SET result = %s WHERE id = %s")
                    executeInsertion(update,(result, resultId,), cursor, connection)
        except StopIteration:
            executeInsertion(insert, (semesterId, subjectId, result), cursor, connection)

def databaseClose():
    global connection
    global cursor
    cursor.close()
    connection.close()

