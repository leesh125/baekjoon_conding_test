import sys
input = sys.stdin.readline

def print_star(i,j,n):
    if (i//n) % 3 == 1 and (j//n) % 3 == 1:
        print(' ',end='')
    else:
        if n == 1:
            print('*',end='')
        else:
            print_star(i,j,n//3)

N = int(input())
for i in range(N):
    for j in range(N):
        print_star(i,j,N)
    print()