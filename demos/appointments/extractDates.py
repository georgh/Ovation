import re
from dateutil import parser

month="(january|february|march|arpil|may|june|july|august|september|october|november|december)"
day="(monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow|today|yesterday)"
concrete_day="(1st|2nd|[0-9]+(th)?)"
year="(201[7-9])"

pattern=".*?".join([concrete_day, month, year + "?"])
date_regex=re.compile(pattern)
time_regex1=re.compile("(after|before)? ([0-9]+) o'? ?clock")
time_regex2=re.compile("() ([0-9]+) hours")
time_regex3=re.compile("(after|before) ([0-9]+)")

def findMatches(regex, sentence):
    global regexs
    result=[]
    start=0
    while True:
        match=regex.search(sentence, start)
        
        if not match:
            break
        start=match.end()+1
        result.append(match)
    return result

        
def findDates(sentence):
    result=[]
    for date in findMatches(date_regex, sentence):
        try:
            dt = parser.parse(date.group())
            if dt:
                result.append(dt)
        except ValueError:
            pass
    return result


def findTime(sentence):
    result=[]
    
    for time_regex in [time_regex1, time_regex2, time_regex3]:
        for time in findMatches(time_regex, sentence):
            print ("time", time)
            result.append( (time.group(1), int(time.group(2))))
    return result

if __name__ == '__main__':
    print(findTime("5 o clock"))
