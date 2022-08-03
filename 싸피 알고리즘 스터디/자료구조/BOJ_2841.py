import sys
from collections import defaultdict, deque
input = sys.stdin.readline

dict = defaultdict(deque) # 기타 줄 하나에 큐 하나씩
cnt = 0 # 누적
N, P = map(int, input().split())

for _ in range(N):
    line, prat = map(int, input().split()) # 쳐야될 줄, 프랫
    if len(dict[line]) == 0: # 해당 줄에 누르고 있는 프랫이 없으면
        dict[line].append(prat) # 프랫 추가
        cnt += 1 # 누적 += 1
    else: # 이미 누르고 있는 프랫이 있을 떄
        while True: # 반복
            if not dict[line]: # 손을 다 떼었다면 
                dict[line].append(prat) # 새로운 프랫 누르기
                cnt += 1 # 누적
                break # 빠져나오기
            now_string = dict[line][-1] # 현재 가장 높은 프랫의 줄
            if now_string < prat: # 그것이 다음 누를 프랫보다 작으면
                dict[line].append(prat) # 그대로 프랫 추가
                cnt += 1 # 누적
            elif now_string > prat: # 그것이 다음 누를 프랫보다 크면
                dict[line].pop() # 뽑아낸다
                cnt += 1 # 누적
                continue # 반복 한번 더
            else: break # 같은 음이면 그냥 기타줄 친다.
print(cnt)

# Good Explanation
import sys
input = sys.stdin.readline

n, f = map(int, input().split())
stack = [[] for _ in range(7)] # 2차원 배열로 기타의 줄 상태를 담음
ans = 0
for i in range(n):
    line, fret = map(int, input().split())
    if not stack[line]: # 해당 줄에 누르고 있는 프랫이 없으면
        stack[line].append(fret)
        ans += 1
    elif stack[line]: # 해당 줄에 누르고 있는 프랫이 있으면
        while stack[line] and fret < stack[line][-1]:
            stack[line].pop()
            ans += 1
        if stack[line] and fret == stack[line][-1]:
            pass
        elif  stack[line] and fret > stack[line][-1]:
            stack[line].append(fret)
            ans += 1
        elif not stack[line]:
            stack[line].append(fret)
            ans += 1
print(ans)