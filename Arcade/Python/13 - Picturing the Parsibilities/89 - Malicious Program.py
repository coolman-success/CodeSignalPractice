import datetime

def solution(curDate, changes):
    obj = datetime.datetime.strptime(curDate, "%d %b %Y %H:%M:%S")
    try:
        newDate = datetime.datetime(obj.year + changes[2],
                                obj.month + changes[1],
                                obj.day + changes[0],
                                obj.hour + changes[3],
                                obj.minute + changes[4],
                                obj.second + changes[5])
        return newDate.strftime(newDate, "%d %b %Y %H:%M:%S")
    except ValueError:
        return curDate
