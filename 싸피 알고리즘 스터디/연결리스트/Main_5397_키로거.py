import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = list(input().rstrip())
    ans = []
    idx = 0
    for s in string:
        if s == '<':
            if idx == 0:
                continue
            else:
                idx -= 1
        elif s == '>':
            if idx > len(ans):
                continue
            else:
                idx += 1
        elif s == '-':
            if idx == 0 or len(ans) == 0:
                continue
            else:
                ans.pop(idx)
        else:
            ans.append(s)
    print(''.join(ans))
