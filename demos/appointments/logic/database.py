calendar = []
timeslots = []
restrictions = []


def addTimeSlot(tslot):
    global timeslots
    timeslots.append(tslot)
    timeslots.sort()


def getFirstFree():
    if len(timeslots) == 0:
        print("Not availbale!")
        return None
    return timeslots[0]


def queryScores():
    return [0, 1, 2, 3, 4]
