import timeslots as db

def apply(day=None, weekday=None, hour=None):
      """
      Valid calls:
      all 3 parameters take a single instance or a list of values
      Example: weekday=[0,2] removes all mondays and wednesdays
      Parameter hour takes in additon a tuple.
      If given a tuple, all times between (start, end) are removed. End is excluded
      Example: hour=[(1,4), 7] will remove all entries with 1 <= hour < 4 and hour==7

      You can also combine multiple restrictions:
      hour=5, weekday=1 removes the slot at 5 a clock tuesday
      """

      #if we get an single instance, convert it to list:
      if not isinstance(day, list):
            day = [day]

      if not isinstance(hour, list):
            hour = [hour]

      if not isinstance(weekday, list):
            weekday = [weekday]
          
      removeitems = []
      for tsl in db.timeslots:
            
            for w in weekday:
                  for d in day:
                        for h in hour:
                              if (tsl.weekday() == w or w == None) and (tsl.day == d or d == None) :
                                    if isinstance(h, tuple):
                                          if (tsl.hour >= h[0] and tsl.hour < h[1]):
                                                removeitems += [tsl]
                                    elif h == None or tsl.hour == h:
                                          removeitems += [tsl]

      print("Removing: {}".format(removeitems))
      db.timeslots = [tsl for tsl in db.timeslots if tsl not in removeitems] 


