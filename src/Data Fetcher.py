# Importing the yfinance package
import yfinance as yf
import csv
 
# Set the start and end date
start_date = '2021-12-20'
end_date = '2022-12-31'
filename = "C:/Users/Ketul/Desktop/Algo Trading/Files/Symbols200.csv"

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for x in csvreader:
        try:
            # Set the ticker
            ticker = x
            
            # Get the data
            data = yf.download(ticker, start_date, end_date)
            
            #export data
            path = "C:/Users/Ketul/Desktop/Algo Trading/Historical Data/" + str(x[:2])+".csv"
            data.to_csv(path)
        except:
            print(x, " Not available")