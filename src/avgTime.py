import csv
import pandas as pd

filename = "C:/Users/Ketul/Desktop/lovebabbar.csv"
time=[]
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for x in csvreader:
        time.append(x[2])

for x in time:
    if(len(x)==7):
        time[time.index(x)]="0"+x
    elif(len(x)==4):
        time[time.index(x)]="00:0"+x
    else:
        time[time.index(x)]="00:"+x

totalHrs=0
totalMin=0
totalSec=0


for x in time:
    totalHrs+=int(x[0:2])
    totalMin+=int(x[3:5])
    totalSec+=int(x[6:])

print(totalHrs, totalMin, totalSec)
    
