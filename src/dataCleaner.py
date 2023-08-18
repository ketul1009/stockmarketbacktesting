import csv

filename = "C:/Users/Ketul/Desktop/Algo Trading/Files/temp.csv"
filename2 = "C:/Users/Ketul/Desktop/Algo Trading/Files/Symbols200.csv"
symbols=[]

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for x in csvreader:
        symbols.append(x[2]+".NS")

with open(filename2, 'w', newline="") as csvfile2:
    csvwriter = csv.writer(csvfile2)
    for x in symbols:
        csvwriter.writerow([x])