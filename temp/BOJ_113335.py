# My turn
import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
bridge = deque() # 다리에 올라가 있는 트럭 담을 큐
trucks = list(map(int,input().split())) # 트럭들의 무게 리스트
totalWeight, min_time, idx = 0, 0, 0 # 다리위에 트럭 무게 총합, 최소시간, 트럭 가리킬 인덱스

while idx < n: # 다음 트럭을 가리킬 인덱스가 트럭 개수보다 넘으면 그만두기 (# 무한)
    if len(bridge) == w: # 다리 길이만큼 꽉차면
        totalWeight -= bridge.popleft() # 가장 왼쪽에 있는 트럭 빼주면서, 그만큼 무게 빼기
    temp_sum = totalWeight + trucks[idx] # 현재 다리위에 트럭들의 무게함 + 다음 올라 탈 트럭 무게
    if temp_sum <= L: # 위 무게가 다리 하중보다 적거나 같으면
        bridge.append(trucks[idx]) # 다리위에 다음 트럭 올라탐
        totalWeight = temp_sum # 무게 그만큼 추가
        idx += 1 # 다음 트럭 가리킬것임
    else: # 위 무게가 더 크면
        bridge.append(0) # 임의의 쓰레기값 0(트럭) 추가
    
    min_time += 1 # 시간 + 1
    # if idx >= n: break # 마지막 원소가 다리에 올라서자마자 종료
print(min_time + w) # 마지막 트럭이 다 건너려면 "걸린시간 + 다리 길이" 해줘야 모든 트럭이 건너는 시간 나옴
        
# Good Explanation
n, w, L = map(int, input().split())
trucks = list(map(int , input().split()))
on_turn = [0] * n

on_weight = 0
on_num = 0

turn = 1
rear = 0
head = 0
while rear < n:
    if on_turn[head] != 0 and on_turn[head] + w == turn:
        on_weight -= trucks[head]
        head += 1

    if on_weight + trucks[rear] <= L:
        on_turn[rear] = turn
        on_weight += trucks[rear]
        rear += 1
        turn += 1
    else:
        turn = on_turn[head] + w

print(turn + w - 1)