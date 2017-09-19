import timeslots as db

def apply(day=None, weekday=None, hour=None):
      # I can only monday 
      # -> restrict on all days beside monday (multiple calls?)
      # I cannot this monday (but next is fine)
      # -> restriction on ?
      # I
      if not isinstance(day, list) and day != None:
            day = [day]

      if not isinstance(hour, list) and hour != None:
            hour = [hour]

      if not isinstance(weekday, list) and weekday != None:
            weekday = [weekday]
          
      removeitems = []
      for tsl in db.timeslots:
            
            if weekday != None:
                  for d in weekday:
                        if tsl.weekday() == d:
                              removeitems += [tsl]
            
            if day != None:
                  for d in day:
                        if tsl.day == d:
                              removeitems += [tsl]

            if hour != None:
                  for h in hour:
                        if isinstance(h, tuple):
                              if tsl.hour >= h[0] and tsl.hour < h[1]:
                                    removeitems += [tsl]
                        else:
                              if tsl.hour == h:
                                    removeitems += [tsl]


      print("Removing: {}".format(removeitems))
      db.timeslots = [tsl for tsl in db.timeslots if tsl not in removeitems] 


