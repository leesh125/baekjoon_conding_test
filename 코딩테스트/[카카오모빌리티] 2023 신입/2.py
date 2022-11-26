def solution(id_list, k):
    answer = 0
    dic = {}

    for id_l in id_list:
        ids = id_l.split(' ')
        ids = set(ids)
        for id in ids:
            if id not in dic:
                dic[id] = 1
                answer += 1
            else:
                if dic[id] >= k:
                    continue
                else:
                    dic[id] += 1
                    answer += 1
    return answer