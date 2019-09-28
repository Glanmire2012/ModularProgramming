#Script: Void5
#Author: Owen Sheehan
#Description: Void functions 1

EDGE_SOLID="+"
MIDDLE_SOLID="-"
EDGE_GAPPY="|"
HEIGHT_OF_BOX=2
SPACE=" "
def box_sides():
    print(EDGE_GAPPY+SPACE*6+EDGE_GAPPY)

def box_end():
    print(EDGE_SOLID+MIDDLE_SOLID*6+EDGE_SOLID)


def draw_box():
    for i in range(3):
        box_sides()
    box_end()

def draw_nose():
    print("   /\\")
    print("  /  \\")
    print(" /    \\")
    print("/      \\")
    box_end()

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