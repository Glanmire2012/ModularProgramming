# Script: Lab7Question1
# Author: Owen Sheehan
# Description: Files and Lists

def main():
    data_file=open("samplefile1.txt")
    file_contents_as_list=read_to_list(data_file)
    lenght_list=lenght_of_list(file_contents_as_list)
    output(lenght_list)

def read_to_list(data_file):
    list = []
    while True:
        line = data_file.readline()
        if line == "":
            break
        list.append(line)
    return list

def lenght_of_list(list):
    lenght=len(list)
    return lenght

def output(lenght):
    print("The list is "+str(lenght)+" entries in lenght.")

main()