import sys

n = int(sys.stdin.readline())
tri = []
dp = []

for i in range(1, n + 1):
    tri.append(list(map(int, sys.stdin.readline().split()))) # 삼각형을 표현할 2차원 배열 입력받기
    dp.append([0 for _ in range(i)]) # 비용을 기록할 대응 삼각형

dp[0][0] = tri[0][0]
if n != 1: # 삼각형이 아닌 하나의 숫자가 들어오면 그대로 출력을 해야함
    dp[1][0] = tri[1][0] + dp[0][0]
    dp[1][1] = tri[1][1] + dp[0][0]

for i in range(2, n):
    dp[i][0] = dp[i - 1][0] + tri[i][0] # 맨 왼쪽 최대값은 항상 이전값 더하기 지금값
    dp[i][-1] = dp[i - 1][-1] + tri[i][-1] # 맨 오른쪽 최대값은 항상 이전값 더하기 지금값
    for j in range(1, i):
        dp[i][j] = tri[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j]) # 현재 비용 + max(이전 행 왼쪽 대각선, 이전 행 오른쪽 대각선)
print(max(dp[-1]))
