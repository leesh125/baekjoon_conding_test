# My turn
import sys
n = list(map(int,list(sys.stdin.readline().rstrip())))
for i in sorted(n,reverse=True):  # 입력받은 배열을 정렬하고 원소 하나씩 출력
    print(i, end='')
    
# Good explanation
print(''.join(sorted(input())[::-1]))

# Good explanation 2
print("".join(sorted(input(), reverse=True))) # 파이썬 문자열 정렬도 가능하네..
