import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    k = int(input())
    page = list(map(int, input().split()))

    dp = [[0] * k for _ in range(k)]  # 누적 합을 나타낼 배열
    for i in range(k - 1):
        dp[i][i + 1] = page[i] + page[i + 1]  # 0~1, 1~2 파일 크기 누적 합(임시)
        for j in range(i + 2, k):  # 0~2, 0~3, 1~3 파일 크기 누적 합(임시)
            dp[i][j] = dp[i][j - 1] + page[j]

    for d in range(2, k):  # 대각선
        for i in range(k - d):
            j = i + d  # 0~2 = (0,0) + (1,2), (0,1) + (2,2)
            minimum = [dp[i][k] + dp[k + 1][j] for k in range(i, j)]
            dp[i][j] += min(minimum)  # 누적값을 더할 최솟값

    print(dp[0][k - 1])
