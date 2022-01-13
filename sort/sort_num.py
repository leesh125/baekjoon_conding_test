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

# input

# output