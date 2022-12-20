for _ in range(3):
    zero_cnt = input().rstrip().split().count('0')
    print('E' if zero_cnt == 0 else 'D' if zero_cnt == 4 else 'C' if zero_cnt == 3 else 'B' if zero_cnt == 2 else 'A')    