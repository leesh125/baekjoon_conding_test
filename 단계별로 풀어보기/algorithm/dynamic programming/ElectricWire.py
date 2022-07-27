from sys import stdin

n = int(stdin.readline())
e = []
d = [1] * n

for i in range(n):
    e.append(list(map(int, stdin.readline().split())))

e.sort()  # 첫 전봇대 기준으로 정렬(뒤 전봇대 가장 긴 수열 길이 구하기 위해)

for i in range(1, n):
    for j in range(i):
        if e[i][1] > e[j][1]:  # 겹치지 않으면
            d[i] = max(d[i], d[j] + 1)  # 최대 설치 가능 전봇대 수 갱신

print(n - max(d))  # 총 전봇대 줄 - 최대 설치 가능 전봇대 수
