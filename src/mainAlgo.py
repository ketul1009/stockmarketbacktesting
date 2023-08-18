import csv
from datetime import datetime

def fiveSMA(close):
    return sum(close)/5

def mainAlgo(filename):
    dataDict, closePrices=getData(filename)
    trades={}
    smaArray=[]
    sma = sum(closePrices[:5])/5
    dates = list(dataDict.keys())
    openTrade = False
    smaArray.append(sma)

    for i in range(6, len(dataDict.keys())):
        
        previousDate = dates[i-1]
        previousOpen = float(dataDict[previousDate][0])
        previousHigh = float(dataDict[previousDate][1])
        previouslow = float(dataDict[previousDate][2])
        previousClose = float(dataDict[previousDate][3])

        date = dates[i]
        openPrice = float(dataDict[date][0])
        high = float(dataDict[date][1])
        low = float(dataDict[date][2])
        close = float(dataDict[date][3])
        sma = fiveSMA(closePrices[i-4:i+1])
        smaArray.append(sma)

        if(previousHigh<sma and high>previousHigh and not openTrade):
            if(openPrice < previousHigh):
                entry = previousHigh
                sl = previousHigh*0.99
                target = previousHigh*1.02
                trades[date] = [entry, sl, target, 0, "", 0, sma]
                openTrade = True
                openDate = date

            elif(openPrice > previousHigh):
                entry = openPrice
                sl = previousHigh*0.99
                target = previousHigh*1.02
                trades[date] = [entry, sl, target, 0, "", 0, sma]
                openTrade = True
                openDate = date

        if(openTrade):
            if(high>target and openPrice<target):
                trades[openDate][3]=target
                trades[openDate][4]=date
                trades[openDate][5]=((target-entry)/entry)*100
                openTrade = False
            
            elif(openPrice>target):
                trades[openDate][3]=openPrice
                trades[openDate][4]=date
                trades[openDate][5]=((openPrice-entry)/entry)*100
                openTrade = False
            
            elif(low<sl and openPrice>sl):
                trades[openDate][3]=sl
                trades[openDate][4]=date
                trades[openDate][5]=((sl-entry)/entry)*100
                openTrade = False

            elif(openPrice<sl):
                trades[openDate][3]=openPrice
                trades[openDate][4]=date
                trades[openDate][5]=((openPrice-entry)/entry)*100
                openTrade = False

    return trades

def avgTime(startDate, endDate):
    d1 = datetime.strptime(startDate, '%Y-%m-%d')
    d2 = datetime.strptime(endDate, '%Y-%m-%d')
    date1 = datetime.timestamp(d1)
    date2 = datetime.timestamp(d2)
    return (date2-date1)/86400
    
def getAnalysis(trades):

    netReturn=0.0
    profits=0
    losses=0
    drawdown=0
    duration = 0
    for key in trades.keys():
        netReturn+=float(trades[key][5])
        if(float(trades[key][5]>0.3)):
            profits+=1
        else:
            losses+=1
            drawdown+=float(trades[key][5])

        duration+= avgTime(key, trades[key][4])
        
    analysis = [netReturn, len(trades.keys()), (profits/(profits+losses))*100, 
                    drawdown, netReturn/(profits+losses), duration/(profits+losses)]
    return analysis

def getData(filename):
    dataDict = {}
    closePrices=[]
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)

        for x in csvreader:
            dataDict[x["Date"]] = [x["Open"], x["High"], x["Low"], x["Close"]]

    for key in dataDict.keys():
        closePrices.append(float(dataDict[key][3]))

    return dataDict, closePrices
