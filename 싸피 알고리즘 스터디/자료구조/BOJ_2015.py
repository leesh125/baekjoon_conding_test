import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (N+1)
dp[0] = 0
ans = 0

for i in range(1,N+1):
    dp[i] = nums[i-1] + dp[i-1]

dict = {}
for i in range(N,-1,-1):
    ans += dict.get(dp[i] + K,0)
    dict[dp[i]] = dict.get(dp[i],0) + 1
print(ans)
# B - A = K
# B = A + K