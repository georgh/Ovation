import datetime
import database as db

def addTimeSlot(slot):
      db.timeslots += [slot]
      db.timeslots.sort()


def getFirstFree():
      return db.timeslots[0]


class Restriction():

      def __init__(self, day=None, weekday=None, hour=None):
            # I can only monday 
            # -> restrict on all days beside monday (multiple calls)
            # I cannot this monday (but next is fine)
            # -> restriction on ?
            # I
            self.day = day
            self.hour = hour
            self.weekday = weekday                 


      def apply(self):
            #filter timeslots accordingly
            #
            removeitems = []
            for sl in db.timeslots:
                  if self.day != None:
                        if sl.weekday() == self.weekday:
                              removeitems += [sl]
                  if self.day != None:
                        if sl.day == self.day:
                              removeitems += [sl]

            print("Removing: {}".format(removeitems))
            db.timeslots = [sl for sl in db.timeslots if sl not in removeitems] 


