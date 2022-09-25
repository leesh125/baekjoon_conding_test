import sys
from itertools import product
input = sys.stdin.readline

def permutation(arr,N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr, N-1):
            result.append([elem] + rest)
    return result

def perms(cnt):
    if cnt == m:
        print(*nums)
        return
    for i in range(1,n+1):
        nums[cnt] = i
        perms(cnt+1)

n,m = map(int, input().split())

# 1. itertools
# for pro in product(range(1,n+1),repeat=m):
#     print(*pro)

# 2. 파이썬 중복순열
# for p in permutation([i for i in range(1,n+1)], m):
#     print(*p)

# 3. 수업 떄 한거

nums = [0 for _ in range(m)]

perms(0)
