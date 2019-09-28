# Script: homework3
# Author: Owen Sheehan
# Description: Homework Question 3 8/2/2018

def countdown(start,finish):
    for i in range(start,finish-1,-1):
        print(i)
    if i == 1:
        print("Blast Off!")
    else:
        print("Mission Aborted!")

countdown(5,1)

