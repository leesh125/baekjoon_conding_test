import sys
input = sys.stdin.readline

temp = input()
now, ans = 0,0
flag = False

for i in range(len(temp)-1):
    if temp[i] == '(':
        if temp[i+1] == ')':
            ans += now
            flag = True
        else:
            now += 1
    else:
        if flag:
            flag = False
            continue
        now -= 1
        ans += 1
print(ans)