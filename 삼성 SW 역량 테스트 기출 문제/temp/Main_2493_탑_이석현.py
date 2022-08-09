import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
stack = [0]
answer = [0 for _ in range(N)]

for i in range(N):
    while stack:
        if nums[stack[-1]] > nums[i]:
            answer[i] = stack[-1] + 1
            break
        else:
            stack.pop()
    stack.append(i)

print(*answer)
