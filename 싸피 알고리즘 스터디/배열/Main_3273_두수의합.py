import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
arr = [0] * 2000001
for n in nums:
    arr[n] += 1
K = int(input())
ans = 0

for n in nums:
    if arr[K-n] != 0:
        ans += 1

print(ans//2)