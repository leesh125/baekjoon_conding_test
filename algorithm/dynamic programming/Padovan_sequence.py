import sys

d = [0] * 101
for i in range(1, 4):
    d[i] = 1  # 파도반 수열 1~3 번째까진 1


def padovan(n):
    if n <= 3:
        return 1
    for i in range(4, n + 1):
        d[i] = d[i - 2] + d[i - 3]  # 파도반 수열 규칙 적용
    return d[n]


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(padovan(n))
