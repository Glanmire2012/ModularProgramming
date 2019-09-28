#Script: Revision_Lab1_Question1.py
#Author: Owen Sheehan
#Description: Read and display Students name and over all mark

ok=True

try:
    while ok:
        try:
            check=True
            while check:
                studentName=input("Please enter the name of the student:")
                studentNameLenght=len(studentName)
                if studentNameLenght < 2:
                    print("Error! The students name must be 2 or more characters in lenght. Please try again.")
                else:
                    check=False
        except:
            print("Error while entering the student name!!")
        try:
            check=True
            while check:
                overallMark=int(input("Please enter the students overall exam mark (numerically):"))
                if overallMark < 0:
                    print("The exam mark must be entered as a positive number. Please try again.")
                elif overallMark > 100:
                    print("The exam mark must not exceed 100. Please try again ")
                elif overallMark >= 70:
                    check = False
                    grade="H1"
                elif overallMark >= 60:
                    check = False
                    grade="H21"
                elif overallMark >= 50:
                    check = False
                    grade="H22"
                elif overallMark >= 40:
                    check = False
                    grade="Pass"
                else:
                    check = False
                    grade="Fail"
            print("Student Name:", studentName, "  Overall Exam Mark:", overallMark, " Grade:", grade)

        except:
            print("Error while entering the exam mark!!")


except:
    print("error")