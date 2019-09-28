#Script: Revision_Lab1_Question1.py
#Author: Owen Sheehan
#Description: Read and display Students name and over all mark

ok=True

try:
    while ok:
        studentName=input("Please enter the name of the student:")
        overallMark=int(input("Please enter the students overall exam mark (numerically):"))
        print("Student Name:",studentName,"  Overall Exam Mark:",overallMark)

except:
    print("error")