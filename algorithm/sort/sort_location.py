import sys
n = int(sys.stdin.readline())
loc = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 
loc.sort(key=lambda x:(x[0],x[1])) # 배열 첫 번째 원소로 정렬 후, 값이 같을 경우 두 번째 원소로 정렬
for x,y in loc:
    print(x,y)

# Good explanation
import sys

N = int(input())

li = [sys.stdin.readline() for _ in range(N)]
li.sort(key=lambda x: tuple(map(int, x.split())))
print(li)
print(''.join(li))
