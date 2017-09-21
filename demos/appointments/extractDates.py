import re

month="(january|february|march|arpil|may|june|july|august|september|october|november|december)"
day="(monday|tuesday|wednesday|thursday|friday|saturday|sunday|tomorrow|today|yesterday)"
concrete_day="(1st|2nd|[0-9]+(th)?)"
year="(201[7-9])"

pattern = ".*".join([concrete_day, month, year + "?"])
regex=re.compile(pattern)


def findDates(sentence):
    global regex
    print("findDates")
    result=[]
    start=0
    while True:
        match = regex.match(sentence, start)
        print("match", match);
                      
        if not match:
            break
        start=match.end()+1
        result.append(match.group())
    return result


print(regex.match("abc 1st october xxx"))
