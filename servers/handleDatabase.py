import datetime
import database as db

def addTimeSlot(slot):
      db.timeslots += [slot]
      db.timeslots.sort()


def getFirstFree():
      return db.timeslots[0]


class Restriction():

      def __init__():
            pass

      def applyRestriction(restriction):
            #filter timeslots accordingly
            db.timeslots
