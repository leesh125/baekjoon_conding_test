import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(now):
    global visited
    global ans
    
    visited[now] = True
    team.append(now)
    num = withs[now]

    if visited[num]: # 현재 학생 방문 했으면
        if num in team:
            ans += len(team[team.index(num):])
        return
    else:
        dfs(num)

for tc in range(int(input())):
    N = int(input())
    ans = 0 
    withs = [0] + list(map(int, input().split()))
    visited = [False] * (N+1) # 방문처리

    for now in range(1,N+1): # 학생들 1~N
        if visited[now]: # 이미 방문했으면 지나가기
            continue
        team = []
        dfs(now) # 탐색
    print(N-ans)