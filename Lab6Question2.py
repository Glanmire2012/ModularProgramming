# Script : Lab6Question2
# Author : Owen Sheehan
# Description : Functions, lists and strings

def main():
    names=["Mary","Ann","Ben","Kate","Emily"]
    ages=[4,7,9,2,1]
    over_fives=get_over_fives(names,ages)
    print(over_fives)

def get_over_fives(names,ages):
    over_fives=[]
    for i in range(len(ages)):
        if ages[i] >= 5:
            over_fives.append(names[i])
    return over_fives

main()