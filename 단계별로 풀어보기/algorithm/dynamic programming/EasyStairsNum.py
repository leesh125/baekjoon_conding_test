from sys import stdin

n = int(stdin.readline())
# 행: 자릿수, 열: 0~9의 숫자(계단수를 저장하기 위한 리스트)
dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1  # 1행은 0빼고 모두 하나의 계단수

for i in range(2, n + 1):  # 2행부터
    for j in range(10):  # 0 ~ 9 대입해보기
        if j == 0:  # 0이라면 이전행의 -1 숫자가 없음
            dp[i][j] = dp[i - 1][1]  # 이전 행의 1이라는 숫자가 가지는 계단수의 갯수 그대로 가져옴
        elif j == 9:  # 9라면 이전행의 10 숫자가 없음
            dp[i][j] = dp[i - 1][8]  # 이전 행의 8이라는 숫자가 가지는 계단수의 갯수 그대로 가져옴
        else:  # 이전 행의 -1, +1 숫자가 가지는 계단수 개수
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)
