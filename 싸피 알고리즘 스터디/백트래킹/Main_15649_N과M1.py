import sys
from itertools import permutations
input = sys.stdin.readline

def p(cnt):
    if cnt == M:
        print(*nums)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            nums[cnt] = i+1
            p(cnt+1)
            visited[i] = False
            
def permutation(arr, N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr[:i] + arr[i+1:], N-1):
            result.append([elem] + rest)
    return result

N,M = map(int, input().split())
nums = [0 for _ in range(M)]
visited = [False for _ in range(N)]

# 1번 방법
# p(0)

# 2번 방법
# for perm in permutation(list(range(1,N+1)), M):
#     print(*perm)

# 3번 방법
for perm in permutations(range(1,N+1), M):
    print(*perm)