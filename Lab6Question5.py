# Script : Lab6Question5
# Author : Owen Sheehan
# Description : Functions, lists and strings

def main():

    letterinput=input("Letter:")
    letter=letterinput.upper()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    letter_months=get_months_that_start_with(months,letter)
    print(letter_months)

def get_months_that_start_with(months,letter):
    letter_month=[]
    for i in range(len(months)):
        if months[i][0] == letter:
            letter_month.append(months[i])
    return letter_month
main()