meeting = int(input()) # 회의시간 수 입력받기
m_time = [list(map(int, input().split())) for _ in range(meeting)] # 회의 시작, 끝 시간 받기

m_time = sorted(m_time, key=lambda x: (x[0])) # 회의 시작 시간 먼저 오름차순 정렬(같은 시간대에 끝날때 먼저 시작한 회의가 먼저오게)
m_time = sorted(m_time, key=lambda x: (x[1])) # 회의 끝 시간 오름차순 정렬

end_time = 0 # 0으로 끝나는 시작 지정

cnt = 0


for i in range(meeting):
    if m_time[i][0] >= end_time: # 해당 시작 시간이 이전 회의 끝나는 시간 보다 크거나 같으면(겹치지 않음)
       cnt += 1 # 횟수 1 증가
       end_time = m_time[i][1] # 끝나는 시간을 해당 회의시간 마지막으로 변경

print(cnt)

# input
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# output 
# 4