calendar = []
timeslots = []
restrictions = []


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
