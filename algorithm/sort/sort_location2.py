import sys
n = int(sys.stdin.readline())
loc = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 
loc.sort(key=lambda x:(x[1],x[0])) # 배열 두 번째 원소로 정렬 후, 값이 같을 경우 첫 번째 원소로 정렬
for x,y in loc:
    print(x,y)