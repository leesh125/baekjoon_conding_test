meeting = int(input())
m_time = [list(map(int, input().split())) for _ in range(meeting)]

m_time = sorted(m_time, key=lambda x: (x[0]))
m_time = sorted(m_time, key=lambda x: (x[1]))

end_time = 0

cnt = 0


for i in range(meeting):
    if m_time[i][0] >= end_time:
       cnt += 1
       end_time = m_time[i][1]

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