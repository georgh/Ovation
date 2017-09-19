import datetime
import timeslots as db

def addTimeSlot(tslot):
      db.timeslots += [tslot]
      db.timeslots.sort()


def getFirstFree():
      if len(db.timeslots) ==0:
            print("Non availbale!")
            return None
      return db.timeslots[0]