# Script: homework2
# Author: Owen Sheehan
# Description: Homework Question 2 8/2/2018

def countdown(start):
    for i in range(start,-1,-1):
        if i >=1:
            print(i)
        elif i < 1:
            print("Blast Off!")

countdown(5)

