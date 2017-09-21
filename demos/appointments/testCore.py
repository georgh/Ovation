import logic.core as core
import logic.parser as parser
from logic import database as db
from datetime import datetime

db.loadFromFile()

print("Database initialized! entries are now:")
for b in db.timeslots:
      print("{} weekday: {}".format(b, b.weekday()))

now, _ = parser.convertStrToDatetime("tomorrow")
user_input = core.UserInput("", 
      core.Intent.POSITIVE, 
      [core.Entity(str(now), "date")])
print(user_input.entities)
res = core.response(user_input)
print(res.text)

print("afterwards:")

for b in db.timeslots:
      print("{} weekday: {}".format(b, b.weekday()))
