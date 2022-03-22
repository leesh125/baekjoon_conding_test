import sys

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for diagonal in range(1, n):  # 0,0 1,1 등 자기 자신 행렬 제외
    for i in range(0, n - diagonal):  # 대각선 우측 한 칸씩 이동
        j = i + diagonal  # 현재 대각선에서 몇 번째 원소인지

        if diagonal == 1:  # 차이가 1밖에 나지 않는 칸
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue

        dp[i][j] = float("inf")

        # 두 칸 이상 차이 날 때
        for k in range(i, j):  # 각 부분으로 나눠보기(ex.(0,2) -> (0,0)+(1,2) or (0,1)+(2,2))
            dp[i][j] = min(
                dp[i][j],
                # (배열1부터 배열k까지 곱셈 횟수) + (배열k+1부터 배열N까지 곱셈 횟수) + (두 행렬의 곱셈 횟수)
                dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1],
            )

print(dp[0][n - 1])
