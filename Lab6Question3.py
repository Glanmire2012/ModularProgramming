# Script : Lab6Question3
# Author : Owen Sheehan
# Description : Functions, lists and strings

def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    print_months(months)

def print_months(months):
    for i in range(len(months)):
        the_month=months[i]
        print(the_month[0:3])

main()