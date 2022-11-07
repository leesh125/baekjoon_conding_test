import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    string = list(input().rstrip())
    lq, rq = deque(), deque()
    
    for s in string:
        if s == '<':
            if lq:
                rq.appendleft(lq.pop())
        elif s == '>':
            if rq:
                lq.append(rq.popleft())
        elif s == '-':
            if lq:
                lq.pop()
        else:
            lq.append(s)
    q = lq + rq
    for n in q: print(n,end='')
    print()
    