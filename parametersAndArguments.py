# Script: parametersAndArguments1.5
# Author: Owen Sheehan
# Description: Parameters and arguments Lab work

def sing_verse(number):

    if number >= 2:
        print(number, "green bottles hanging on the wall,")
        print(number, "green bottles hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print("There'll be",number-1,"green bottles hanging on the wall.")
    elif number == 1:
        print(number, "green bottle hanging on the wall,")
        print(number, "green bottle hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print("There'll be no green bottles hanging on the wall.")
def main():
    for i in range(10,0,-1):
        sing_verse(i)

main()


