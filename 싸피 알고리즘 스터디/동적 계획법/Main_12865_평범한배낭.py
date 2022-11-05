import sys
input = sys.stdin.readline

N,K = map(int,input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
info = [list(map(int,input().split())) for _ in range(N)]

for i in range(N+1):
    if i == 0: continue
    for j in range(K+1):
        if info[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-info[i-1][0]] + info[i-1][1])
print(dp[-1][-1])
