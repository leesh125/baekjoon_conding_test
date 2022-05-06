import sys

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
question = [list(map(int, input().split())) for _ in range(M)]
d = [[0] * N for _ in range(N)]  #  각 인덱스 시작점 ~ 끝점으로 잡고 해당 수열이 펠린드롬 인지 검사

for i in range(N):
    d[i][i] = 1  # 자기 자신은 팰린드롬(ex.1인덱스 ~ 1인덱스)

for i in range(N - 1):
    if arr[i] == arr[i + 1]:  # 차이가 1 나는 인덱스는 깉디먄 펠린드롬
        d[i][i + 1] = 1

for diagonal in range(2, N):  # 대각선
    for i in range(0, N - diagonal):  # 행
        j = i + diagonal  # 열

        # 현재 인덱스 + 1 , 마지막 인덱스 - 1 이 펠린드롬 이면서 시작점, 끝점의 숫자가 같다면
        if d[i + 1][j - 1] == 1 and arr[i] == arr[j]:
            d[i][j] = 1  # 펠린드롬


for i in range(M):
    print(d[question[i][0] - 1][question[i][1] - 1])
