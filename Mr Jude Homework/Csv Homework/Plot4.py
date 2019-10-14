import csv
from matplotlib import pyplot as plt
from datetime import datetime
import statistics

def day_type(rows):
  for row in rows:
    day_of_week = datetime.strptime(row[1], "%Y-%M-%d").weekday()
    if day_of_week <= 4:
      row.append("weekday")
    else:
      row.append("weekend") 

with open("activity.csv") as f:
  reader = csv.reader(f)
  header = next(reader)
  rows = [row for row in reader]
  interval_range = [int(row[2]) for row in rows][:288]
  weekday_averages, weekend_averages = [], []

  
  set_day_status(rows)
  print(rows)

  
  for interval in interval_range:
    weekend_interval_sum, weekend_interval_count, weekend_interval_average = 0, 0, 0
    weekday_interval_sum, weekday_interval_count, weekday_interval_average = 0, 0, 0
    for row in rows:
      if int(row[2]) == interval and row[0] != "NA":
        if row[3] == "weekend":
          weekend_interval_sum += int(row[0])
          weekend_interval_count += 1
          weekend_interval_average = weekend_interval_sum / weekend_interval_count
        elif row[3] == "weekday":
          weekday_interval_sum += int(row[0])
          weekday_interval_count += 1
          weekday_interval_average = weekday_interval_sum / weekday_interval_count
    weekend_averages.append(weekend_interval_average)
    weekday_averages.append(weekday_interval_average)
  
  plt.plot(interval_range, weekend_averages)
  plt.plot(interval_range, weekday_averages)
  plt.legend(['Weekend', 'Weekday'])
  plt.show()
  
                 
                 