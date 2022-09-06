hour, minute = map(int,input().split())
add_minute = int(input())
n_hour, n_minute = (hour + (minute + add_minute) // 60)%24 , (minute + add_minute) % 60
print(n_hour, n_minute)
