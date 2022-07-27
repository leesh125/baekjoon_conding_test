# My turn
import sys
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(n)]
for n in sorted(nums): # 입력받은 수를 정렬 한 배열을 하나씩 출력
    print(n) 

# Good explanation
# import sys
# a = sys.stdin.readlines()
# a = list(map(int, a))
# for i in sorted(a[1:]):
#     print(i)

# # input
# 5
# 5
# 4
# 3
# 2
# 1

# # output
# 1
# 2
# 3
# 4
# 5