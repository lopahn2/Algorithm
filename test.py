def solution(a, b):
    dayOfTheWeek = [FRI,SAT,SUN,MON,TUE,WED,THU]
    monthDay = {
        1:31,
        2:29,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:30
    }
    month = 1
    day = 1
    idx = 0
    i = 0
    while True:
        if month != a:
            day += 1
            if day > monthDay[month]:
                month +=1
                day = 1
            idx += 1
            continue
        if month == a:
            if day == b:
                return dayOfTheWeek[idx % 7]
            else:
                day += 1
                idx += 1
    return 'fail'
    
    
    