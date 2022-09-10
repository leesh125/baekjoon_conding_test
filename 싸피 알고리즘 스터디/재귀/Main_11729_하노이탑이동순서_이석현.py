def hanoitop(n,start,temp,end):
    global cnt
    if n == 0:
        return
    hanoitop(n-1,start,end,temp)
    print(start,end)
    hanoitop(n-1,temp,start,end)


N = int(input())
print(2**N-1)
hanoitop(N,1,2,3)

# 1 3 7 15 31