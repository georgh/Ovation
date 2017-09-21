import calendar
from datetime import datetime, timedelta

import parsedatetime as pdt  # $ pip install parsedatetime


def convertStrToDatetime(time_string):
      cal = pdt.Calendar()
      time_struct, parse_status = cal.parse(time_string)
      # print("%s:\t%s" % (time_string, datetime(*time_struct[:6])))
      return datetime(*time_struct[:6])

def timeToStr(hour, min):

      if min == 0:
            if hour > 18:
                  return "{} o clock in the evening".format(hour - 12)
            if hour > 12:
                  return "{} o clock in the afternoon".format(hour - 12)
            else:
                  return "{} o clock in the morning".format(hour)
      elif min == 30:
            if hour > 12:
                  return "half past {} in the afternoon".format(hour-12)
            else:
                  return "half past {}".format(hour)
      else:
            return "{}:{}".format(hour, min)

def dateToStr(day, month, weekdayNum):
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

      if day == 1:
            return "{} the first of {}".format(dayname, calendar.month_name[month])
      elif day == 2:
            return "{} the second of {}".format(dayname, calendar.month_name[month])
      elif day == 3:
            return "{} the third of {}".format(dayname, calendar.month_name[month])
      else:
            return "{} the {}th of {}".format(dayname, day, calendar.month_name[month])

def convertDatetimeToStr(date):
      now = datetime.now()
      tomorrow = datetime.now() + timedelta(days=1)
      if date.date() == datetime.today().date(): #is today
            hourdiff = date.hour - now.hour
            mindiff = date.minute - now.minute
            if hourdiff == 0:
                return "today at {}. That's in {} minutes.".format(timeToStr(date.hour, date.minute), mindiff)
            return "today at {}. That's in about {} hours".format(timeToStr(date.hour, date.minute), hourdiff)

      elif date.date() == tomorrow.date():
            return "tomorrow at {}".format(timeToStr(date.hour, date.minute))

      else:
            return "{} at {}".format(dateToStr(date.day, date.month, date.weekday()), timeToStr(date.hour, date.minute))

      # date.day
      # date.month
      # date.year
      # date.weekday()
      # date.minute
      # date.hour

      # #check for today
      # #skip today and say in XX hours/XXminutes
      # #check for tomoorw
      # #check for next week

      # {tomorrow/next week/on XX.XX} at {X a clock/half past X/XX:XX}




