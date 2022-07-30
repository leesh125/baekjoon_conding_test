import sys
input = sys.stdin.readline

def condition1(num): # 함수 1
    posList = [] # 좌표 기록할 리스트
    maxLike = 0 # 인접한 자리에 좋아하는 학생 수 중 가장 많은 수
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] == 0: # 빈칸이라면
                meLike = 0 # 내가 좋아하는 학생 수
                for x, y in dir:
                    nx, ny = i + x, j + y
                    # 인접한 학생이 범위 조건에 맞고, 좋아하는 학생이라면
                    if 1<=nx<N+1 and 1<=ny<N+1 and graph[nx][ny] in dic[num]: 
                        meLike += 1 # 내가 좋아하는 학생 수 + 1
                if meLike == maxLike: # 내가 좋아하는 학생 수가 최대와 같다면
                    posList.append((i,j)) # 리스트에 추가
                elif meLike > maxLike: # 그 이상이라면
                    posList.clear() # 리스트 초기화
                    posList.append((i,j)) # 좌표 리스트에 추가
                    maxLike = meLike # 갱신
    if len(posList) > 1: # 여러 자리가 후보라면
        condition2(posList,num) # 조건2 실행
    else: # 하나 밖에 없다면
        graph[posList[0][0]][posList[0][1]] = num # 기록된 좌표에 현재 학생 번호 추가
                
def condition2(posList,num): # 조건2 함수
    posList2 = []
    maxLike = 0
    for i,j in posList: # 넘어온 후보 자리만 비교
        meLike = 0
        for x, y in dir:
            nx, ny = i + x, j + y
            # 인접한 학생이 범위 조건에 맞고, 그 자리가 빈칸이라면
            if 1<=nx<N+1 and 1<=ny<N+1 and graph[nx][ny] == 0:
                meLike += 1 # 빈자리수 + 1
        if meLike == maxLike: # 빈자리 수가 최대 수와 같으면
            posList2.append((i,j)) # 리스트에 좌표 추가
        elif meLike > maxLike: # 최대수를 넘으면
            posList2.clear() # 초기화
            posList2.append((i,j)) # 리스트에 현재좌표 추가
            maxLike = meLike # 갱신
    
    if len(posList2) > 1: # 여러명이라면
        condition3(posList2, num) # 조건3 실행
    else: # 하나라면
        graph[posList2[0][0]][posList2[0][1]] = num # 현재좌표에 학생번호 추가

def condition3(posList2, num): # 조건3
    for x,y in posList2: # 넘어온 후보들로만 비교
        graph[x][y] = num # 가장 낮은 행,열에 학생번호 추가
        return # 끝
            
dir = [(-1,0),(1,0),(0,-1),(0,1)] # 인접 방향
scores = {0:0, 1:1, 2:10, 3:100, 4:1000} # 점수들
ans = 0
dic = dict() # 번호마다 좋아하는 학생 기록할 dict
N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(N*N):
    likeList = list(map(int, input().split()))
    dic[likeList[0]] = likeList[1:]

for n in dic.keys(): # 각 번호마다
    condition1(n) # 함수1 실행

for i in range(1,N+1):
    for j in range(1,N+1):
        cnt = 0
        for x, y in dir: # 인접한 학생들중
            nx, ny = i + x, j + y

            if 1<=nx<N+1 and 1<=ny<N+1 and graph[nx][ny] in dic[graph[i][j]]: # 좋아하는 학생이 있으면
                cnt += 1 # cnt += 1
        ans += scores[cnt] # 점수 누적
print(ans)
