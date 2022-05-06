import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n # 동전에 값어치
d = [0] * (k + 1) # 0~원하는 값어치 돈 만드는 경우의 수
for i in range(n):
    coins[i] = int(input())
coins.sort()  

for i in range(n): # 코인 값어치 만큼
    for j in range(1, k + 1): # 1원부터 원하는 값어치 숫자까지
        if j == coins[i]: # 해당 값어치가 코인의 값어치와 같다면 +1
            d[j] += 1
        elif j > coins[i]: # 해당 값어치가 코인의 값어치보다 크다면
            d[j] += d[j - coins[i]] # 해당 값어치 = 해당 값어치 + 현재 코인 만큼 뺀 값어치의 경우의 수

print(d[-1])
