a = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        a.append(n)
if a:
    print(sum(a));print(min(a))
else:
    print(-1)