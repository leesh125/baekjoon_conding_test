# My turn
n = int(input())  # 대기인원 수
time = list(map(int, input().split())) # 각각 걸리는 시간
time.sort() # 오름차순 정렬(그리디: 가장 낮은 인출 시간 먼저 계산하기위해)

time_sum = 0
arr = []

for i in range(n):  
    time_sum += time[i] # 누적 인출 시간을 변수에 새로 담음
    arr.append(time_sum) # 배열로 묶어서 원소의 합을 구함

print(sum(arr))


# Good explanation
a = int(input())
l = []
total = 0
cur = 0
l = list(map(int, input().split()))

l.sort()
for x in l:
    cur += x   # 현재 사람 인출시간을 cur 변수에 누적 합
    total += cur # 전체 인출시간을 뽑기위해 누적한 인출시간을 합
print(total)