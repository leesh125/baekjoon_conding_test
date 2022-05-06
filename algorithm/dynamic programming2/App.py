import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
total = sum(costs)  # 비용의 총합
result = total  # 최소 비용을 담을 변수

# 해당 앱들의 종료 최소비용의 메모리 합
dp = [[0] * (total + 1) for _ in range(n + 1)]

for i in range(1, n + 1):  # 앱들
    for j in range(1, total + 1):  # 최대 비용까지
        if j < costs[i - 1]:  # 현재 비용이 현재 앱을 종료 시킬만큼의 비용이 아니라면
            dp[i][j] = dp[i - 1][j]  # 이전 최댓값 그대로 적용
        else:
            # 이전 최댓값 or 이전 현재비용-현재 앱의 비용 + 종료하고자하는 지금 앱의 메모리
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + memories[i - 1])

        if dp[i][j] >= m:  # 조건 충족 시
            result = min(result, j)  # 최소비용 결과 갱신
print(result)
