import logic.database as db

"""
This class implements the logic of the QA for the bot aka it chooses
a meaningful answer for the user based on the current slots available
and the last questions asked (so that we do not repeat them)
"""

questions = []

RETARDMODE = True

def clear():
    global questions
    questions = []


def countFirstSlots():
    return questions.count('first')


def returnFirst():
    value = db.getFirstFree()
    if value is None:
        return "There are no free appointments slots free in the next two weeks."
    else:
        questions.append(str(value))
        return "First free slot would be " + str(value)

def nextQuestion():
    global RETARDMODE
    if countFirstSlots() < 2 or RETARDMODE:
        questions.append("first")
        return returnFirst()

    scores = db.queryScores()

    # Erase the non-suitable questions
    if "morningAfternoon" in questions:
        scores[0] = 0
    if "dayOfWeek" in questions:
        scores[1] = 0
    if "weekInMonth" in questions:
        scores[2] = 0

    # Check if there are scores which are non-zero
    if sum(scores) != 0:
        index = scores.index(max(scores))
        # Morning/Afternoon
        if index == 0:
            questions.append("morningAfternoon")
            return "Do you prefer to schedule the appointment in the morning or in the afternoon?"
        # Day of week
        elif index == 1:
            questions.append("dayOfWeek")
            return "Which day of the week would you prefer?"
        # Week in the month
        elif index == 2:
            questions.append("weekInMonth")
            return "Would you prefer this week or the next?"

    return returnFirst()
