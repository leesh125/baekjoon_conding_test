# My turn
# 계수 정렬 
import sys
n = int(sys.stdin.readline())
count = [0] * 10001 # 숫자를 count 할 배열

for i in range(n):
    count[int(sys.stdin.readline())] += 1 # 입력 받은 숫자를 인덱스로 하여 count +1

for i in range(10001):
    for j in range(count[i]): #count 만큼 
        print(i) # 현재 숫자 출력

# Good explanation
