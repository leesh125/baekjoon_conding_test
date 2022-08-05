from posixpath import split
import sys
input = sys.stdin.readline

dict = dict()
N, M = map(int, input().split())

for _ in range(N):
    addr, password = input().rstrip().split()
    dict[addr] = password # dictionary 사용

for _ in range(M):
    findPass = input().rstrip()
    print(dict[findPass])