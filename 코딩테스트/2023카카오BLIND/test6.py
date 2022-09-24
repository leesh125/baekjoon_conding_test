from collections import deque

answer = 'z'
def solution(n, m, x, y, r, c, k):
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]

    def bfs():
        global answer
        q = deque()
        q.append((x,y,[],0))

        while q:
            to_x, to_y, move,cnt = q.popleft()

            if cnt == k:
                if to_x == r and to_y == c:
                    string = ''.join(move)
                    if string < answer:
                        answer = string
                        return
                continue

            for i in range(4):
                nx = to_x + dx[i]
                ny = to_y + dy[i]

                if 1<=nx<=n and 1<=ny<=m:
                    if i == 0:
                        char = 'd'
                    elif i == 1:
                        char = 'l'
                    elif i == 2:
                        char = 'r'
                    elif i == 3:
                        char = 'u'
                    q.append((nx,ny,move+[char],cnt+1))
            
    bfs()
    return answer if answer != 'z' else 'impossible'
print(solution(2, 2, 1, 1, 2, 2, 2))
#print('dr' > 'z')