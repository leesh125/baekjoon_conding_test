# My turn
import sys


def cost(n):
    for i in range(1, n):
        for j in range(3):  # 각 열의 값 비교를 위해(r,g,b)
            d[i][j] = min(
                d[i - 1][j - 1] + rgb[i][j], d[i - 1][j - 2] + rgb[i][j]
            )  # 이전항과 현재값 더한것의 최솟값
    return min(d[-1])  # 마지막 행 최솟값


n = int(sys.stdin.readline())
d = [0] * 1001
rgb = []
d = []

for i in range(n):
    rgb.append(list(map(int, sys.stdin.readline().split())))
    if i == 0:
        d.append(rgb[i])
    else:
        d.append([0, 0, 0])

print(cost(n))

# Good Explanation
import sys

R, G, B = 0, 0, 0
for i in range(int(sys.stdin.readline())):
    r, g, b = map(int, sys.stdin.readline().rstrip().split())
    # 중첩하여 비용 증가
    r += min(G, B)
    g += min(R, B)
    b += min(R, G)
    R, G, B = r, g, b  # 해당 비용을 다음 계산에 사용
print(min(R, G, B))
