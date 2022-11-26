import datetime
dateformat = "%Y%m%d"
def countDiffDay(year,month,day,temp_year,temp_month,temp_day):
    start_date = str(year) + str(month) + str(day)
    end_date = str(temp_year) + str(temp_month) + str(temp_day)

    datetime_convert1 = datetime.datetime.strptime(start_date,dateformat)
    datetime_convert2 = datetime.datetime.strptime(end_date,dateformat)

    return (datetime_convert1 - datetime_convert2).days

def solution(s, times):
    isAccount = 1
    
    o_year, o_month, o_day, o_hour, o_minute, o_second = map(int,s.split(':'))
    year, month, day, hour, minute, second = o_year, o_month, o_day, o_hour, o_minute, o_second
    temp_year, temp_month, temp_day = o_year, o_month, o_day

    for time in times:
        t_day,t_hour,t_minute,t_second = map(int,time.split(':'))

        add_second = t_second + second
        if add_second >= 60:
            minute += add_second // 60
            second = add_second % 60
        else:
            second = add_second

        add_minute = t_minute + minute
        if add_minute >= 60:
            hour += add_minute // 60
            minute = add_minute % 60
        else:
            minute = add_minute

        add_hour = t_hour + hour
        if add_hour >= 24:
            day += add_hour // 24
            hour = add_hour % 24
        else:
            hour = add_hour

        add_day = t_day + day
        add_day -= 1
        if add_day >= 30:
            month += add_day // 30
            day = add_day % 30 + 1
        else:
            day = add_day + 1
        
        month -= 1
        if month >= 12:
            year += month // 12
            month = month % 12
        month += 1

        if countDiffDay(year,month,day,temp_year,temp_month,temp_day) > 1:
            isAccount = 0
        temp_year, temp_month, temp_day= year, month, day

    return [isAccount, countDiffDay(year,month,day,o_year,o_month,o_day) + 1]