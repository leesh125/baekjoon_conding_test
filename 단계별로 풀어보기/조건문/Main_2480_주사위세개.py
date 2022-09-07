numbers = [0] * 7
temp = 0
for n in map(int, input().split()):
    numbers[n] += 1
    if n > temp:
        temp = n
max_num = max(numbers)

if max_num == 3:
    print(numbers.index(3) * 1000 + 10000)
elif max_num == 2:
    print(numbers.index(2) * 100 + 1000)
else:
    print(temp*100)

