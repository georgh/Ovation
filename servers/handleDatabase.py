import datetime
import database as db

def addTimeSlot(tslot):
      db.timeslots += [tslot]
      db.timeslots.sort()


def getFirstFree():
      if len(db.timeslots) ==0:
            print("Non availbale!")
            return None
      return db.timeslots[0]


class Restriction():

      day,hour,weekday, noMorning, noAfternoon

      def __init__(self, day=None, weekday=None, hour=None):
            # I can only monday 
            # -> restrict on all days beside monday (multiple calls?)
            # I cannot this monday (but next is fine)
            # -> restriction on ?
            # I
            if day == None:
                  self.day = None
            elif not isinstance(day, list):
                  self.day = [day]
            else:
                  self.day = day

            if hour == None:
                  self.hour = None
            elif not isinstance(hour, list):
                  self.hour = [hour]
            else:
                  self.hour = hour

            if weekday == None:
                  self.weekday = None
            elif not isinstance(weekday, list):
                  self.weekday = [weekday]
            else:
                  self.weekday = weekday
                

      def noMorning(self):
            self.hourRange(0,12)

      def noAfternoon(self):
            self.hourRange(12, 24)
            pass

      def hourRange(self, startTime, endTime):
            self.hour = [(startTime, endTime)]

      def apply(self):
            #filter timeslots accordingly
            #
            removeitems = []
            for tsl in db.timeslots:
                  
                  if self.weekday != None:
                        for d in self.weekday:
                              if tsl.weekday() == d:
                                    removeitems += [tsl]
                  
                  if self.day != None:
                        for d in self.day:
                              if tsl.day == d:
                                    removeitems += [tsl]

                  if self.hour != None:
                        for h in self.hour:
                              if isinstance(h, tuple):
                                    if tsl.hour >= h[0] and tsl.hour < h[1]:
                                          removeitems += [tsl]
                              else:
                                    if tsl.hour == h:
                                          removeitems += [tsl]


            print("Removing: {}".format(removeitems))
            db.timeslots = [tsl for tsl in db.timeslots if tsl not in removeitems] 


