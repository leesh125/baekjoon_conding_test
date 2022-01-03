import sys
def dfs(x,y): #  dfs
    if x <= -1 or x >= n or y <= -1 or y >= n: # 범위를 벗어날때
        return False
    
    global cnt # 아파트 수를 나타내기 위한 cnt
    if graph[x][y] == 1: # 만약 해당 칸이 방문되있는 경우
        
        graph[x][y] = 2 # 임의의 숫자 2로 변경

        dfs(x-1, y) # dfs 재귀
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        cnt += 1 # 해당 단지의 아파트 수(dfs 체크된 경우) + 1
        return True
    return False


n = int(sys.stdin.readline()) # 빠르게 입력 받기(input() 대체)
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip()))) # 빠르게 입력 받기

cnt = 0
res = 0
cnt_arr = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:  # 해당 칸이 방문 되있는 경우(재귀)
            res += 1           # 해당 단지(이웃) +1
            cnt_arr.append(cnt) # cnt를 배열에
            cnt = 0
cnt_arr.sort() # 오름차순 정렬

print(res)
for i in cnt_arr:
    print(i)

