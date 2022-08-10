from copy import deepcopy
import sys
from itertools import permutations
input = sys.stdin.readline

def getCircle(start,start_x,start_y,end_x,end_y,new_graph):
    circle = []
    for j in range(start+start_y,end_y-start):
        circle.append(new_graph[start_x+start][j])
    for i in range(start+start_x,end_x-start):
        circle.append(new_graph[i][end_y-start])
    for j in range(end_y-start, start_y+start,-1):
        circle.append(new_graph[end_x-start][j])
    for i in range(end_x-start, start_x+start,-1):
        circle.append(new_graph[i][start_y+start])

    return circle
    
def match(circle,new_graph):
    idx = 0

    for j in range(start+start_y,end_y-start):
        new_graph[start_x+start][j] = circle[idx]
        idx += 1
    for i in range(start+start_x,end_x-start):
        new_graph[i][end_y-start] = circle[idx]
        idx += 1
    for j in range(end_y-start, start_y+start,-1):
        new_graph[end_x-start][j] = circle[idx]
        idx += 1
    for i in range(end_x-start, start_x+start,-1):
        new_graph[i][start_y+start] = circle[idx]
        idx += 1
    
def rotate(start,start_x,start_y,end_x,end_y,new_graph):
    circle = getCircle(start,start_x,start_y,end_x,end_y,new_graph)
    circle = circle[-1:] + circle[:-1]
    match(circle,new_graph)

N, M, cnt = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
cnt_list = []
ans = int(1e9)
for _ in range(cnt):
    a,b,c = map(int, input().split())
    cnt_list.append([a-c-1,b-c-1,a+c-1,b+c-1])

for li in list(permutations(range(cnt),cnt)):
    new_graph = deepcopy(graph)
    for l in li:
        start_x,start_y,end_x,end_y = cnt_list[l][0],cnt_list[l][1],cnt_list[l][2],cnt_list[l][3]
        for start in range(min(N,M)//2):
            rotate(start,start_x,start_y,end_x,end_y,new_graph)
    for g in new_graph:
        total = 0
        total += sum(g)
        ans = min(ans, total)
print(ans)