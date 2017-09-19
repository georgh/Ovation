import handleDatabase as db
import datetime



d = datetime.datetime(2017,6,5,15)
db.addTimeSlot(d)
d = datetime.datetime(2017,6,9,11)
db.addTimeSlot(d)
print(db.getFirstFree())



