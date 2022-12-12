temp = input()
stk = []
num = 1
ans = 0

for i in range(len(temp)):
    if temp[i] == "(":
        stk.append(temp[i])
        num *= 2
    elif temp[i] == "[":
        stk.append(temp[i])
        num *= 3
    elif temp[i] == ")":
        if not stk or stk[-1] == "[":
            ans = 0
            break
        if temp[i-1] == "(":
            ans += num
        stk.pop()
        num //= 2
    elif temp[i] == "]":
        if not stk or stk[-1] == "(":
            ans = 0
            break
        if temp[i-1] == "[":
            ans += num
        stk.pop()
        num //= 3
print(0 if stk else ans)