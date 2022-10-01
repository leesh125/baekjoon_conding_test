# from itertools import combinations_with_replacement

# n,m = map(int, input().split())
# nums = map(str,sorted(map(int, input().split())))
# print('\n'.join(map(' '.join,combinations_with_replacement(nums,m))))

def dup_combination(idx,cnt):
    if cnt == m:
        print(*ans)
        return
    
    for i in range(idx, n):
        ans[cnt] = nums[i]
        dup_combination(i,cnt+1)

def dup_combination2(arr, N):
    result = []

    if N == 0: return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in dup_combination2(arr[i:],N-1):
            result.append([elem] + rest)
    return result

n,m = map(int, input().split())
nums = sorted(list(map(int,input().split())))
ans = [0] * m
# dup_combination(0,0)

for combi in dup_combination2(nums, m):
    print(*combi)