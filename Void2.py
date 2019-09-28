#Script: Void1
#Author: Owen Sheehan
#Description: Void functions 1



def draw_box():
    for i in range(3):
        print("-      -")
    print("+------+")

def draw_nose():
    print("   /\\")
    print("  /  \\|")
    print(" /    \\")
    print("/      \\")
    print("+------+")

def draw_thrusters():
    print("  //\\\\")
    print(" //  \\\\")
    print("//    \\\\")


def draw_shuttle():
    draw_nose()
    for i in range(3):
        draw_box()
    draw_thrusters()


draw_shuttle()