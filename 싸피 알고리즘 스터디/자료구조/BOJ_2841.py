from email.policy import default
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

dict = defaultdict(deque)
cnt = 0
N, P = map(int, input().split())

for _ in range(N):
    line, prat = map(int, input().split())
    if len(dict[line]) == 0:
        dict[line].append(prat)
        cnt += 1
    else:
        now_string = dict[line][-1]
        if now_string < prat:
            dict[line].append(prat)
            cnt += 1
        elif now_string > prat:
            while True:
                dict[line].pop()
                cnt += 1
                if now_string < prat:
                    dict[line].append(prat)
                    cnt += 1
                    break
                elif now_string == prat:
                    break
                if not dict[line]:
                    break
                now_string = dict[line][-1]
                

    print(dict, cnt)
print(cnt)
