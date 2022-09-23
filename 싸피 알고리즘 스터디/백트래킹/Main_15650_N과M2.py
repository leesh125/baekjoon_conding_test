import sys
from itertools import combinations
input = sys.stdin.readline

def c(idx, cnt):
    if cnt == m:
        print(*ans)
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            ans[cnt] = i+1
            c(i+1,cnt+1)
            visited[i] = False

def combination(arr,N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:],N-1):
            result.append([elem] + rest)
    return result

n,m = map(int, input().split())
ans = [0 for _ in range(m)]
nums = list(range(1,n+1))
visited = [False for _ in range(n)]
# for c in combination(nums,m):
#     print(*c)
for c in combinations(range(1,n+1), m):
    print(*c)
