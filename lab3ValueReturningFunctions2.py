# Script :lab3ValueReturningFunctions2.py
# Author: Owen Sheehan
# Description: Exercise 2 return a string

def longest_string(s1,s2):
    s1Len=len(s1)
    s2Len=len(s2)
    if s1Len > s2Len:
        result = ("The First string is the Longest String!")
    elif s2Len > s1Len:
        result = ("The Second string is the Longest String!")
    else:
        result = ("Both of these strings are of equal lenght!")

    return result

def main():
    s1=input("Please enter the first String:")
    s2=input("Please enter the second String:")
    print(longest_string(s1,s2))

main()

