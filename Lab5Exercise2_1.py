# Script: Lab5Exercise2_1
# Author: Owen Sheehan
# Description: Scores

def main():
    result=0
    scores=[9,8,6,7,6]
    judges=["kim","tim","fin","lynn","wynn"]
    listLen=len(scores)
    tScore=0
    i=0
    for i in range(listLen):
        tScore+=scores[i]
    scoreAv=tScore/listLen
    print("The average Score is",scoreAv)
    print("The lowest score was:",min(scores))
    print("The largest score was:",max(scores))
    low=min(scores)
    i=0
    n=0
    for i in range(listLen):
        if scores[i]==low:
            print(judges[i],"gave a score of",low)
            n+=1
    print(n,"judge(s) gave a score of",low)
    scores.sort()
    scores.reverse()
    i=0
    for i in range(3):
        result+=scores[i]
    if result >= 25:
        print("Proceeds to the next round with a score of",result)
    else:
        print("Has Failed to reach the next round with a score of",result)


main()