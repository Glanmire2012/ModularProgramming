# Script: r00038222exam1evsd1
# Author: Owen Sheehan
# Description: exam 1

def main ():
    times=[]
    park_run, number_of_runners=read_run_details()
    times = get_times(number_of_runners)
    fastest_time = calculate_fastest(times)
    display_details(park_run, times,fastest_time)

def read_run_details():
    park_run=input("Park name >>>")
    number_of_runners=input("Number of runners >>> ")
    return park_run,number_of_runners

def get_times(number_of_runners):
    times=[]
    for i in range(int(number_of_runners)):
        run_time=input("Time (minutes) >>> ")
        times.append(run_time)
    return times

def calculate_fastest(times):
    x=0
    for i in range(len(times)):
        if x == 0:
            fastest = times[i]
            x=1
        elif x == 1:
            if times[i] <= fastest:
                fastest=times[i]
            else:
                continue
    return fastest




def display_details(park_run,times,fastest_time):
    print("Park: "+park_run)
    print("Fastest Time: "+fastest_time)
    runners_with_time=times.count(fastest_time)
    if runners_with_time <= 1:
        print("Only "+str(runners_with_time)+" runner acheived this time.")
    else:
        print("There were "+str(runners_with_time)+" runners that completed the race in this time.")

main()