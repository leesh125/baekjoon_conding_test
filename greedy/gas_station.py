# My turn
city = int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))
cur_c = cost[0]  # 현재 비용 값
cur_d = 0  # 현재 거리 값
res = 0 # 결과 변수

for i in range(1,len(cost)):
    if cur_c <= cost[i]:   # 현재 도시 주유비용이 다음 비용 보다 낮거나 같으면(현재 도시가 주유비용 더 쌈)
        cur_d += distance[i-1] # 현재까지 거리 누적 합
        min_c = cur_c # 아직까진 현재 도시 주유비용이 다른 지역에 비해 최저가
    else:
       res += (distance[i-1] + cur_d) * cur_c  # 결과 값에 현재 주유 비용 * (현재 거리 + 직전 도시까지 거리)
       cur_c = cost[i] # 현재 비용을 교체
       cur_d = 0 # 현재 거리도 초기화
    
    if i == len(cost)-1 and cur_d != 0:  # 만약 끝까지 갔는데 남은 거리가 있다면
        res += cur_d * cur_c  # 현재 거리 * 현재 비용 을 결과에 더해준다
        
print(res)

# Good explanation
def solution(cities, distance, price):
    cost = 0 
    min_cost = price[0] # 최소 주유 비용(임의로 첫번째로)
    for i in range(cities-1): # 도시 갯수 - 1 만큼 반복(거리가 담긴 배열과 길이 같음)
        if price[i] < min_cost: # 현재 비용이 최소 비용보다 싸면
            min_cost = price[i] # 교체
        cost += min_cost * distance[i] # 비용은 최솟값 * 다음 도시까지 거리 -> 누적합
    return cost

cities=int(input())
distance = list(map(int,input().split()))
price=list(map(int,input().split()))
print(solution(cities,distance,price))

# input
# 4
# 2 3 1
# 5 2 4 1
# or
# 4
# 3 3 4
# 1 1 1 1
# output
# 18
# or
# 10
