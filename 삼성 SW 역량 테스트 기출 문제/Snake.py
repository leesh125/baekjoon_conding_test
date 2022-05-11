import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
q = deque() # 시간, 방향전환을 담을 큐

K = int(input()) # 사과갯수
for i in range(K):
    row, col = map(int, input().split()) # 사과 위치
    graph[row - 1][col - 1] = 2  # 사과는 2로 표시(1행 1열이 기본이므로 0행 0열로 맞춰줌)
graph[0][0] = 1 # 첫번째부터 시작 (1은 뱀이 있는 위치)

L = int(input()) # 정보 갯수
for i in range(L):
    time, dir = input().split() # 몇초 후 방향전환, 방향
    q.append([int(time), dir])  # 방향전환 정보 q에 담기

dx = [-1, 0, 1, 0]  # 위, 오른, 아래, 왼
dy = [0, 1, 0, -1]
direction = 1  # 처음 에는 오른쪽 이동
head_x, head_y, tail_x, tail_y = 0, 0, 0, 0  # 현재 좌표
repeat = 0 # 몇초 진행중인지 확인할 변수
snake = deque() # 뱀이 어느 좌표에 있는지
snake.append((0, 0)) # (0,0)부터 시작

while True:  # 벽 또는 자기 자신과 부딪히면 끝
    if q: # 방향, 시간 관련 정보가 있을 때
        if q[0][0] == repeat: # 해당 시간이 지났으면
            time, dir = q.popleft() # 시간, 방향
            if dir == "L": # L이면 왼쪽으로 꺾음
                if direction == 0: # 방향 리스트에 처음 이전으로 가려고하면
                    direction = 4 # 끝으로 가게끔
                direction -= 1 # d의 왼쪽이 방향이 됨
            elif dir == "D": # D이면 오른쪽으로 꺾음
                if direction == 3: # 방향 리스트에 마지막 이후로 가려고하면
                    direction = -1 # 처음으로 가게끔
                direction += 1 # d의 오른쪽이 방향이 됨
    # 방향에 따라 뱀의 대가리를 이동시킬것
    head_x += dx[direction] 
    head_y += dy[direction]

    # 범위 초과 or 뱀이 자기 몸을 박았다면 빠져나오기
    if (head_x < 0 or head_x >= N or head_y < 0 or head_y >= N or graph[head_x][head_y] == 1):
        break

    snake.append((head_x, head_y)) # 뱀에 머리 부분 snake queue에 추가

    if graph[head_x][head_y] == 2:  # 사과면
        graph[head_x][head_y] = 1  # 사과 먹음(동시에 몸 길이 늘림)
    elif graph[head_x][head_y] == 0: # 사과 없다면
        graph[head_x][head_y] = 1 # 뱀을 이동시키고
        remove_x, remove_y = snake.popleft() # 뱀의 꼬리 부분을
        graph[remove_x][remove_y] = 0 # 빈칸으로(이동시킴)

    repeat += 1 # 초 증가
print(repeat + 1) # 다음 초에 박기때문 