#Script: Revision_Lab1_Question1.py
#Author: Owen Sheehan
#Description: Read and display Students name and over all mark

ok=True

try:
    while ok:
        studentName=input("Please enter the name of the student:")
        overallMark=int(input("Please enter the students overall exam mark (numerically):"))
        if overallMark >= 70:
            grade="H1"
        elif overallMark >= 60:
            grade="H21"
        elif overallMark >= 50:
            grade="H22"
        elif overallMark >= 40:
            grade="Pass"
        else:
            grade="Fail"
        print("Student Name:",studentName,"  Overall Exam Mark:",overallMark," Grade:",grade)

except:
    print("error")