# 수 정렬하기1 과 동일한 문제(더 큰 데이터 입력이 들어옮)
# My turn
import sys
a = sys.stdin.readlines() 
a = list(map(int, a)) 
for i in sorted(a[1:]): # 첫번쨰 줄 버리고 정렬된 것으로 하나씩 출력
    print(i)

# Good explanation
from sys import stdin, stdout

input() # 첫 번째 입력 흘리기
arr = sorted(map(int, stdin.read().split())) # 들어온 값들 바로 정렬
stdout.write('\n'.join(map(str,arr))) # 숫자 하나당 개행 문자를 넣어 출력(시간 단축)

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