import sys, heapq
input = sys.stdin.readline

N = int(input())
nums, hq = [], [] # 숫자를 받을, 힙큐를 표현할 리스트

for i in range(N): # 행만큼 반복
    nums = list(map(int, input().split())) # 한줄 입력 받기
    for n in nums: # 한줄에 한 숫자씩
        if i == 0: # 초기에는
            heapq.heappush(hq, n) # 일단 n만큼 넣기
        else: 
            temp = heapq.heappop(hq) # 일단 꺼내보기(낮은 수부터 꺼내짐)
            if temp < n: # 뺀 수가 현재 대기 상태 숫자보다 작으면
                heapq.heappush(hq,n) # 더 큰 수를 힙큐에 삽입
            else: # 뺀 수가 현재 대기 상태 숫자보다 크면
                heapq.heappush(hq,temp) # 뺀 수를 힙큐에 삽입

print(heapq.heappop(hq)) # N개의 숫자중 가장 작은거를 뽑아냄

# Good Explanation
import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split()))) # 2차원 배열 형태로 숫자 삽입

indices = [N-1]*N # 가리키는 행번호를 나타낼 배열(하나씩 올라가는 구조)

for _ in range(N): 
    maxNumber = numbers[indices[0]][0] # 마지막 행의 첫번째 수를 임의의 가장 큰 수로 지정
    maxIndex = 0 # 열값도 임의로
    for i in range(1, N): # 임의가 0이니 1부터 시작
        if maxNumber < numbers[indices[i]][i]: # 다음 수가 더 크다면
            maxNumber = numbers[indices[i]][i] # 최댓값 갱신
            maxIndex = i # 인덱스도 갱신

    indices[maxIndex] -= 1 # 가장 큰 수의 행번호를 한칸 올림(더 작은수로 비교)

indices[maxIndex] += 1 # 마지막 빼기가 되는것 다시 원래대로
print(numbers[indices[maxIndex]][maxIndex]) # 행과 열에 맞는것 출력
