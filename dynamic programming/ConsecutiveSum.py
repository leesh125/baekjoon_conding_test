from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
d = [-1000] * n
d[0] = arr[0]

for i in range(1, n): 
    d[i] = max(arr[i], arr[i] + d[i - 1]) # 현재 값 or 현재 값 + 누적값

print(max(d)) # 가장 큰 합을 구함
