# Script : Lab6Question4
# Author : Owen Sheehan
# Description : Functions, lists and strings

def main():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    abbrev_names=get_short_names(months)
    print(abbrev_names)

def get_short_names(months):
    short_month=[]
    for i in range(len(months)):
        short_month.append(months[i][0:3])
        # the_month=months[i]
        # short=the_month[0:3]
        # short_month.append(short)
    return short_month
main()