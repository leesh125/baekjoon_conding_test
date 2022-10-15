import sys
input = sys.stdin.readline

def rotate():
    last = graph[-1]
    for i in range(2*N-1,0,-1):
        graph[i-1],graph[i] = graph[i],graph[i-1]
    graph[0] = last

    for i in range(N-2,-1,-1):
        robots[i+1] = robots[i]
    robots[0] = 0
    if robots[N-1] > 0:
        robots[N-1] = 0

N,K = map(int, input().split())
input = list(map(int,input().split()))
graph = input

robots = {} # 벨트 인덱스 담기
flag = False
for i in range(N):
    robots[i] = 0

time = 0
while True:
    time += 1

    rotate() # 1 과정

    for i in range(N-2,0,-1): # 2 과정
        if robots[i] > 0 and robots[i+1] == 0 and graph[i+1] > 0:
            robots[i] = 0
            robots[i + 1] = 1
            graph[i + 1] -= 1
    if robots[N-1] > 0:
        robots[N-1] = 0

    if graph[0] > 0: # 3과정
        robots[0] = 1
        graph[0] -= 1

    cnt = 0
    for g in graph: # 4 과정
        if g == 0:
            cnt += 1
        if cnt >= K:
            flag = True
            break
    if flag: break
print(time)