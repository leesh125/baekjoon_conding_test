import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())  # 행, 열
graph = [list(input().rstrip()) for _ in range(N)]  # 그래프
red_x, red_y, blue_x, blue_y = 0, 0, 0, 0  # 빨간 구슬, 파란 구슬 x,y 좌표

# 구슬 좌표 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == "B":
            blue_x, blue_y = i, j
        elif graph[i][j] == "R":
            red_x, red_y = i, j

# 기울여서 움직이기
def move(x, y, nx, ny):
    count = 0
    # 다음 좌표가 막히지 않은 곳이거나 현재 좌표가 탈출구가 아닐동안
    while graph[x + nx][y + ny] != "#" and graph[x][y] != "O":
        x += nx  # 다음 좌표로 이동
        y += ny
        count += 1  # 몇 칸 이동했는지
    return x, y, count  # 끝에 도달하거나, 탈출구인 것의 x,y 좌표와 거기까지 가는데에 거리


# bfs 탐색
def bfs(red_x, red_y, blue_x, blue_y, res):
    q = deque()
    q.append((red_x, red_y, blue_x, blue_y, res))  # 큐에 구슬들의 좌표와 누적 이동 수 추가
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:  # 큐 있을동안
        red_x, red_y, blue_x, blue_y, res = q.popleft()  # 구슬들의 좌표와 누적 이동 수 꺼내기

        if res > 10:  # 누적 수가 10 넘으면 -1
            return -1
        for i in range(4):  # 위,아래,오른쪽,왼쪽 기울이기
            next_red_x, next_red_y, red_count = move(
                red_x, red_y, dx[i], dy[i]
            )  # 빨간 구슬 기울인 후 좌표
            next_blue_x, next_blue_y, blue_count = move(
                blue_x, blue_y, dx[i], dy[i]
            )  # 파란 구슬 기울인 후 좌표

            if (  # 둘 다 같은 곳에 도달하고 탈출하지 않았다면
                next_red_x == next_blue_x
                and next_red_y == next_blue_y
                and graph[next_red_x][next_red_y] != "O"
            ):
                if red_count > blue_count:  # 빨간 count가 더 많으면(빨간 좌표가 파란 좌표보다 뒤에서 시작한 것)
                    next_red_x -= dx[i]  # 빨간 좌표를 이동한 것에서 -1
                    next_red_y -= dy[i]
                else:  # 파란 구슬 경우
                    next_blue_x -= dx[i]
                    next_blue_y -= dy[i]
            if (  # 둘 다 안빠졌을 때
                graph[next_red_x][next_red_y] != "O"
                and graph[next_blue_x][next_blue_y] != "O"
            ):  # q에 추가(누적 수 증가시켜서)
                q.append((next_red_x, next_red_y, next_blue_x, next_blue_y, res + 1))
            elif (  # 빨간 좌표만 빠졌을 때
                graph[next_red_x][next_red_y] == "O"
                and graph[next_blue_x][next_blue_y] != "O"
            ):
                return res + 1  # 이동한 거 +1(한 번 더 기울인거기 때문에)


# 10을 넘으면 -1 아니면 누적 수 반환
print(-1) if bfs(red_x, red_y, blue_x, blue_y, 0) > 10 else print(
    bfs(red_x, red_y, blue_x, blue_y, 0)
)
