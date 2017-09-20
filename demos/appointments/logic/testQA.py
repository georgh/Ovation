import logic.database as db
import logic.questionAnswer as qa

# adding values to database:
db.loadFromFile()

print("Database initialized:")
for b in db.timeslots:
    print("{} weekday: {}".format(b, b.weekday()))

print("----")
print(qa.nextQuestion())
print("User says: NO")
db.removeFirst()
print(qa.nextQuestion())
print("User says: NO")
db.removeFirst()
print(qa.nextQuestion())
print("User says: I like trains")
print(qa.nextQuestion())
print("User says: Shibboleth")
print(qa.nextQuestion())
print("User says: Cowabunga")
print(qa.nextQuestion())
print("User says: NO")
db.removeFirst()
print(qa.nextQuestion())
print("User says: NO")
db.removeFirst()
print(qa.nextQuestion())
print("User says: NO")
db.removeFirst()
print(qa.nextQuestion())
print("User says: NO")
db.removeFirst()
print(qa.nextQuestion())
