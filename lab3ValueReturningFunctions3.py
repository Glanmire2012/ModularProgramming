# Script: lab3ValueReturningFunctions3.py
# Author: Owen Sheehan
# Description: Exercise 3 return a float

def read_nonnegative_float(prompt):
    okay=False
    while not okay:
        try:
            dim = float(input(prompt))
            if dim >= 0:
                okay=True
            else:
                print("Please enter only non-negative numbers!")
        except:
            print("Please only enter numbers!")
    return dim

def calculate_rectangle(width,height):
    result=width*height
    return result

def display(area):
    print("The area of this Rectangle is:",area)

def main():
    height=read_nonnegative_float("Enter the Height of the Rectangle:")
    width=read_nonnegative_float("Enter the Width of the Rectangle:")
    area = calculate_rectangle(width,height)
    display(area)

main()
