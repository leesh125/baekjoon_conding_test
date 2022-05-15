import sys
input = sys.stdin.readline

N,M = map(int, input().split())
x,y,dir = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,1,0] # 위, 오른, 아래 ,왼쪽 방향
dy = [0,1,0,-1] 

# 청소하는 함수
def clean(cur_x,cur_y,cur_dir,graph): 
    cnt,cleaning,graph[cur_x][cur_y] = 0,1,2 # 회전 수 = 0, 청소 횟수 = 1, 현재 위치 청소 처리

    while True:
        if cnt != 4: # 2-a
            next_x = cur_x + dx[(cur_dir-1) % 4] # 다음 갈 좌표
            next_y = cur_y + dy[(cur_dir-1) % 4]
            
            if graph[next_x][next_y] != 0: # 다음 좌표가 벽이면
                cnt += 1 # a 진행 횟수
            else: # 다음이 빈 공간이면
                cleaning += 1 # 청소 횟수 += 1
                graph[next_x][next_y] = 2 # 해당 칸 이동과 동시에 청소
                cur_x,cur_y,cnt = next_x,next_y,0 # 좌표와 회전 횟수 초기화
            cur_dir = (cur_dir-1) % 4 # 회전
        else: # 2-b
            next_x = cur_x + dx[(cur_dir-2) % 4] # 다음 갈 좌표(현재방향의 뒤)
            next_y = cur_y + dy[(cur_dir-2) % 4]

            if graph[next_x][next_y] == 1: # 벽이면
                break # 빠져나오기
            else: # 벽이 아니면
                cur_x,cur_y,cnt = next_x, next_y,0 # 해당 좌표로 이동
    return cleaning

print(clean(x,y,dir,graph))
