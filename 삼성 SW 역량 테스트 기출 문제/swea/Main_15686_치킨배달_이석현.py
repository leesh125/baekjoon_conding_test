import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chickens = []
houses = []
ans = int(1e9)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append([i,j])
        elif graph[i][j] == 1:
            houses.append([i,j])

def get_combination(chickens, M):
    result = []

    if M == 0:
        return [[]]
    
    for i in range(0, len(chickens)):
        elem = chickens[i]
        for rest in get_combination(chickens[i+1:], M-1):
            result.append([elem] + rest)
        # print()
    return result

# ==================================================================== #
# 1. Not Using Libarary  

for combi in get_combination(chickens, M):
    chicken_dis = 0
    for house in houses:
        houseX, houseY = house
        temp = int(1e9)
        for c in combi:
            chickenX, chickenY = c
            temp = min(temp,abs(chickenX-houseX) + abs(chickenY-houseY))
        chicken_dis += temp
    ans = min(ans, chicken_dis)
print(ans)
    

# ==================================================================== #
# 1. Using Libarary        

# for li in list(combinations(chickens,M)):
#     chicken_dis = 0
#     for house in houses:
#         houseX, houseY = house
#         temp = int(1e9)
#         for l in li:
#             chickenX, chickenY = l
#             temp = min(temp, abs(houseX-chickenX) + abs(houseY-chickenY))
#         chicken_dis += temp
#     ans = min(ans, chicken_dis)


# print(ans)
    