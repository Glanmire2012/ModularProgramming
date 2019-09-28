# Script: Lab5Exercise1_3
# Author: Owen Sheehan
# Description: Creating and accessing lists in python

def main():
    countries=["Spain","Brazil","Portugal","Bolivia"]
    listLenght=len(countries)
    i=0
    for i in range(0,listLenght):
        print(countries[i])
    countries.append("Italy")
    countries.remove("Bolivia")
    i = 0
    for i in range(0, listLenght):
        print(countries[i])
    first2Countries=countries[:2]
    last2Countries=countries[2:5]
    i = 0
    print(first2Countries[:])
    print(last2Countries[:])

main()


