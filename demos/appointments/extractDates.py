import re
from dateutil import parser

month="(january|february|march|arpil|may|june|july|august|september|october|november|december)"
day="(monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow|today|yesterday)"
concrete_day="(1st|2nd|[0-9]+(th)?)"
year="(201[7-9])"

pattern=".*?".join([concrete_day, month, year + "?"])
date_regex=re.compile(pattern)
time_regex=re.compile("[0-9]+ o clock")
regexs=[date_regex, time_regex]

def findMatches(regex, sentence):
    global regexs
    result=[]
    start=0
    while True:
        match=regex.search(sentence, start)
        
        if not match:
            break
        start=match.end()+1
        result.append(match.group())
    return result

        


def findDates(sentence):
    global data_regex
    result=[]
    for date in findMatches(date_regex, sentence):
        try:
            dt = parser.parse(date)
            if dt:
                result.append(dt)
        except ValueError:
            pass
    return result





def findTime(sentence):
    global regexs
    result=[]
    print("A")
    for time in findMatches(time_regex, sentence):
        print("time", time)
        result.append(time)
    return result
