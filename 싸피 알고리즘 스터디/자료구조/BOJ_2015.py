import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def backTracking(start, total):
    global ans
    if total > K or start == N: return
    if total == K:
        ans += 1
        return
    for i in range(start,N):
        total += nums[i]
        backTracking(i+1, total)

N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(N):
    backTracking(i, 0)

print(ans)