import sys
input = sys.stdin.readline

N, M, X, Y, K = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
dice = [0,0,0,0,0,0] # 바닥, 앞, 오른, 왼, 뒤, 천장
for dir in direction: # 방향마다
    if dir == 1: # 동
        if Y + 1 >= M:
            continue
        Y += 1
        # 천장 -> 오른 # 왼쪽 -> 천장 # 바닥 -> 왼쪽 # 오른 -> 바닥
        dice[2],dice[5],dice[4],dice[0] = dice[5],dice[4],dice[0],dice[2]   
    elif dir == 2: # 서
        if Y - 1 < 0:
            continue
        Y -= 1
        # 천장 -> 왼쪽 # 오른 -> 천장 # 바닥 -> 오른 # 왼쪽 -> 바닥
        dice[4],dice[5],dice[2],dice[0] = dice[5],dice[2],dice[0],dice[4]   
    elif dir == 3: # 북쪽
        if X - 1 < 0:
            continue
        X -= 1
        # 천장 -> 뒤 # 앞 -> 천장 # 바닥 -> 앞 # 뒤 -> 바닥
        dice[3],dice[5],dice[1],dice[0] = dice[5],dice[1],dice[0],dice[3]    
    elif dir == 4: # 남쪽
        if X + 1 >= N:
            continue
        X += 1
        # 천장 -> 앞 # 뒤 -> 천장 # 바닥 -> 뒤 # 앞 -> 바닥
        dice[0],dice[1],dice[5],dice[3] = dice[1],dice[5],dice[3],dice[0]  

    if graph[X][Y] != 0: # 지도에 위치가 0이 아니라면
        dice[0] = graph[X][Y] # 바닥에 복사
        graph[X][Y] = 0 # 해당 위치 값은 0으로
    else: # 지도에 위치가 0이 아니라면
        graph[X][Y] = dice[0] # 바닥에 있는 숫자를 지도에 복사시키기
    print(dice[5]) # 천장값 출력
        