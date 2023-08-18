import mainAlgo as ma
import csv

filename = "C:/Users/Ketul/Desktop/Algo Trading/Files/Symbols200.csv"
path = "C:/Users/Ketul/Desktop/Algo Trading/Historical Data/"
resultFile = "C:/Users/Ketul/Desktop/Algo Trading/Results/Results.csv"
finalResults=[]

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for x in csvreader:
        symbol = str(x)[2:len(str(x))-2]
        symbolFile = path + str(x)+".csv"
        try:
            symbolResult = ma.mainAlgo(symbolFile)
            analysis = ma.getAnalysis(symbolResult)
            finalResults.append([symbol]+analysis)
        except Exception as e:
            print(e, symbol, "Failure")

with open(resultFile, 'w', newline="") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    fields = ["Name", "Return", "Total Trades", "% Profitable", "Drawdown", "Avg Trade", "Avg Days"]
    csvwriter.writerow(fields)   

    # writing the data rows 
    for x in finalResults:
        csvwriter.writerow(x)

