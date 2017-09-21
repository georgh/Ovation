import calendar
from datetime import datetime, timedelta

import parsedatetime as pdt  # $ pip install parsedatetime


def convertStrToDatetime():
      ##TODO
      cal = pdt.Calendar()
      now = datetime.now()
      print("now: %s" % now)
      for time_string in ["tomorrow at 6am", "next moday at noon",
                          "2 min ago", "3 weeks ago", "1 month ago"]:
          #print("%s:\t%s" % (time_string, cal.parseDT(time_string, now)[0]))
          time_struct, parse_status = cal.parse(time_string)
          print("%s:\t%s" % (time_string, datetime(*time_struct[:6])))

      time_struct, parse_status = cal.parse("tomorrow")
      datetime(*time_struct[:6])

def timeToStr(hour, min):

      if min == 0:
            if hour > 12:
                  return "{} o clock in the afternoon".format(hour - 12)
            else:
                  return "{} o clock".format(hour)
      elif min == 30:
            if hour > 12:
                  return "half past {} in the afternoon".format(hour-12)
            else:
                  return "half past {}".format(hour)
      else:
            return "{}:{}".format(hour, min)

def dateToStr(day, month):

      if day == 1:
            return "the first of {}".format(calendar.month_name[month])
      elif day == 2:
            return "the second of {}".format(calendar.month_name[month])
      elif day == 3:
            return "the third of {}".format(calendar.month_name[month])
      else:
            return "{}th of {}".format(day, calendar.month_name[month])

def convertDatetimeToStr(date):
      now = datetime.now()
      tomorrow = datetime.now() + timedelta(days=1)
      if date.date() == datetime.today().date(): #is today
            hourdiff = date.hour - now.hour
            mindiff = date.min - now.min
            return "today at {}. That's in {} hours and {} minutes".formate(timeToStr(date.hour, date.minute), hourdiff, mindiff)

      elif date.date() == tomorrow.date():
            return "tomorrow at {}".format(timeToStr(date.hour, date.minute))

      else:
            return "on {} at {}".format(dateToStr(date.day, date.month), timeToStr(date.hour, date.minute))

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




