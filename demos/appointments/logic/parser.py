import calendar
from datetime import datetime, timedelta

import parsedatetime as pdt  # $ pip install parsedatetime

FAKE_NOW = None


def convertToRange(r):
      # timespans = ["morning", "afternoon", "evening", "night"]
      if r.lower() == "morning":
            return (0, 12)
      elif r.lower() == "afternoon":
            return (12,24)
      elif r.lower() == "evening":
            return (17,24)
      elif r.lower() == "night":
            return (20,24)

def convertStrToDatetime(time_string):
      if isinstance(time_string, datetime):
            return time_string, True
      cal = pdt.Calendar()
      time_struct, parse_status = cal.parse(time_string)
      # print("%s:\t%s" % (time_string, datetime(*time_struct[:6])))
      if parse_status:
            return datetime(*time_struct[:6]), True
      else:
            return None, False
def timeToStr(hour, min):

      if min == 0:
            if hour > 18:
                  return "{} o'clock in the evening".format(hour - 12)
            if hour > 12:
                  return "{} o'clock in the afternoon".format(hour - 12)
            else:
                  return "{} o'clock in the morning".format(hour)
      elif min == 30:
            if hour > 12:
                  return "half past {} in the afternoon".format(hour-12)
            else:
                  return "half past {}".format(hour)
      else:
            return "{}:{}".format(hour, min)

def getWeekdayName(weekdayNum):
      if weekdayNum == 0:
            dayname = "Monday"
      elif weekdayNum == 1:
            dayname = "Tuesday"
      elif weekdayNum == 2:
            dayname = "Wednesday"
      elif weekdayNum == 3:
            dayname = "Thursday"
      elif weekdayNum == 4:
            dayname = "Friday"
      elif weekdayNum == 5:
            dayname = "Saturday"
      else:
            dayname = "Sunday"
      return dayname 

def dateToStr(day, month, weekdayNum):
      dayname = getWeekdayName(weekdayNum)
      if day == 1:
            return "{} the first of {}".format(dayname, calendar.month_name[month])
      elif day == 2:
            return "{} the second of {}".format(dayname, calendar.month_name[month])
      elif day == 3:
            return "{} the third of {}".format(dayname, calendar.month_name[month])
      else:
            return "{} the {}th of {}".format(dayname, day, calendar.month_name[month])

def getNow():
      global FAKE_NOW
      if FAKE_NOW:
            return FAKE_NOW
      else:
            return datetime.now()
      
def convertDatetimeToStr(date):
      if date == None:
            return "Error: Input is none"
      now = getNow()
      tomorrow = now + timedelta(days=1)
      if date.date() == now.date():  # is today
            hourdiff = date.hour - now.hour
            mindiff = date.minute - now.minute
            if hourdiff == 0:
                return "today at {}. That's in {} minutes.".format(timeToStr(date.hour, date.minute), mindiff)
            return "today at {}. That's in about {} hours".format(timeToStr(date.hour, date.minute), hourdiff)

      elif date.date() == tomorrow.date():
            return "tomorrow at {}".format(timeToStr(date.hour, date.minute))

      else:
            return "{} at {}".format(dateToStr(date.day, date.month, date.weekday()), timeToStr(date.hour, date.minute))





