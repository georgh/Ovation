days = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday",
        "sunday", "tomorrow", "today"]
timespans = ["morning", "afternoon", "evening", "night"]

DAY = 1
TIMESPAN = 2


def valid_entity(entity_type, entity_value):
    valid = False
    testList = []
    if entity_type == DAY:
        testList = days
    if entity_type == TIMESPAN:
        testList = timespans
    for word in testList:
        if entity_value == word:
            valid = True
    return valid


def filterList(entity_list):
    filteredList = []
    for entity in entity_list:
        if entity.entity.lower() == "day" and valid_entity(DAY, entity.value.lower()):
            filteredList.append(entity)
        if entity.entity.lower() == "timespan" and valid_entity(TIMESPAN, entity.value.lower()):
            filteredList.append(entity)
        if entity.entity.lower() == "date":
            filteredList.append(entity)
    return filteredList
