import sys
from collections import deque
input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    string = input().rstrip().split(' ')

    if string[0] == 'push':
        q.append(string[1])
    elif string[0] == 'pop':
        print(q.popleft() if q else -1)
    elif string[0] == 'size':
        print(len(q))
    elif string[0] == 'empty':
        print(0 if q else 1)
    elif string[0] == 'front':
        print(q[0] if q else -1)
    elif string[0] == 'back':
        print(q[-1] if q else -1)