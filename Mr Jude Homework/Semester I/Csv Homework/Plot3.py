import csv
import statistics
import re
import matplotlib.pyplot as plt


def NAvalue():
    with open("activity.csv") as f :
        x = f.read()
        return len(re.findall("NA",x))
        
print("Total NA in activity.csv is :",NAvalue())

def strategy():
    with open("activity.csv") as f:
        x = f.read()
    with open("activity..csv","w+") as f:
        f.write(re.sub("NA","0",x))

def medianmeanperday():
    with open("activity.csv") as f:
        reader = csv.reader(f)
        next(reader)
        medianPerDay = []
        meanPerDay = []
        stepToday = []
        acc = 0
        while True:
            try:
                acc += 1
                step = next(reader)[0]
                stepToday.append(int(step) if step != "NA" else 0)
                if acc % 288 == 0:
                    stepToday.sort()
                    medianPerDay.append(statistics.median(stepToday))
                    meanPerDay.append(statistics.mean(stepToday))
                    stepToday = []
            except StopIteration:
                   break
        return medianPerDay, meanPerDay