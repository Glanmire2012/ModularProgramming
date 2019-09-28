# Script : Lab6Question1
# Author : Owen Sheehan
# Description : Functions, lists and strings

def main():
    time_taken = [32,27,23,26,26,28]
    names = ["Ann","Joe","Pat","Ken","Ali","Ger"]
    target=target_times(time_taken)
    print_lists(names,time_taken,target)

def target_times(time_taken):
    target=[]
    target=[item*0.9 for item in time_taken]
    return target

def print_lists(names,time_taken,target):
    for i in range(len(names)):
        print("Name:",names[i],"Time:",time_taken[i],"Target for next race:",target[i])

main()