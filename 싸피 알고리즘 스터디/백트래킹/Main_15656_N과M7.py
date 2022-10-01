from itertools import product

def dup_permutation(cnt):
    if cnt == m:
        print(*ans)
        return
    
    for i in range(n):
        ans[cnt] = nums[i]
        dup_permutation(cnt+1)

def dup_permutation2(arr, N):
    result = []

    if N == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in dup_permutation2(arr, N-1):
            result.append([elem] + rest)
    return result

n,m = map(int, input().split())
nums = sorted(list(map(int,input().split())))
ans = [0] * m

# for pro in product(nums,repeat=m):
#     print(*pro)

# dup_permutation(0)
for perm in dup_permutation2(nums,m):
    print(*perm)