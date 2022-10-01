from itertools import combinations

# n,m = map(int, input().split())
# nums = map(str,sorted(list(map(int,input().split()))))
# print('\n'.join(list(map(' '.join, combinations(nums,m)))))

def combination(idx,cnt):
    if cnt == m:
        print(*ans)
        return
    
    for i in range(idx, n):
        ans[cnt] = nums[i]
        combination(i+1,cnt+1)

def combination2(arr,N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination2(arr[i+1:], N-1):
            result.append([elem] + rest)
    return result

n,m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * m

# combination(0,0)
for combi in combination2(nums, m):
    print(*combi)