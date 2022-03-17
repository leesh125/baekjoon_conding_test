from sys import stdin

dp = [0] * 1000001  # 각 숫자(=인덱스)마다 1을 만들기 위한 최소비용

n = int(stdin.readline())

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 해당 숫자에서 1을 뺐을 경우
    if i % 2 == 0:  # 해당 숫자가 2로 나눠지면
        dp[i] = min(dp[i // 2] + 1, dp[i])  # 2로 나눈 숫자의 1로가기위한 최소비용 +1 : 현재의 최소비용
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
print(dp[n])
