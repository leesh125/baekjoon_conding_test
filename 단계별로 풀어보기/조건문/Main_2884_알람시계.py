hour, minute = map(int, input().split())
alarm_minute = minute - 45

if alarm_minute >= 0:
    print(hour, alarm_minute)
else:
    if hour == 0:
        print(23, 60+alarm_minute)
    else:
        print(hour-1,60+alarm_minute)