# My turn
import sys
from itertools import combinations

input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int,input().split())) for _ in range(N)]
# team_list = list(combinations(range(N),N//2)) # 가능한 조합 리스트
# min_gap = int(1e9) # 최솟값 변수

# for i in range(len(team_list) // 2): # 반복문을 절반까지만((처음,끝) 인덱스 조합, (2번째,끝에서 두번째) ...)
#     first_sum, last_sum = 0,0 # 처음 조합, 끝 조합 합들
#     for combi in list(combinations(team_list[i], 2)): # 해당 숫자로 만들 수 있는 팀
#         first_sum += graph[combi[0]][combi[1]] # i,j 시너지 더하기
#         first_sum += graph[combi[1]][combi[0]]  

#     for combi2 in list(combinations(team_list[-(i+1)], 2)): # 위에 조합을 제외한 나머지 숫자로 만들 수 있는 팀 
#         last_sum += graph[combi2[0]][combi2[1]]
#         last_sum += graph[combi2[1]][combi2[0]]

#     min_gap = min(min_gap, abs(first_sum - last_sum)) # 최솟값 갱신
# print(min_gap)

# Good Explanation
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 해당 학생의 팀원들의 시너지 총 합
allstat = sum(newstat) // 2 # 전체 시너지 점수 X 2(조합의 시너지 점수를 빼주려고)

mins = 65535
for l in cb(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l))) # 전체 시너지 점수 X 2 - 조합의 시너지 점수 합
print(mins)

# Good Explanation2
def dfs(depth, idx): # dfs 탐색(백트래킹)
    global min_diff
    if depth == n//2: # 
        power1, power2 = 0, 0
        for i in range(n): # 0 ~ 끝 번호
            for j in range(n): # 0 ~ 끝 번호
                if visited[i] and visited[j]: # 둘 다 방문했다면(둘이 같은팀)
                    power1 += graph[i][j] # 점수 더하기(중복 순회라 한번만 더해도됨)
                elif not visited[i] and not visited[j]: # 둘 다 방문 안했다면(둘이 같은팀)
                    power2 += graph[i][j] # 점수 더하기(중복 순회라 한번만 더해도됨)
        min_diff = min(min_diff, abs(power1-power2)) # 다른 팀과의 점수 차 최솟값 갱신
        return

    for i in range(idx, n): # 매개변수로 주어진 인덱스 부터 끝까지
        if not visited[i]: # 방문하지 않은 번호라면
            visited[i] = True # 방문 처리
            dfs(depth+1, i+1) # 깊이 +=1, 인덱스 += 1(백트래킹)
            visited[i] = False # 해당 조합이 끝나면 false처리


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0) # 깊이 0, 인덱스 0 부터 시작
print(min_diff)