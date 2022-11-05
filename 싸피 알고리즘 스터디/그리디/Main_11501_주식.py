import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    ans = 0
    max_num = nums[-1]
    for i in range(N-2,-1,-1):
        if max_num > nums[i]: ans += max_num - nums[i]
        else:max_num = nums[i]
    print(ans)