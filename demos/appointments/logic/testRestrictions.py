import datetime as dt

import database as db
import restriction

#adding values to database:
d = dt.datetime(2017, 9, 1)
d = d.replace(day=19, hour=9) #tuesday
db.addTimeSlot(d)
d = d.replace(day=19, hour=19)
db.addTimeSlot(d)
d = d.replace(day=26, hour=12)
db.addTimeSlot(d)
d = d.replace(day=24, hour=12)
db.addTimeSlot(d)
d = d.replace(day=24, hour=13)
db.addTimeSlot(d)
d = d.replace(day=23, hour=12)
db.addTimeSlot(d)

print("Database initialized! entries are now:")
for b in db.timeslots:
      print("{} weekday: {}".format(b, b.weekday()))

print(db.queryScores())

print("First free: " + str(db.getFirstFree()))

print("Removing Wednesday:")
restriction.apply(weekday=2)
print("First free: " + str(db.getFirstFree()))

print("Removing before 10:")
restriction.apply(hour=(0, 10))
print("First free: " + str(db.getFirstFree()))

print("Removing the 26th:")
restriction.apply(day=26)
print("First free: " + str(db.getFirstFree()))

print("Removing the 24 and 25:")
restriction.apply(day=[24, 25])
print("First free: " + str(db.getFirstFree()))

print("Testing combined restrictions: Hour between 12 and 20 weekday Tuesday ")
restriction.apply(weekday=1, hour=(12, 20))
print("First free: " + str(db.getFirstFree()))

print("Final Databse entries are:")
for b in db.timeslots:
      print("{} weekday: {}".format(b, b.weekday()))
