def recursive(b):
    if b == 1:
        return remain 
    else:
        if b % 2:
            return (recursive(b // 2)**2*a)%c
        else:
            return (recursive(b // 2)**2)%c

a,b,c = map(int, input().split())
remain = a % c

print(recursive(b))

# Good Explanation
print(pow(*map(int,input().split()))) # 내장 함수 사용