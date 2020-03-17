#%%
import csv
from matplotlib import pyplot as plt
import datetime as dt
import statistics as st

filename = "activity.csv"
dict = {}
dictInterval = {}
dictIntervalWeekDays = {}
dictIntervalWeekEnds = {}

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if (steps!= "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date), [])
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval, [])
            dictInterval[interval].append(int(steps))
            
            if (date2 % 7 == 0):
                dictIntervalWeekEnds.setdefault(interval, [])
                dictIntervalWeekEnds[interval].append(int(steps))
            else:
                dictIntervalWeekDays.setdefault(interval, [])
                dictIntervalWeekDays[interval].append(int(steps))
                
listDate = []
listTotal = []
listAve = []
for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))
    
plt.hist(listTotal)
plt.title("Total steps per day")
plt.xlabel("Steps per day")    
plt.ylabel("Frequency")
plt.yticks(range(0, 25, 5))
plt.show()

print("The Mean is :", st.mean(listTotal))
print("The Median is :", st.median(sorted(listTotal)))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    