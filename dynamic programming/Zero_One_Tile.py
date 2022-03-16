# My turn
import sys


def tile(x):
    if x <= 3:
        return x
    for i in range(4, len(d)):
        d[i] = d[i - 1] + d[i - 2]
        if d[i] >= 15746:  # 분배법칙에 의해 15746을 넘긴 수는 나머지 값으로 계산가능
            d[i] %= 15746
    return d[x]


n = int(sys.stdin.readline())
d = [0] * (n + 1)
if n >= 4:
    for i in range(1, 4):
        d[i] = i  # 1,2,3 자리 숫자를 만드는건 타일 순서와 똑같음

print(tile(n))

# Good Explanation
n = int(input())

a = 0
b = 1

for _ in range(n):
    a, b = b, (a + b) % 15746  # 수열의 규칙을 잘 이용한 예

print(b)
