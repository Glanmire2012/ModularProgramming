# Script: lab3ValueReturningFunctions1.py
# Author: Owen Sheehan
# Description: Exercise 1 return a string

def name(first,last):
    fullname=(last+","+first)
    return fullname

def main():
    firstname=input("Please enter the first name:")
    surname=input("Please enter the Surname:")
    print(name(firstname,surname))

main()
