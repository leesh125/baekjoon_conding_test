import sys
from itertools import permutations
input = sys.stdin.readline

def permutation(cnt):
    if cnt == m:
        print(*ans)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans[cnt] = nums[i]
            permutation(cnt+1)
            visited[i] = False

def permutation2(arr,N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation2(arr[:i] + arr[i+1:], N-1):
            result.append([elem] + rest)
    return result

n,m = map(int, input().split())
nums = sorted(list(map(int,input().split())))
ans = [0] * m
visited = [False] * n

# permutation(0)
# for perm in permutation2(nums,m):
#     print(*perm)

for perm in permutations(nums, m):
    print(*perm)