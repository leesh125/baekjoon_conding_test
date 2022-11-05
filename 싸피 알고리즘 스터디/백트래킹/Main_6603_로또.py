import sys
input = sys.stdin.readline

def combination(arr, N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:], N-1):
            result.append([elem] + rest)
    return result

while True:
    nums = sorted(list(map(int,input().split()))[1:])
    if len(nums) == 0:
        break
    for combi in combination(nums, 6):
        print(*combi)
    print()