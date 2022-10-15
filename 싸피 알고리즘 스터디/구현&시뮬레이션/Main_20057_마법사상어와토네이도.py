import sys
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def move_sand(x,y,dir):
    global ans
    temp_ans = 0
    origin_sand = graph[x][y]
    sand = origin_sand
    graph[x][y] = 0
    if dir == 0: # 좌
        nx = x - 1
        temp = int(origin_sand * 0.07)
        if nx >= 0:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1
        if nx < N:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.01)
        nx = x - 1; ny = y + 1
        if nx >= 0 and ny < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1; ny = y + 1
        if ny < N and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.1)
        nx = x - 1; ny = y - 1
        if ny >= 0 and nx >= 0:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1; ny = y - 1
        if ny >= 0 and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.02)
        nx = x - 2
        if nx >= 0:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 2
        if nx < N:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.05)
        ny = y - 2
        if ny >= 0:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        if y - 1 >= 0:
            sand -= temp_ans
            graph[x][y-1] += sand
        else:
            ans += (sand-temp_ans)
    elif dir == 1: # 아래
        ny = y - 1
        temp = int(origin_sand * 0.07)
        if ny >= 0:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        ny = y + 1
        if ny < N:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.01)
        nx = x - 1; ny = y + 1
        if nx >= 0 and ny < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x - 1; ny = y - 1
        if ny >= 0 and nx >= 0:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.1)
        nx = x + 1; ny = y - 1
        if ny >= 0 and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1; ny = y + 1
        if ny < N and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.02)
        ny = y - 2
        if ny >= 0:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        ny = y + 2
        if ny < N:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.05)
        nx = x + 2
        if nx < N:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        if x + 1 < N:
            sand -= temp_ans
            graph[x+1][y] += sand
        else:
            ans += (sand-temp_ans)
    elif dir == 2: # 우
        nx = x - 1
        temp = int(origin_sand * 0.07)
        if nx >= 0:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1
        if nx < N:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.1)
        nx = x - 1; ny = y + 1
        if nx >= 0 and ny < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1; ny = y + 1
        if ny < N and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.01)
        nx = x - 1; ny = y - 1
        if ny >= 0 and nx >= 0:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1; ny = y - 1
        if ny >= 0 and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.02)
        nx = x - 2
        if nx >= 0:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 2
        if nx < N:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.05)
        ny = y + 2
        if ny < N:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        if y + 1 < N:
            sand -= temp_ans
            graph[x][y+1] += sand
        else:
            ans += (sand-temp_ans)
    elif dir == 3: # 위
        ny = y - 1
        temp = int(origin_sand * 0.07)
        if ny >= 0:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        ny = y + 1
        if ny < N:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.1)
        nx = x - 1; ny = y + 1
        if nx >= 0 and ny < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x - 1; ny = y - 1
        if ny >= 0 and nx >= 0:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.01)
        nx = x + 1; ny = y - 1
        if ny >= 0 and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        nx = x + 1; ny = y + 1
        if ny < N and nx < N:
            graph[nx][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.02)
        ny = y - 2
        if ny >= 0:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        ny = y + 2
        if ny < N:
            graph[x][ny] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp
        temp = int(origin_sand * 0.05)
        nx = x - 2
        if nx >= 0:
            graph[nx][y] += temp
            sand -= temp
        else:
            temp_ans += temp
            ans += temp

        if x - 1 >= 0:
            sand -= temp_ans
            graph[x-1][y] += sand
        else:
            ans += (sand-temp_ans)


def tornado():
    r, idx = 1, 0
    nx = x; ny = y
    while True:
        for _ in range(2):
            for _ in range(r):
                nx += dx[idx]
                ny += dy[idx]

                move_sand(nx,ny,idx) # 모래 옮기기

                if nx == 0 and ny == 0:
                    return

            idx = (idx + 1) % 4
        r += 1

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
standard = N // 2
x = standard; y=standard
ans = 0

tornado()
print(ans)