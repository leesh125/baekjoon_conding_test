nums = [0] * 10
max_num, max_idx = 0,0
for s in input().rstrip():
    n = int(s)
    if n == 9:
        nums[6] += 1
    else:
        nums[n] += 1
nums[6] = (nums[6] + 1) // 2

for i in range(10):
    if nums[i] > max_num:
        max_num = nums[i]
print(max_num)