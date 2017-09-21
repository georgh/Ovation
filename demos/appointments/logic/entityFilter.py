DAYS = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday",
        "sunday", "tomorrow", "yesterday"]
TIMESPANS = ["morning", "afternoon", "evening", "night"]


def entityIsValid(entity):
    global DAYS, TIMESPANS
    return ((entity.entity == "day" and entity.value in DAYS)
            or (entity.entity == "timespan" and TIMESPANS)
            or not entity.entity in ["day", "timespan"])
