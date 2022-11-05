import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
dp = [0] * N
dp[0] = nums[0]
ans = dp[0]

for i in range(1,N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], nums[i]+dp[j])
    ans = max(ans,dp[i])

print(ans)