from itertools import combinations_with_replacement

def combination(idx,cnt):
    if cnt == m:
        print(*nums)
        return

    for i in range(idx,n):
        nums[cnt] = i + 1
        combination(i,cnt+1)

def combination2(arr,N):
    result = []

    if N == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination2(arr[i:], N-1):
            result.append([elem] + rest)
    return result

n,m = map(int, input().split())
visited = [False] * n
nums = [0] * m
# combination(0,0)

# for combi in combinations_with_replacement(range(1,n+1),m):
#     print(*combi)

for combi in combination2(list(range(1,n+1)), m):
    print(*combi)
