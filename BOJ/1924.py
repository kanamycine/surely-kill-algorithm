month_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
month, day = map(int, input().split())
day_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']

if month != 1:
    diff_month = month - 1
    diff_day = 0
    for i in range(1, diff_month+1):
        diff_day += month_day[i]
    diff_day += day
    daily = diff_day % 7
    print(day_list[daily])
elif month == 1:
    Jan_daily = day % 7
    print(day_list[Jan_daily])

