# Script: homework4
# Author: Owen Sheehan
# Description: Homework question 4 8/2/2018

def file_to_screen():
    my_file=open("file.txt")
    content=my_file.read()
    print (content.upper())
    my_file.close()

file_to_screen()

