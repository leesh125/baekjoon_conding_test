from sys import stdin


def knapsack(n, k, weights, values):
    d = [[0 for i in range(k + 1)] for i in range(n + 1)]  # 보석값의 누적값 dp
    for i in range(n + 1):
        for j in range(k + 1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif weights[i - 1] <= j:  # 현재 보석의 무게가 배낭무게보다 가볍다면
                # 현재 배낭에 이전 누적값 : 현재 보석 값 + 현재 보석 넣기전 최댓값 비교
                d[i][j] = max(d[i - 1][j], values[i - 1] + d[i - 1][j - weights[i - 1]])
            else:
                d[i][j] = d[i - 1][j]
    return d[-1][-1]


n, k = map(int, stdin.readline().split())
weights = []  # 보석의 무게들
values = []  # 보석의 가치들

for _ in range(n):
    w, v = map(int, stdin.readline().split())
    weights.append(w)
    values.append(v)
print(knapsack(n, k, weights, values))


# Good explanation
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (k + 1)  # 배낭 무게 한도 (ex. 7까지)
ary.sort()
for weight, val in ary:  # 각 보석의 무게와 값어치
    for j in range(k, weight - 1, -1):  # 배낭 무게 max부터 현재 무게까지(-1)
        # 현재 배낭무게의 최대 값어치 = 현재 배낭 무게의 값어치 누적 : 해당 무게만큼 뺀 배낭 무게의 값어치 누적 + 현재 보석 값어치
        dp[j] = max(dp[j], dp[j - weight] + val)

print(dp[k])
