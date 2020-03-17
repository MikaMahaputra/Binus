import csv
from matplotlib import pyplot as plt

    
def time_series():
    with open("activity.csv") as f:
        reader = csv.reader(f)
        next(reader)
        step_intervals = [0]*288
        days = 61
        acc = 0
        while True :
            try:
                step = next(reader)[0]
                step_intervals[acc] += int(step) if step != "NA" else 0
                acc += 1
                if acc == 288:
                    acc = 0
            except StopIteration:
                break
        return step_intervals
    
def average (steps_interval):
    days = 61
    avg= []
    for step in steps_interval:
        avg.append(step/days)
    return avg

def makeplot():
    fig,axs =plt.subplots(2)   
    axs[0].set_title("Steps per 5 mins")
    axs[0].plot(time_series())
    axs[1].set_title("Average steps per 5 mins")
    axs[1].plot(average(time_series()))
    plt.tight_layout()
    plt.show() 
    
makeplot()