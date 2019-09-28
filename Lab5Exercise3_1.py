# Script: Lab5Exercise2_1
# Author: Owen Sheehan
# Description: Scores

def main():
    runner=[]
    time=[]
    for i in range(4):
        runner.append(input("Enter the name of the runner:"))
        time.append(input("What was their time in seconds:"))
    winTime=min(time)
    indWin=time.index(winTime)
    print("The winner is",runner[indWin],"with a time of",time[indWin],"seconds.")
    i=0
    for i in range(4):
        if i != indWin:
            runTime=time[i]-time[indWin]
            print(runTime)

            #lostBy=(runTime-winTime)
            #print(runner[i],"was",lostBy,"seconds behind")


main()