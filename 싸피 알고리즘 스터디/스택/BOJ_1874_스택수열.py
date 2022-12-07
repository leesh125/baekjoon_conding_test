import sys
input = sys.stdin.readline

stk = []
ans = []
flag = True
idx = 1

for _ in range(int(input())):
    n = int(input())

    if not stk or idx-1 < n:
        for i in range(idx,n+1):
            stk.append(i)
            ans.append('+')
        idx = n + 1
    
    while stk:
        if stk[-1] == n:
            stk.pop()
            ans.append('-')
            break
        temp = stk.pop()
        if temp > n:
            flag = False
            break
        ans.append('-')

print('\n'.join(ans) if flag else 'NO')
