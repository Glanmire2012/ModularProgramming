# Script: Lab7Question1
# Author: Owen Sheehan
# Description: Files and Lists

def main():
    data_file=open("samplefile1.txt")
    file_contents_as_list=read_to_list(data_file)
    data_file.close()
    save_to_file(file_contents_as_list)

def read_to_list(data_file):
    list = []
    while True:
        line = data_file.readline().rstrip()
        if line == "":
            break
        list.append(line)
    return list

def save_to_file(list):
    data_file = open("samplefile1.txt","w")
    list.sort()
    print(list[:])
    for i in range(len(list)):
        data_file.write(list[i]+"\n")
    data_file.close()

main()