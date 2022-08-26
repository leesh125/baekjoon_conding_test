import sys
from collections import deque
input = sys.stdin.readline

def move(x,y,d):
    cnt = 0
    while graph[x+dir[d][0]][y+dir[d][1]] != '#' and graph[x][y] != 'O':
        cnt += 1
        x += dir[d][0]
        y += dir[d][1]
    return x, y, cnt

def bfs(red, blue):
    redX, redY = red
    blueX, blueY = blue
    q = deque()
    q.append((redX, redY, blueX, blueY,0))

    while q:
        now_redX, now_redY, now_blueX, now_blueY, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            next_redX, next_redY, red_cnt = move(now_redX, now_redY,i)
            next_blueX, next_blueY, blue_cnt = move(now_blueX, now_blueY,i)
            
            if (next_blueX == next_redX and next_redY == next_blueY and # 같은 곳에 도달
                graph[next_blueX][next_blueY] != 'O'): # 구멍이 아니라면 
                if red_cnt > blue_cnt:
                    next_redX -= dir[i][0]
                    next_redY -= dir[i][1]
                else:
                    next_blueX -= dir[i][0]
                    next_blueY -= dir[i][1]
            if graph[next_blueX][next_blueY] != 'O':
                if graph[next_redX][next_redY] != 'O':
                    q.append((next_redX,next_redY,next_blueX,next_blueY,cnt+1))
                else:
                    return cnt+1

N,M = map(int, input().split())
graph = []
blue,red = (),()
dir = [(-1,0),(1,0),(0,1),(0,-1)]
ans = 0

for i in range(N):
    temp = list(input().rstrip())
    graph.append(temp)
    for j in range(M):
        if temp[j] == 'B':
            blue = (i,j)
        elif temp[j] == 'R':
            red = (i,j)

print(bfs(red, blue))
