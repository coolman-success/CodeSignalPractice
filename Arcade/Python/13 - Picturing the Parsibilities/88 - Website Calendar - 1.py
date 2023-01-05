import calendar

def solution(month, year):
    cal = calendar.HTMLCalendar(0)
    tbl = cal.formatmonth(year, month)
    return tbl.replace("\n", "")
