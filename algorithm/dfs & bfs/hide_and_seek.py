import sys, math
from collections import deque

def bfs():
    queue = deque()
    queue.append(subin)
    if subin >= sister:     # 만약 수빈이가 동생보다 앞에있다면 
        print(subin-sister) # 수빈 - 동생 => 감소는 -1 뿐이기에 실행시간을 아낌
        return

    while queue:
        move = queue.popleft()

        if move == sister: # 이동한 곳이 동생과 같다면
            print(visited[move]) # 방문한 곳에 카운트가 담긴 배열의 원소를 출력
            break
        for i in (move-1, move+1, move*2):  # 이동한 곳-1, 이동한 곳 +1, 이동한 곳 *2 별로
            if 0<=i<=MAX and not visited[i]: # 범위를 벗어나지 않고 한번도 방문하지 않은 곳이면(같던 곳은 방문할 필요가없음)
                visited[i] = visited[move] + 1 # 새로 방문한 곳에 카운트를 이전보다 1 증가
                queue.append(i)

MAX = 100000
subin, sister = map(int,sys.stdin.readline().rstrip().split())
visited = [0] * (MAX+1)
bfs()
# 5
# 4[1] 6[1] 10[1]
# 3[2] 5[2] 8[2] 7[2] 12[2]


# 나의 접근
# 문제점 - 정답은 나오긴 하나, 범위 초과를 생각하지 않았고,
#         완전 삼진 트리일 경우에만 해당되는 코드

# import sys, math
# from collections import deque
# subin, sister = map(int,sys.stdin.readline().rstrip().split())
# cnt = 1
# dx = [-1, 1, 0]
# ans = 0
# queue = deque()
# queue.append(subin)

# if subin >= sister:
#     print(subin - sister)
#     exit()

# while queue:
#     move = queue.popleft()
#     dx[2] = move*2

#     if ans != 0:
#         print(int(math.log(ans, 3)))
#         exit()

#     for i in range(3):
#         cnt += 2
#         if i < 2:
#             nx = move + dx[i]
#         else:
#             nx = dx[2]

#         if nx == sister:
#             ans = cnt
#             break
#         else:
#             queue.append(nx)

# Good explanation
# def find(n, k):
#     if n >= k:
#         return n-k
#     elif k == 1:
#         return 1
#     elif k%2:
#         return min(find(n, k-1), find(n, k+1)) + 1
#     else:
#         return min(k-n, find(n, k//2) + 1)
  
# import sys
# n, k = map(int, sys.stdin.readline().split())
# print(find(n, k))