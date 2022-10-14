from collections import defaultdict
from copy import deepcopy
import sys
input = sys.stdin.readline
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def fish(dic,fishes,directions,sharkX,sharkY):
    for i in range(1,17):
        if i not in dic:
            continue
        x,y = dic[i]
        dir = directions[x][y]

        for _ in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or (nx == sharkX and ny == sharkY):
                dir = (dir + 1) % 8
                continue    
            
            dic[i] = [nx,ny]
            if fishes[nx][ny] != 0:
                dic[fishes[nx][ny]] = [x,y]
            
            if fishes[nx][ny] == 0:
                directions[nx][ny] = dir
                directions[x][y] = -1
            else:
                directions[x][y] = directions[nx][ny] 
                directions[nx][ny] = dir
            fishes[x][y], fishes[nx][ny] = fishes[nx][ny],fishes[x][y]
            
            break

    return dic, fishes, directions

def dfs2(sharkX,sharkY,eat,dic,fishes,directions):
    global ans
    temp_dic = deepcopy(dic)
    temp_fishes = deepcopy(fishes)
    temp_directions = deepcopy(directions)
    # temp_directions[sharkX][sharkY] = -1

    n_eat = eat + temp_fishes[sharkX][sharkY]
    ans = max(ans, n_eat)
    del temp_dic[fishes[sharkX][sharkY]]
    temp_fishes[sharkX][sharkY] = 0
    shark_dir = temp_directions[sharkX][sharkY]
    
    n_dic, n_fishes, n_direction = fish(temp_dic,temp_fishes,temp_directions,sharkX,sharkY)
    

    x = sharkX; y = sharkY
    while True:
        x += dx[shark_dir]
        y += dy[shark_dir]
        if 0 > x or x >= 4 or 0 > y or y >= 4:
            break
        if n_fishes[x][y] != 0:
            dfs2(x,y,n_eat,n_dic, n_fishes, n_direction)


fishes = [[0] * 4 for _ in range(4)]
directions = [[0] * 4 for _ in range(4)]
dic = defaultdict(list)
ans = 0
eat = 0

for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(0,7,2):
        fishes[i][j//2] = temp[j]
        dic[temp[j]].append(i)
        dic[temp[j]].append(j//2)
    for j in range(1,8,2):
        directions[i][j//2] = temp[j]-1

# sharkX,sharkY = [0,0]

dfs2(0,0,eat,dic,fishes,directions)
print(ans)
