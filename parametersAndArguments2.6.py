# Script: parametersAndArguments2.6
# Author: Owen Sheehan
# Description: Parameters and arguments lab work

def draw_hair(times):
    for i in range (times):
        print("#"*4)


def draw_eyes(include):
    if include:
        print("----")
        print("@  @")
    else:
        print("@  @")

def draw_nose(passed):
    print(" "+passed*2)

def draw_mouth(times):
    print("="*times)

def main():
    brow=input("Do you want Eybrows? y/n")
    draw_hair(2)
    if brow == "y":
        draw_eyes(True)
    elif brow == "n":
        draw_eyes(False)
    draw_nose("|")
    draw_mouth(4)


main()