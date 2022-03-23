import sys

# from collections import deque

sys.setrecursionlimit(10000)  # 재귀 깊이 설정

input = sys.stdin.readline


def dfs(x, y):
    # 도착지까지 가는 경우의 수가 없을 때(0), 그 값을 그대로 리턴할 수 있기에 -1로 확인
    if d[x][y] != -1:
        return d[x][y]

    # 끝점이라면 경우의 수 1 리턴
    if x == n - 1 and y == m - 1:
        return 1

    d[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:  # 범위 초과 안한다면
            if arr[nx][ny] < arr[x][y]:  # 내리막길 이라면
                d[x][y] += dfs(nx, ny)  # 현재 경우의 수 + 반환된 경우의 수
    return d[x][y]  # 출발지(시작점)에서 목적지까지 향한 경우의 수 리턴


# def bfs(arr, x, y):
#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx <= -1 or nx >= n or ny <= -1 or ny >= m:  # 범위 벗어날 경우
#                 continue
#             if arr[nx][ny] >= arr[x][y]:
#                 continue
#             if d[nx][ny] != 0:
#                 queue.append((nx, ny))
#                 d[nx][ny] += 1
#             else:
#                 d[nx][ny] += 1
#     return d[-1][-1]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# print(bfs(arr, 0, 0))
print(dfs(0, 0))
print(d)
