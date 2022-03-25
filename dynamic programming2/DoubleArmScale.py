# My turn
import sys

input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))  # 추의 무게
sum_weight = sum(weight)  # 추의 무게 합(->리스트의 마지막 인덱스)
m = int(input())
marble = list(map(int, input().split()))  # 구슬의 무게

# 0 인덱스 제외(행: 추 무게 리스트,인덱스 , 열: 0~추의 무게 합)
d = [[0] * (sum_weight + 1) for _ in range(n + 1)]

for i in range(1, sum_weight + 1):  # 0 인덱스를 0으로
    d[0][i] = 0

for i in range(1, n + 1):  # 추 무게 리스트 인덱스
    for j in range(1, sum_weight + 1):  # 추 무게 합(0~total 합)
        if weight[i - 1] == j:  # 자기 자신은 표현 가능
            d[i][j] = 1
        elif weight[i - 1] < j:  # 추 무게 합이 현재 추 무게보다 무거우면
            d[i][j] = max(  # 이전 무게가 표현할 수 있는지, 현재 무게 - 현재 추의 무게 and 이전 무게 - 현재 추의 무게
                d[i - 1][j], d[i - 1][j - weight[i - 1]] * d[i][j - weight[i - 1]]
            )
        else:  # 그 외에는 이전 무게가 표현할 수 있는 것과 같음
            d[i][j] = d[i - 1][j]

result = []
length = len(d[-1])  # 추의 무게 최종 합

for i in range(m):
    if length >= marble[i] + 1:  # 추의 무게 최종 합이 현재 구슬의 무게보다 클 때
        if d[-1][marble[i]] == 1:  # 자기 자신의 무게를 표현할 수 있는지
            result.append("Y")  # 그럼 가능
            continue
    if marble[i] > sum_weight:  # 현재 구슬의 무게가 추의 무게 최종 합보다 크면
        result.append("N")  # 표현 불가 그럼 불가능
        continue
    for j in range(sum_weight + 1 - marble[i]):  # 표현할 수 있는 범위 내에서
        # ex)1, 2 의 추는 1의 구슬과 함께 시너지 발동, 1, 4 의 추는 3의 구슬과 함께 시너지 발동
        if d[-1][j] * d[-1][j + marble[i]] == 1:
            result.append("Y")
            break
        if j == sum_weight - marble[i]:
            result.append("N")
print(*result)

# Good Explanation
input()
s = []
for k in map(int, input().split(" ")):
    for i in range(len(s)):  # 추들로 표현할 수 있는 무게를 모두 구함
        s.append(k + s[i])
        s.append(abs(k - s[i]))
    s.append(k)
    s = list(set(s))
input()
for k in map(int, input().split(" ")):
    print("Y" if k in s else "N", end=" ")  # 구슬이 표현 가능한 무게에 포함되면
