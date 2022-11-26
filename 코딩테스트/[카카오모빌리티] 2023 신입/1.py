def solution(flowers):
    dic = {}

    for flower in flowers:
        start, end = flower
        for i in range(start,end):
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

    return len(dic)

solution()