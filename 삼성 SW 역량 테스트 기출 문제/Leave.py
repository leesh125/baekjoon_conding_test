import sys
input = sys.stdin.readline

N = int(input())
consulting = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N+1)

# 역순으로 최댓값 구하기(해당 일자까지의 최대 급여)
for i in range(N-1,-1,-1): 
    if dp[i] == 0: dp[i] = dp[i+1] # 만약 해당 일자의 최대 급여가 0이라면 전에 비교했던 다음날의 최대급여 가져오기
    if i + consulting[i][0] > N: continue # 상담 일자가 퇴사일자보다 길면 넘어가기
    # 해당 일자까지의 최대급여 = max(이어받은 최대급여,해당 일자 급여 + 해당 일자의 상담을 마치고 난 다음의 최대 급여)
    dp[i] = max(dp[i],dp[i + consulting[i][0]] + consulting[i][1]) 
print(dp[0]) # 1일 까지의 최대급여