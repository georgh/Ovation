import datetime as dt

calendar = []
timeslots = []


# TODO Persist calendar and handle it

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


def removeFirst():
    del timeslots[0]


def queryScores():
    return [1, 2, 3]


def saveToFile():
    file = open('timeslots.txt', 'w')
    for item in timeslots:
        file.write("%s\n" % item)


def loadFromFile():
    with open('timeslots.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like '\n' at the end of each line
    content = [x.strip() for x in content]
    content = [dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in content]
    global timeslots
    timeslots = content
    return
