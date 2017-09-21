import datetime as dt
import numpy as np
from datetime import datetime

calendar = []
timeslots = []


def clear():
    global timeslots
    timeslots = []


def addTimeSlot(tslot):
    timeslots.append(tslot)
    timeslots.sort()


def getFirstFree():
    if len(timeslots) == 0:
        return None
    return timeslots[0]


def remove(date):
    if date in timeslots:
        timeslots.remove(date)


def removeFirst():
    if len(timeslots) > 0:
        del timeslots[0]


def queryScores():
    '''
    Computes a score for the following cases:
    "morning or Afternoon"
    "which day" 
    "this or next week" 

   
    '''
    days = np.zeros(shape=(7,1))
    countAfternoon = 0
    week = np.zeros(shape=(3,1))
    currentWeek = datetime.now().isocalendar()[1]
    for tsl in timeslots:
        days[tsl.weekday()] += 1
        countAfternoon += (tsl.hour > 12)
        if currentWeek == tsl.isocalendar()[1]:
            week[0] += 1
        elif (currentWeek+1) == tsl.isocalendar()[1]:
            week[1] += 1
        else:
            week[2] += 1

    moAf = min(len(timeslots) - countAfternoon, countAfternoon)
    return [moAf, np.min(days), np.min(week)]


def saveToFile():
    file = open('timeslots.txt', 'w')
    for item in timeslots:
        file.write("%s\n" % item)


def loadFromFile():
    with open('logic/timeslots.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like '\n' at the end of each line
    content = [x.strip() for x in content]
    content = [dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in content]
    global timeslots
    timeslots = content
    return


def persist(chosenDate):
    loadFromFile()
    remove(chosenDate)
    saveToFile()
