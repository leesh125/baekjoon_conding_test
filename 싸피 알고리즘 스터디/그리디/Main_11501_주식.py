import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    ans = 0
    dp = [0] * N

    max_num = nums[-1]
    
    for i in range(N-2,-1,-1):
        
        if max_num > nums[i]:
            dp[i] = max_num - nums[i]
        else:
            max_num = nums[i]
        
    print(sum(dp))