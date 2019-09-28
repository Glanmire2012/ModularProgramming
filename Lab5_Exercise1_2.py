# Script: Lab5Exercise1_2
# Author: Owen Sheehan
# Description: Creating and accessing lists in python

def main():
    list1=[8,8,8,9,9,9]
    listLenght=len(list1)
    list1[listLenght-1]=0
    list1[listLenght-2]=0
    list1.reverse()
    print(list1)
    print(sum(list1))
main()