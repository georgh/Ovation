import datetime

timeslots = []
restrictions = []

def addTimeSlot(tslot):
      global timeslots
      timeslots += [tslot]
      timeslots.sort()


def getFirstFree():
      global timeslots
      if len(timeslots) == 0:
            print("Non availbale!")
            return None
      return timeslots[0]


def removeFirst():
      if len(timeslots) != 0:
            del timeslots[0]



