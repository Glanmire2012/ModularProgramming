# Script: Lab5Exercise1_1
# Author: Owen Sheehan
# Description: Creating and accessing lists in python

def main ():
    list1=[15,14,77,23]
    print("The first number in the list is",list1[0])
    listLenght=len(list1)
    print("The Last number in the list is",list1[listLenght-1])
    print("The list is",listLenght,"numbers in Lenght")
    list2=[]+list1
    i=0
    for i in range(0,listLenght):
        list1[i]+=1
    print(list1)
    print(list2)
main()