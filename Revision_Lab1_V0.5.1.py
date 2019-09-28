#Script: Revision_Lab1_Question1.py
#Author: Owen Sheehan
#Description: Read and display Students name and over all mark

ok=True
i=0
studentList=[]
markList=[]
gradeList=[]
studentName=0
overallMark=0
try:
    while ok:
        try:
            #Enter and validate student name.
            check=True
            while check:
                studentName=input("Please enter the name of the student:")
                studentNameLenght=len(studentName)
                if studentNameLenght < 2:
                    print("Error! The students name must be 2 or more characters in lenght. Please try again.")
                else:
                    studentList.append(studentName)
                    check=False
        except:
            print("Error while entering the student name!!")
        try:
            #enter and validate level of study
            check=True
            while check:
                programmeLev=int(input("At what level is the student studying? Enter only 7 or 8."))
                if programmeLev != 7 and programmeLev != 8:
                    print("Enter only 7 or 8.")
                else:
                    levTable=programmeLev
                    check=False
        except:
            print("Error while entering programme level!!")
        try:
            #Enter and validate exam mark. Assign grade based on the level of study
            check=True
            while check:
                overallMark=int(input("Please enter the students overall exam mark (numerically):"))
                if overallMark < 0:
                    print("The exam mark must be entered as a positive number. Please try again.")
                elif overallMark > 100:
                    print("The exam mark must not exceed 100. Please try again ")
                elif overallMark >= 70:
                    if levTable == 8:
                        grade="H1"
                    else:
                        grade="DT"
                    check = False
                    markList.append(overallMark)
                    gradeList.append(grade)
                elif overallMark >= 60:
                    if levTable == 8:
                        grade="H21"
                    else:
                        grade="M1"
                    check = False
                    markList.append(overallMark)
                    gradeList.append(grade)
                elif overallMark >= 50:
                    if levTable ==8:
                        grade="H22"
                    else:
                        grade="M2"
                    check = False
                    markList.append(overallMark)
                    gradeList.append(grade)
                elif overallMark >= 40:
                    grade="Pass"
                    check = False
                    markList.append(overallMark)
                    gradeList.append(grade)
                else:
                    check = False
                    grade="Fail"
                    markList.append(overallMark)
                    gradeList.append(grade)
            print("Student Name:", studentName, "  Overall Exam Mark:", overallMark, " Grade:", grade)
            print("Student Name:",studentList[i], "  Overall Exam Mark:", markList[i], " Grade:",gradeList[i])
            try:
                i=i+1
                answer=input("Do you wish to enter another student? (press Enter to continue or x to quit):")
                if answer == "x" or answer == "X":
                    ok=False
                else:
                    continue

            except:
                print("Error")
            
        except:
            print("Error while entering the exam mark!!")


except:
    print("error")