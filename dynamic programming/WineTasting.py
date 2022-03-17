from sys import stdin

n = int(stdin.readline())
wine = [0]
for _ in range(n):
    wine.append(int(stdin.readline()))
dp = [0] * 10001  # 해당 인덱스 당 최대 포도주 시음 수

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
else:
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]  # 2인덱스의 최대 시음수는 1,2 인덱스의 합

    for i in range(3, n + 1):
        # 현재 포도주 + -2인덱스 누적 포도주 : 현재 포도주 + 이전 포도주 + -3 인덱스 포도주 : -1 인덱스 포도주
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1])

    print(dp[n])
