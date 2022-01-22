from sys import stdin

N,C = map(int,stdin.readline().split())
homes = [int(stdin.readline()) for _ in range(N)]
homes.sort() # 이분 탐색을 위해 오름차순 정렬

min_gap = 1 # 집 사이의 최소 거리 : 1
max_gap = homes[-1]-homes[0] # 놓여진 집들 중 최대 거리 차이

result = 0
while min_gap <= max_gap: 
    cnt = 1 # 첫 번째 집은 공유기가 설치되었다고 가정(항상 최적의 해를 나타내기에)
    mid_gap = (max_gap+min_gap) // 2 # 거리차이의 중간값 구하기

    tmp = homes[0] # 첫번째 집의 좌표 임시로 담아두기
    for i in range(1, N):
        if homes[i] - tmp >= mid_gap: # 다음 집에서 임시로 담아둔 집의 거리가 거리 중간값 보다 크면
            cnt += 1 # 공유기 설치
            tmp = homes[i] # 해당 집 부터 거리를 다시 재기에 좌표를 임시변수에 담기
    
    if cnt >= C: # 만약 요구되는 공유기 설치 수보다 크면(조건을 만족하면)
        result = mid_gap # 해당 값을 결과 출력값에 담기(변할 수 있음)
        min_gap = mid_gap + 1 # 최소 거리를 중간값 보다 +1 (더 넓은 범위로 공유기를 설치한다)
    else: # 만약 요구되는 공유기 설치 수보다 작으면(조건을 만족하지 못하면)
        max_gap = mid_gap - 1 # 최대 거리를 중간값 보다 -1 (더 좁은 범위로 공유기를 설치한다)

print(result)