import sys
input = sys.stdin.readline

temp = list(input().split())
N = int(temp[0])
nums = []
if len(temp) != 1:
    for n in temp[1:]:
        nums.append(int(n[::-1]))
while len(nums) != N:
    temp = list(input().split())
    for n in temp:
        nums.append(int(n[::-1]))
for n in sorted(nums):
    print(n)
